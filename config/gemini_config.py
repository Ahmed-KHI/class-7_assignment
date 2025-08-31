"""
Gemini Model Configuration
Following teacher's pattern for model setup
"""
from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables
load_dotenv(find_dotenv(), override=True)

# Get Gemini configuration from environment
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_PATH")  
gemini_model_name = os.getenv("GEMINI_MODEL_NAME")

# Create Gemini client and model following teacher's pattern
gemini_client = AsyncOpenAI(api_key=gemini_api_key, base_url=gemini_base_url)
GEMINI_MODEL = OpenAIChatCompletionsModel(openai_client=gemini_client, model=str(gemini_model_name))
