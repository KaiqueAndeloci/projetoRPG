from os.path import dirname, realpath, isfile
from json import dump

class JsonManager():
    def __init__(self):
        self.path = dirname(realpath(__file__))# + "/"
    
    def create_json():
        data = {}