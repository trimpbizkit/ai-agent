import os
import argparse
from dotenv import load_dotenv
from google import genai

_MODEL = "gemini-2.5-flash"


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("failed to load api key from .env")
    
    contents = args.user_prompt

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model=_MODEL, contents=contents)

    if response.usage_metadata is None:
        raise RuntimeError("no usage metadata on response, likely the result of a failed API request")

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response:\n{response.text}")



if __name__ == "__main__":
    main()
