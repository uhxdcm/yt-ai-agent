import os
from google import genai
from google.genai import types

# Initialize the Gemini client using the environment variable we'll set up in GitHub
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def generate_youtube_content():
    # Prompt engineering the agent for YouTube Shorts / Automation
    prompt = """
    You are an expert YouTube automation growth agent. 
    1. Pick a viral, high-interest evergreen topic currently trending among Gen Z/young adults (e.g., tech secrets, psychology hacks, futuristic AI tools, or mind-blowing space facts).
    2. Write a 45-second high-retention YouTube Short script with a powerful hook in the first 3 seconds.
    3. Provide an optimized catchy title, a description, and 5 viral hashtags.
    
    Format the output cleanly with labels: TITLE, SCRIPT, DESCRIPTION, HASHTAGS.
    """

    # Calling Gemini 2.5 Flash for fast, intelligent generation
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    
    print("--- AUTOMATED YOUTUBE CONTENT GENERATED ---")
    print(response.text)

if __name__ == "__main__":
    generate_youtube_content()
