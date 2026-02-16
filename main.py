import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
API_KEY: str | None = os.environ.get("GEMINI_API_KEY")


def main():
    if API_KEY is None:
        raise RuntimeError(
            "Please check your secrets' source file. A key with the value provided was not found."
        )
    gemini_client = genai.Client(api_key=API_KEY)
    parser = argparse.ArgumentParser(
        prog="gemini-client",
        usage="Enter your prompt here: ",
        description="Takes your question or prompt, and returns Gemini 2.5 Flash's response to the prompt",
    )
    parser.add_argument(
        "user_prompt",
        type=str,
        help="Enter your prompt or questions for Gemini AI here: ",
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    _prompt = args.user_prompt
    messages: list[types.Content] = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]
    response: genai.GenerateContentResponse = gemini_client.models.generate_content(  # type: ignore
        model="gemini-2.5-flash",
        contents=messages,
    )

    if response is None or response.usage_metadata is None:  # type: ignore
        raise RuntimeError(
            "No response was provide. Please check configuration and connection and try again!"
        )

    req_token_count, res_token_count, gemini_response = (  # type: ignore
        response.usage_metadata.prompt_token_count,  # type: ignore
        response.usage_metadata.candidates_token_count,  # type: ignore
        response.text,  # type: ignore
    )
    response: str = f"Response: {gemini_response}"
    verbose_response: str = f"""
User prompt: {_prompt}
Prompt tokens: {req_token_count}
Response tokens: {res_token_count}
{response}"""
    if args.verbose:
        print(verbose_response)
    else:
        print(response)


if __name__ == "__main__":
    main()
