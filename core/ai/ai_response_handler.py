# ai_response_handler.py

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ai_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a real-time assistant for a Twitch-integrated Unity game."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"[AI Response Error] {str(e)}")
        return "[AI Error] Unable to process command."

# Example usage (can be removed in production)
if __name__ == "__main__":
    user_cmd = input("Enter a Twitch command or game prompt: ")
    print("AI Response:", generate_ai_response(user_cmd))
