class Research:
    def __init__(self,value:int=None,level:int=None):
        self.value = value
        self.level = level

    def json_parse(self,json:dict):
        if 'value' in json.keys():
            self.value = json['value']
        if 'level' in json.keys():
            self.level = json['level']

    def __str__(self):
        out = 'Research:{'
        out = out + 'value:{0},'.format(self.value)
        out = out + 'level:{0},'.format(self.level)
        out = out + '}\n'
        return out

    def __repr__(self):
        return self.__str__()


