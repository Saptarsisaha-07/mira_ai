from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "sb-bdceae543603b3afd0e90ce55f78e23e"})

version = "1.0.3"
input_data = {
    "remix_style": "",
    "original_recipe": ""
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@cosmic-labs/recipe-remixer/{version}"
else:
    flow_name = "@cosmic-labs/recipe-remixer"

result = client.flow.execute(flow_name, input_data)
print(result)