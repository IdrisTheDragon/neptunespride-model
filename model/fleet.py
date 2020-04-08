class Fleet:
    def __init__(self,uid:int=None,l:int=None,o:list=None,n:str=None,puid:int=None,w:int=None,y:str=None,x:str=None,st:int=None,lx:str=None,ly:str=None):
        self.uid = uid
        self.l = l
        self.o = o
        self.n = n
        self.puid = puid
        self.w = w
        self.y = y
        self.x = x
        self.st = st
        self.lx = lx
        self.ly = ly

    def json_parse(self,json:dict):
        if 'uid' in json.keys():
            self.uid = json['uid']
        if 'l' in json.keys():
            self.l = json['l']
        if 'o' in json.keys():
            self.o = json['o']
        if 'n' in json.keys():
            self.n = json['n']
        if 'puid' in json.keys():
            self.puid = json['puid']
        if 'w' in json.keys():
            self.w = json['w']
        if 'y' in json.keys():
            self.y = json['y']
        if 'x' in json.keys():
            self.x = json['x']
        if 'st' in json.keys():
            self.st = json['st']
        if 'lx' in json.keys():
            self.lx = json['lx']
        if 'ly' in json.keys():
            self.ly = json['ly']

    def __str__(self):
        out = 'Fleet:{'
        out = out + 'uid:{0},'.format(self.uid)
        out = out + 'l:{0},'.format(self.l)
        out = out + 'o:{0},'.format(self.o)
        out = out + 'n:{0},'.format(self.n)
        out = out + 'puid:{0},'.format(self.puid)
        out = out + 'w:{0},'.format(self.w)
        out = out + 'y:{0},'.format(self.y)
        out = out + 'x:{0},'.format(self.x)
        out = out + 'st:{0},'.format(self.st)
        out = out + 'lx:{0},'.format(self.lx)
        out = out + 'ly:{0},'.format(self.ly)
        out = out + '}\n'
        return out

    def __repr__(self):
        return self.__str__()


