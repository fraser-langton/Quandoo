import os

from dotenv import load_dotenv

load_dotenv()

AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
AGENT_ID = os.environ.get('AGENT_ID')

# Test data
MERCHANT_ID = 49294
CUSTOMER_ID = "44eebac2-baf7-4375-bb73-7363d15ba0fc"
RESERVATION_ID = "f10ec261-9a7d-4704-820b-3db509296b62"
