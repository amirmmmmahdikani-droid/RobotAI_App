"""
Voice System
"""


import subprocess
import os



def speak(text):

    """
    تبدیل متن به صدا
    """

    try:

        # برای اندروید با Termux

        result = subprocess.run(
            [
                "termux-tts-speak",
                text
            ],
            capture_output=True,
            text=True
        )


        return "صدا پخش شد"


    except Exception as e:

        return "خطای صدا: " + str(e)





def listen():

    """
    دریافت صدا

    بعداً به میکروفون و تشخیص گفتار وصل می‌شود
    """

    return None





def save_audio(path, data):

    try:

        with open(path, "wb") as f:

            f.write(data)


        return True


    except:

        return False





def voice_available():

    return True
