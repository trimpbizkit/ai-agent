import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import MAX_ITERATIONS
from prompts import system_prompt
from functions.call_function import available_functions, call_function

_MODEL = "gemini-2.5-flash"


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("failed to load api key from .env")
    
    
    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
    
    # Limited iteration loop to call the model
    for _ in range(MAX_ITERATIONS):
        response, function_responses = generate_content(client, messages, args.verbose)
        if response is None and function_responses is None:
            return   
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)
        messages.append(types.Content(role="user", parts=function_responses))

    # Max num of iterations reached and model produced no final response
    print(f"Reached {MAX_ITERATIONS} without generating a response")
    exit(1)

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model=_MODEL,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
        )
    )

    if not response.usage_metadata:
        raise RuntimeError("no usage metadata on response, likely the result of a failed API request")
    
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    if not response.function_calls:
        print(f"Final response:\n{response.text}")
        return None, None

    function_call_results = []
    for function_call in response.function_calls:
        function_call_result = call_function(function_call, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
            or not function_call_result.parts[0].function_response.response   
        ):
            raise RuntimeError(f"Empty function response for {function_call.name}")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_call_results.append(function_call_result.parts[0])
    return response, function_call_results
    


if __name__ == "__main__":
    main()
