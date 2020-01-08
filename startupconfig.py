from configparser import ConfigParser
from kivy.config import Config

# Default window size and position, also used to set minimum window size
window_width = 300
window_height = 200
window_top = 100
window_left = 100

# Use Python lib configparser to read .ini file prior to app startup
parser = ConfigParser()
found = parser.read('windowsize.ini')  # created in main.py: build_config()
if found:
    Config.set('graphics', 'width', parser['Window']['width'])
    Config.set('graphics', 'height', parser['Window']['height'])
    Config.set('graphics', 'position', 'custom')
    Config.set('graphics', 'top', parser['Window']['top'])  # find top and left
    Config.set('graphics', 'left', parser['Window']['left'])
else:
    Config.set('graphics', 'width', window_width)  # default value match default values in main.py: build_config, on_start
    Config.set('graphics', 'height', window_height)
    Config.set('graphics', 'position', 'custom')
    Config.set('graphics', 'top', window_top)
    Config.set('graphics', 'left', window_left)
Config.set('kivy', 'exit_on_escape', 0)  # Turn off exit on escape
Config.set('input', 'mouse', 'mouse,disable_multitouch') # turn off multi-touch emulation, req for mouse right click
