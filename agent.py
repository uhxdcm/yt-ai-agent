import os
from google import genai

# Verify secret key
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("ERROR: GEMINI_API_KEY environment variable is missing or empty!")
else:
    print("SUCCESS: API key detected by GitHub Actions.")

client = genai.Client(api_key=api_key)

def generate_youtube_content():
    prompt = """
    You are an expert YouTube automation growth agent. 
    1. Pick a viral, high-interest evergreen topic currently trending among Gen Z/young adults.
    2. Write a 45-second high-retention YouTube Short script with a powerful hook in the first 3 seconds.
    3. Provide an optimized catchy title, a description, and 5 viral hashtags.
    
    Format the output cleanly with labels: TITLE, SCRIPT, DESCRIPTION, HASHTAGS.
    """

    # Updated model name to match the latest available endpoint
    response = client.models.generate_content(
        model='gemini-3.6-flash',
        contents=prompt,
    )
    
    print("--- AUTOMATED YOUTUBE CONTENT GENERATED ---")
    print(response.text)

if __name__ == "__main__":
    generate_youtube_content()
    
