# Griptape Cloud Nodes

This library provides Griptape Nodes for interacting with Griptape Cloud APIs and services. You can use these nodes to interact with any of the available Griptape Cloud APIs.

**IMPORTANT:** To use these nodes, you will need an API key from Griptape Cloud. An API Key should have been generated for you on the initial setup of Griptape Nodes, so you may use that key. Please visit the [Griptape Cloud console](https://cloud.griptape.ai/configuration/api-keys) to manage your API Keys if needed.

To configure your keys within the Griptape Nodes IDE:

1. Open the **Settings** menu.
1. Navigate to the **API Keys & Secrets** panel.
1. Add a new secret configuration for the service named `Griptape`.
1. Enter your `GT_CLOUD_API_KEY` in the respective field.

## Add your library to your installed Engine

If you haven't already installed your Griptape Nodes engine, follow the installation steps [HERE](https://github.com/griptape-ai/griptape-nodes).
After you've completed those and you have your engine up and running:

1. Copy the path to your `library.json`. Right click on the file, and `Copy Path` (Not `Copy Relative Path`)
   ![Copy path of the library.json](./images/get_json_path.png)
1. Start up the engine!
1. Navigate to settings
   ![Open Settings](./images/open_settings.png)
1. Open your settings and go to the App Events tab. Add an item in **Libraries to Register**
   ![Add Library to Register](./images/add_library.png)
1. Paste your copied `library.json` path from earlier into the new item
   ![Paste in your absolute path](./images/paste_library.png)
1. Exit out of Settings. It will save automatically!
1. Open up the **Libraries** dropdown on the left sidebar
   ![See Libraries](./images/see_libraries.png)
1. Your newly registered library should appear! Drag and drop nodes to use them!
   ![Library Display](./images/final_image.png)
