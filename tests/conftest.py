import os

from dotenv import load_dotenv

load_dotenv()

AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
AGENT_ID = os.environ.get('AGENT_ID')
MERCHANT_ID = os.environ.get('MERCHANT_ID')
