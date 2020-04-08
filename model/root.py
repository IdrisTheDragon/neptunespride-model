import typing

from model.scanning_data import Scanning_data


class Root:
    def __init__(self,scanning_data:Scanning_data=None):
        self.scanning_data = scanning_data

    def json_parse(self,json:dict):
        if 'scanning_data' in json.keys():
            a = Scanning_data()
            a.json_parse(json['scanning_data'])
            self.scanning_data = a

    def __str__(self):
        out = 'Root:{'
        out = out + 'scanning_data:{0},'.format(self.scanning_data)
        out = out + '}\n'
        return out

    def __repr__(self):
        return self.__str__()


