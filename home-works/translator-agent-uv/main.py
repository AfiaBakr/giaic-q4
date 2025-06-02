# uv pip install openai-agents
# uv pip install python-dotenv

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
print(gemini_api_key)

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")


external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True)

# Define the Translator agent
translator = Agent(
    name='Translator Agent',
    instructions="""
    You are a Translator agent. Translate from:
    - Urdu to English
    - English to Urdu
    - Urdu to Arabic
    - Arabic to Urdu
    Always respond with only the translated text.
    """
)

# Ask user to choose translation direction
print("Choose translation direction:")
print("1. Urdu to English")
print("2. English to Urdu")
print("3. Urdu to Arabic")
print("4. Arabic to English")

choice = input("Enter the number of your choice (1 - 4): ").strip()

language_map = {
    "1": "Urdu to English",
    "2": "English to Urdu",
    "3": "Urdu to Arabic",
    "4": "Arabic to English"
}

if choice not in language_map:
    print("Invalid choice.")
    exit()

# Take input sentence from user
sentence = input(f"Enter the sentence to translate ({language_map[choice]}): ").strip()

# Construct the input prompt
prompt = f"Translate this sentence ({language_map[choice]}): {sentence}"

# Run the agent synchronously
response = Runner.run_sync(
    translator,
    input=prompt,
    run_config=config
)

# Show the translated output
print("\nTranslated Output: ")
print(response.final_output)