"""
OpenRouter AI Connection
"""

import requests

from config import (
    API_KEY,
    MODEL,
    SYSTEM_PROMPT,
    INTERNET_TIMEOUT
)


API_URL = "https://openrouter.ai/api/v1/chat/completions"



def ask_ai(message):

    if not API_KEY:

        return ""


    headers = {

        "Authorization": f"Bearer {API_KEY}",

        "Content-Type": "application/json",

        "HTTP-Referer": "http://localhost",

        "X-Title": "Tobi Robot AI"

    }



    data = {

        "model": MODEL,

        "messages": [

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": message
            }

        ]

    }



    try:

        response = requests.post(

            API_URL,

            headers=headers,

            json=data,

            timeout=INTERNET_TIMEOUT

        )


        result = response.json()


        if "choices" in result:

            return result["choices"][0]["message"]["content"]


        if "error" in result:

            return "خطای OpenRouter: " + str(result["error"])


        return str(result)



    except Exception as e:

        return "خطای اتصال: " + str(e)
def ai_available():

    if API_KEY:
        return True

    return False
