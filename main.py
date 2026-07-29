"""
Tobi AI Robot App
Main Controller
"""


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.resources import resource_add_path
import os

from config import ROBOT_NAME


from offline import offline_answer

from ai import ask_ai, ai_available

from memory import add

from owner import (
    login,
    logout,
    is_owner,
    protect_private
)

from esp32 import send_command

from voice import speak


resource_add_path(os.path.join(os.path.dirname(__file__), "fonts"))
Builder.load_file("robot.kv")



class RobotUI(BoxLayout):

    messages = ""


    def add_message(self, sender, text):

        self.messages += (
            f"\n{sender}: {text}\n"
        )


        self.ids.chat.text = self.messages



    def send_message(self):
        print("SEND BUTTON OK")
        text = self.ids.input_box.text.strip()


        if not text:

            return

        print("MESSAGE RECEIVED:", text)

        self.ids.input_box.text = ""



        self.add_message(
            "👤 امیر",
            text
        )


        add(
            "user",
            text
        )


        Clock.schedule_once(
            lambda dt: self.process_message(text),
            0.1
        )



    def process_message(self, text):


        # بررسی اطلاعات خصوصی

        if protect_private(text):

            answer = (
                "⛔ برای اطلاعات خصوصی "
                "ابتدا رمز صاحب را وارد کن."
            )


        else:

            # جواب آفلاین

            answer = offline_answer(text)



            # اگر جواب آفلاین نبود، AI

            if answer is None:


                if ai_available():

                    answer = ask_ai(text)


                else:

                    answer = (
                        "برای این سوال "
                        "به اینترنت و API نیاز دارم."
                    )



        self.add_message(
            ROBOT_NAME,
            answer
        )


        add(
            "robot",
            answer
        )


#        speak(answer)
    def send_esp32(self, command):

        try:

            result = send_command(command)

            self.add_message(
                ROBOT_NAME,
                "ESP32: " + result
            )


        except Exception as e:

            self.add_message(
                ROBOT_NAME,
                "خطای برد: " + str(e)
            )




    def owner_login(self, password):

        if login(password):

            self.add_message(
                ROBOT_NAME,
                "حالت صاحب فعال شد 🔓"
            )

        else:

            self.add_message(
                ROBOT_NAME,
                "رمز اشتباه است ❌"
            )




    def owner_logout(self):

        logout()

        self.add_message(
            ROBOT_NAME,
            "حالت صاحب خاموش شد."
        )





class TobiApp(App):


    def build(self):

        app = RobotUI()


        app.add_message(
            ROBOT_NAME,
            "سلام امیر، من آماده‌ام 🤖"
        )


        return app




if __name__ == "__main__":

    TobiApp().run()
