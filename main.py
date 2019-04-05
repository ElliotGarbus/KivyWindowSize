""" A test for how Windows are sized to evaluate Windows, Mac and Linux"""

import startupconfig  # runs Config.set prior to loading kivy.app
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.metrics import dp
from kivy.core.window import Window


class SizeInput(BoxLayout):
    name = StringProperty()
    action = ObjectProperty()


class SizeIt(BoxLayout):
    def wsize(self, w, h):
        print(f'Using Window.size with width:{w} and height:{h}')
        Window.size = (int(w), int(h))

    def wsize_dp(self, w, h):
        dpw = int(dp(w))
        dph = int(dp(h))
        print(f'Using Window.size dp with dp(width):{dpw} and dp(height):{dph}')
        Window.size = (dpw, dph)


class WindowSizeApp(App):
    win_top = NumericProperty()
    win_left = NumericProperty()
    win_width = NumericProperty()
    win_height = NumericProperty()

    def build_config(self, config):
        config.setdefaults('Window', {'width': 300, 'height': 200, 'top': 40, 'left': 40})

    def window_resize(self, win, w, h):
        print('Window was resized')
        self.win_width, self.win_height = Window.size
        self.win_top = Window.top
        self.win_left = Window.left
        print(f'resize: Window.size: {Window.size}')
        print(f'resize: Window.top: {Window.top}, Window.left: {Window.left}')

    def window_request_close(self, win):
        print('Window close requested')
        config = self.config
        config.set('Window', 'width', Window.size[0])
        config.set('Window', 'height', Window.size[1])
        config.set('Window', 'top', Window.top)
        config.set('Window', 'left', Window.left)
        print(f'close: Window.size: {Window.size}')
        print(f'close: Window.top: {Window.top}, Window.left: {Window.left}')
        return False

    def window_event(self, win):
        # on_draw is called when ever the window is redrawn, display size and pos
        self.win_width, self.win_height = Window.size
        self.win_top = Window.top
        self.win_left = Window.left

    def build(self):
        self.title = 'Window Size and Position Test'
        Window.minimum_height = 160
        Window.minimum_width = 300
        Window.bind(on_request_close=self.window_request_close)
        Window.bind(on_draw=self.window_event)

    def on_start(self):
        # Set Window to previous size and position
        config = self.config
        width = config.getdefault('Window', 'width', 300)
        height = config.getdefault('Window', 'height', 200)
        Window.size = (int(width), int(height))
        Window.top = int(config.getdefault('Window', 'top', 40))
        Window.left = int(config.getdefault('Window', 'left', 40))

        print(f'on_start(): Window.size: {Window.size}')
        print(f'on_start(): Window.top: {Window.top}, Window.left: {Window.left}')

    def on_stop(self):
        # Save Current Window Size and Position
        config = self.config
        # Window position NOT valid in on_stop
        print(f'on_stop(): Window.size: {Window.size}')
        print(f'on_stop(): Window.top: {Window.top}, Window.left: {Window.left}')
        config.write()


WindowSizeApp().run()