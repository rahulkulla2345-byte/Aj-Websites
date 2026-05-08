import os
import json

from openai import OpenAI
from dotenv import load_dotenv

from prompts import AUDIENCE_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def analyze_website(content):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": AUDIENCE_PROMPT
            },
            {
                "role": "user",
                "content": content[:120000]
            }
        ]
    )

    result = response.choices[0].message.content

    try:
        return json.loads(result)

    except:
        return {
            "error": result
        }
