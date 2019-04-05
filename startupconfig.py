from configparser import ConfigParser
from kivy.config import Config

# print('Setting Config values prior to start')
parser = ConfigParser()
found = parser.read('windowsize.ini')  # created in main.py,
if found:
    # print('Setting size and postion')
    Config.set('graphics', 'width', parser['Window']['width'])
    Config.set('graphics', 'height', parser['Window']['height'])
    Config.set('graphics', 'top', parser['Window']['top'])
    Config.set('graphics', 'left', parser['Window']['left'])