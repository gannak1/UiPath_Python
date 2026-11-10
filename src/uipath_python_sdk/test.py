from uipath.platform import UiPath
# Initialize the SDK
sdk = UiPath()
# Execute a process
job = sdk.processes.invoke(
    name="MyProcess",
    input_arguments={"param1": "value1", "param2": 42}
)
# Work with assets
asset = sdk.assets.retrieve(name="MyAsset")
