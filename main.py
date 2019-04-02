""" A test for how Windows are sized to evaluate Windows, Mac and Linux"""
from kivy.config import Config
print('Setting Config values prior to start')
Config.set('graphics', 'width', 800)
Config.set('graphics', 'height', 400)

# Config.set must be run prior to the app starting, or will have no effect

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.metrics import dp
from kivy.core.window import Window


class SizeInput(BoxLayout):
    name = StringProperty()
    action = ObjectProperty()

class SizeIt(BoxLayout):

    def config_set(self, w, h):
        print(f'Using Config.set with width:{w} and height:{h}')
        Config.set('graphics', 'width', int(w))
        Config.set('graphics', 'height', int(h))

    def wsize(self, w, h):
        print(f'Using Window.size with width:{w} and height:{h}')
        Window.size = (int(w), int(h))

    def config_set_dp(self, w, h):
        dpw = int(dp(w))
        dph = int(dp(h))
        print(f'Using Config.set dp() with width:{dpw} and height:{dph}')
        Config.set('graphics', 'width', int(dpw))
        Config.set('graphics', 'height', int(dph))

    def wsize_dp(self, w, h):
        dpw = int(dp(w))
        dph = int(dp(h))
        print(f'Using Window.size dp with dp(width):{dpw} and dp(height):{dph}')
        Window.size = (dpw, dph)


class WindowSizeApp(App):
    pass


if __name__ == '__main__':
    WindowSizeApp().run()