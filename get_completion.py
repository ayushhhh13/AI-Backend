import openai
from dotenv import load_dotenv
import os 

# Load environment variables
load_dotenv()
import base64

# Decode Google credentials from base64
google_creds_b64 = os.getenv("GOOGLE_CREDENTIALS_B64")
if google_creds_b64:
    with open("google_credentials.json", "wb") as f:
        f.write(base64.b64decode(google_creds_b64))

# Set the env var so Google libraries can find it
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google_credentials.json"
# Configure Azure OpenAI API for Chatbot
openai.api_type = "azure"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_version = os.getenv("OPENAI_API_VERSION")
assemblyai_api_key = os.getenv("ASSEMBLYAI_API_KEY")

if not openai.api_key:
    raise ValueError("OPENAI_API_KEY is missing from the .env file!")
if not assemblyai_api_key:
    raise ValueError("Assembly ai key not working.")

def get_completion(prompt, engine="gpt-4o-aispeaking"):
    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
            engine=engine,
            messages=messages,
            temperature=0.7
        )

    content = response.choices[0].message["content"]

    if content.startswith("```json") and content.endswith("```"):
        content = content[7:-3].strip()

    return content
