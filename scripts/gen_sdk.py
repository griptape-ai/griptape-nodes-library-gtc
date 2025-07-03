import copy
import logging
import subprocess
import sys
from pathlib import Path

import httpx
import yaml

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def recurse_openapi_spec_for_edits(spec: dict | list) -> None:
    if isinstance(spec, dict):
        # 0) convert 400/500 response ranges to 4XX/5XX
        responses = spec.get("responses")
        if isinstance(responses, dict):
            if "400" in responses and "401" not in responses:
                responses["401"] = responses.get("400")
            if "400" in responses and "403" not in responses:
                responses["403"] = responses.get("400")
            if "400" in responses and "404" not in responses:
                responses["404"] = responses.get("400")
            if "400" in responses and "406" not in responses:
                responses["406"] = responses.get("400")
            if "400" in responses and "409" not in responses:
                responses["409"] = responses.get("400")
            if "400" in responses and "422" not in responses:
                responses["422"] = responses.get("400")

        # 1) strip out any titles on oneOf items
        if "oneOf" in spec and isinstance(spec["oneOf"], list):
            for item in spec["oneOf"]:
                if isinstance(item, dict) and "title" in item:
                    del item["title"]

        # 2) if this is the CreateAsset operation, clone its 201 → 200
        if spec.get("operationId") == "CreateAsset":
            responses = spec.get("responses", {})
            if "201" in responses and "200" not in responses:
                # deep-copy the 201 response into 200
                responses["200"] = copy.deepcopy(responses["201"])
                # tweak the description if present
                desc = responses["200"].get("description")
                if isinstance(desc, str):
                    responses["200"]["description"] = desc.replace("201 response", "200 response")

        # 3) recurse into all values
        for v in spec.values():
            recurse_openapi_spec_for_edits(v)
    elif isinstance(spec, list):
        for item in spec:
            recurse_openapi_spec_for_edits(item)


def _clean_openapi_spec(spec_path: Path) -> None:
    """Clean the OpenAPI specification by removing 'title' fields from any 'oneOf' schema objects."""
    try:
        # Load the spec
        with spec_path.open("r", encoding="utf-8") as f:
            spec = yaml.safe_load(f)
    except Exception as e:
        message = f"Error loading OpenAPI spec for cleaning: {e}"
        logger.info(message)
        sys.exit(1)

    recurse_openapi_spec_for_edits(spec)

    try:
        # Write cleaned spec back
        with spec_path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(spec, f, sort_keys=False)

        message = f"Cleaned OpenAPI spec: {spec_path}"
        logger.info(message)
    except Exception as e:
        message = f"Error writing cleaned OpenAPI spec: {e}"
        logger.exception(message)
        sys.exit(1)


def _download_openapi_spec(url: str, output_path: Path) -> None:
    """Download the OpenAPI specification from the given URL and save it to the specified output path."""
    try:
        response = httpx.get(url)
        response.raise_for_status()
        with output_path.open("wb") as file:
            file.write(response.content)

        message = f"OpenAPI spec downloaded successfully to {output_path}"
        logger.info(message)
    except Exception as e:
        message = f"Error downloading OpenAPI spec: {e}"
        logger.exception(message)
        sys.exit(1)


def main():
    """Main entry point for downloading, cleaning, and generating the SDK from the OpenAPI spec."""
    griptape_cloud_dir = Path(__file__).parent.parent / "griptape_cloud"
    output_dir = griptape_cloud_dir / "generated"
    output_dir.mkdir(parents=True, exist_ok=True)

    openapi_spec = "https://griptape-cloud-assets.s3.amazonaws.com/Griptape.openapi.yaml"
    openapi_file = Path(__file__).parent.parent / "Griptape.openapi.yaml"
    _download_openapi_spec(openapi_spec, openapi_file)
    _clean_openapi_spec(openapi_file)

    # Use openapi-python-client to generate the SDK
    command = [
        "openapi-python-client",
        "generate",
        "--path",
        str(openapi_file),
        "--output-path",
        str(output_dir),
        "--overwrite",
    ]

    # Move the generated SDK to the correct directory
    move_command = [
        "cp",
        "-r",
        str(output_dir / "griptape_cloud_client"),
        str(griptape_cloud_dir),
    ]

    try:
        subprocess.run(command, check=True)  # noqa: S603
        subprocess.run(move_command, check=True)  # noqa: S603
        message = f"SDK generated successfully in {output_dir}"
        logger.info(message)
    except subprocess.CalledProcessError as e:
        message = f"Error generating SDK: {e}"
        logger.exception(message)
        sys.exit(1)


if __name__ == "__main__":
    main()
