from dotenv import load_dotenv
from mira_sdk import MiraClient
import os

load_dotenv()
client = MiraClient(config={"API_KEY": os.getenv("sb-bdceae543603b3afd0e90ce55f78e23e")})
