from configparser import ConfigParser
from kivy.config import Config

# Use Python lib configparser to read .ini file prior to app startup
parser = ConfigParser()
found = parser.read('windowsize.ini')  # created in main.py: build_config()
if found:
    Config.set('graphics', 'width', parser['Window']['width'])
    Config.set('graphics', 'height', parser['Window']['height'])
    Config.set('graphics', 'position', 'custom')
    Config.set('graphics', 'top', parser['Window']['top']) # find top and left
    Config.set('graphics', 'left', parser['Window']['left'])
else:
    Config.set('graphics', 'width', 300) # default value match default values in main.py: build_config, on_start
    Config.set('graphics', 'height', 200)
    Config.set('graphics', 'position', 'custom')
    Config.set('graphics', 'top', 40)
    Config.set('graphics', 'left', 40)