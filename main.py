import os
import argparse
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
gemini_client = genai.Client(api_key=api_key)


def main():
    if api_key is None:
        raise RuntimeError("Please check your secrets' source file. A key with the value provided was not found.")
    parser = argparse.ArgumentParser(
        prog="gemini-client",
        usage="Enter your prompt here: ",
        description="Takes your question or prompt, and returns Gemini 2.5 Flash's response to the prompt",
    )
    parser.add_argument("user_prompt", type=str, help="Enter your prompt or questions for Gemini AI here: ")
    args = parser.parse_args()
    _prompt = args.user_prompt
    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=args.user_prompt,
    )
    if response is None or response.usage_metadata is None:
        raise RuntimeError("No response was provide. Please check configuration and connection and try again!")

    req_token_count, res_token_count, gemini_response = (
        response.usage_metadata.prompt_token_count,
        response.usage_metadata.candidates_token_count,
        response.text,
    )

    results = f"""
User prompt: {_prompt}
Prompt tokens: {req_token_count}
Response tokens: {res_token_count}
Response:
{gemini_response}"""
    print(results)

if __name__ == "__main__":
    main()
