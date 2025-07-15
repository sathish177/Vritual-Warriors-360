import os
from dotenv import load_dotenv

def init_env():
    """
    Initializes environment variables by loading them from a .env file.
    Ensures GOOGLE_API_KEY is set.
    """
    load_dotenv() # Load variables from .env file
    if not os.getenv("GOOGLE_API_KEY"):
        print("Warning: GOOGLE_API_KEY environment variable not set.")
        print("Please create a .env file in the project root with GOOGLE_API_KEY='YOUR_API_KEY'.")
        # In a production scenario, you might want to exit or raise an error here.
