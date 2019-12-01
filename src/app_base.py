import kivy
import os
from kivy.app import App
from kivy.uix.button import Button

# set required version of KIVY
kivy.require('1.11.1')
# environ to play audio
os.environ["KIVY_AUDIO"] = "ffpyplayer"



class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pushButton = Button(text='Hello world')

    def build(self):
        return self.pushButton


if __name__ == '__main__':
    MyApp().run()
