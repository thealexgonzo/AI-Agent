import os
import sys
from google import genai
from dotenv import load_dotenv

if len(sys.argv) <= 1:
    print("ERROR: A prompt must be provided")
    exit(1)
else:
    def main():
        load_dotenv()
        api_key = os.environ.get("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', 
            contents=sys.argv
        )

        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(f"Response: {response.text}")

    if __name__=="__main__":
        main()