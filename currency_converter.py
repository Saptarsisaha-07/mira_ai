from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "sb-26f6b50ec4679b728e695abebb76fba7"})

version = "1.0.0"
input_data = {
    "amount": "1000",
    "to_currency": "INR",
    "from_currency": "Radianite Points"
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@itz-sapta-07/currency-data/{version}"
else:
    flow_name = "@itz-sapta-07/currency-data"

result = client.flow.execute(flow_name, input_data)
print(result)