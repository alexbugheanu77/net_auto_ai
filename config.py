import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Load from environment variable

# Network Device Credentials (Example -  Securely store/manage these in a real application)
NETWORK_DEVICES = {
    "SW1": {
        "device_type": "cisco_ios",
        "host": "192.168.1.10",
        "username": "your_username",
        "password": "your_password",
        "secret": "your_enable_secret"  # Optional, for enable mode
    },
    # Add more devices as needed
}


# MODEL to be used on OpenAI
MODEL = "gpt-3.5-turbo" # gpt-4 or gpt-3.5-turbo or other models

# Temperature
TEMPERATURE = 0.0 # 0.0 is a good start, change it accordingly

# MAX_TOKENS for the completion
MAX_TOKENS = 2048