from __future__ import annotations

import json
import logging
import subprocess
import sys
import threading
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger("griptape_cloud_subprocess_executor")


class GriptapeCloudSubprocessExecutor:
    """Handles execution of subprocesses in background threads with lifecycle management."""

    def __init__(self) -> None:
        self._process: subprocess.Popen[str] | None = None
        self._thread: threading.Thread | None = None
        self._is_running = False

    def execute_python_script(self, script_path: Path, args: list[str] | None = None, cwd: Path | None = None) -> None:
        """Execute a Python script in a background thread.

        Args:
            script_path: Path to the Python script to execute
            args: Additional command line arguments
            cwd: Working directory for the subprocess
        """
        if self._is_running:
            logger.warning("Another subprocess is already running. Terminating it first.")
            self.terminate()

        args = args or []
        command = [sys.executable, str(script_path), *args]

        def run_subprocess() -> None:
            try:
                logger.info("Starting subprocess: %s", " ".join(command))
                logger.info("Working directory: %s", cwd)
                self._process = subprocess.Popen(  # noqa: S603
                    command,
                    cwd=cwd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )
                self._is_running = True
                logger.info("Subprocess started with PID: %s", self._process.pid)

                # Wait for process completion and capture output
                stdout, stderr = self._process.communicate()
                returncode = self._process.returncode

                # Log all output regardless of return code
                if stdout:
                    logger.info("Subprocess stdout: %s", stdout)
                if stderr:
                    logger.info("Subprocess stderr: %s", stderr)

                if returncode == 0:
                    logger.info("Subprocess completed successfully with return code: %d", returncode)
                else:
                    logger.error("Subprocess failed with return code: %d", returncode)

            except Exception as e:
                logger.error("Error running subprocess: %s", e)
            finally:
                self._is_running = False
                self._process = None

        self._thread = threading.Thread(target=run_subprocess, daemon=True)
        self._thread.start()

    def execute_workflow(self, executor_workflow_path: Path, workflow_input: dict[str, Any] | None = None) -> None:
        """Execute a workflow script with JSON input.

        Args:
            executor_workflow_path: Path to the executor workflow script
            workflow_input: Input parameters to pass as JSON
        """
        workflow_input = workflow_input or {}
        args = ["--json-input", json.dumps(workflow_input)]
        self.execute_python_script(script_path=executor_workflow_path, args=args, cwd=executor_workflow_path.parent)

    def is_running(self) -> bool:
        """Check if a subprocess is currently running."""
        return self._is_running

    def terminate(self, timeout: float = 5.0) -> bool:
        """Terminate the running subprocess.

        Args:
            timeout: How long to wait for graceful termination before force killing

        Returns:
            True if successfully terminated, False otherwise
        """
        if not self._is_running or not self._process:
            return True

        try:
            logger.info("Terminating subprocess...")
            self._process.terminate()

            # Wait for graceful termination
            try:
                self._process.wait(timeout=timeout)
                logger.info("Subprocess terminated gracefully")
                return True  # noqa: TRY300
            except subprocess.TimeoutExpired:
                logger.warning("Subprocess did not terminate gracefully, force killing...")
                self._process.kill()
                self._process.wait()
                logger.info("Subprocess force killed")
                return True

        except Exception as e:
            logger.error("Error terminating subprocess: %s", e)
            return False
        finally:
            self._is_running = False
            self._process = None

    def wait_for_completion(self, timeout: float | None = None) -> bool:
        """Wait for the subprocess to complete.

        Args:
            timeout: Maximum time to wait (None for no timeout)

        Returns:
            True if completed within timeout, False if timed out
        """
        if not self._thread:
            return True

        self._thread.join(timeout=timeout)
        return not self._thread.is_alive()

    def get_status(self) -> dict[str, Any]:
        """Get current status information."""
        return {
            "is_running": self._is_running,
            "has_process": self._process is not None,
            "has_thread": self._thread is not None and self._thread.is_alive(),
            "process_pid": self._process.pid if self._process else None,
        }
