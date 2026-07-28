"""
ESP32 WiFi Controller
"""

import requests

from config import (
    ESP32_IP,
    ESP32_PORT,
    REQUEST_TIMEOUT
)



def base_url():

    return f"http://{ESP32_IP}:{ESP32_PORT}"



def send_command(command):

    try:

        url = base_url() + "/command"


        response = requests.get(
            url,
            params={
                "cmd": command
            },
            timeout=REQUEST_TIMEOUT
        )


        return response.text



    except requests.exceptions.Timeout:

        return "زمان اتصال به ESP32 تمام شد"



    except Exception as e:

        return "خطای ESP32: " + str(e)




def get_status():

    try:

        url = base_url() + "/status"


        response = requests.get(
            url,
            timeout=REQUEST_TIMEOUT
        )


        return response.text



    except Exception as e:

        return "ESP32 خاموش یا قطع است: " + str(e)




def say_on_robot(text):

    return send_command(
        "say:" + text
    )



def move_robot(direction):

    return send_command(
        "move:" + direction
    )



def touch_event():

    return send_command(
        "touch"
    )
