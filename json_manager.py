from os import path
from os.path import dirname, realpath, isfile
from json import dump, load


class jsonManager():
    def __init__(self):
        self.path = dirname(realpath(__file__)) + "/"
    
    def create_json(self, file, dicionario):
        data = dicionario
        path_data_json = self.path + file

        if not isfile(path_data_json):
            with open(path_data_json, 'w') as f:
                dump(data, f, indent = 4, separators = (',', ':'))
            return True
        else:
            return False

    def update(self, file, dicionario):
        pass
    def read(self, file):
        self.arquivo = self.path + file
        print(self.arquivo)
        if isfile(self.arquivo):
            with open(self.path + file) as f:
                data = load(f)
            return data
        else:
            return False

"""if __name__ == '__main__':
    jmaneger = jsonManager()
    dic = {
        
    }
    print(jmaneger.read("teste.json"))"""
