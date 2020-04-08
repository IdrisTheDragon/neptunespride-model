class Star:
    def __init__(self,c:float=None,e:int=None,uid:int=None,i:int=None,s:int=None,n:str=None,puid:int=None,r:int=None,ga:int=None,v:str=None,y:str=None,x:str=None,nr:int=None,st:int=None):
        self.c = c
        self.e = e
        self.uid = uid
        self.i = i
        self.s = s
        self.n = n
        self.puid = puid
        self.r = r
        self.ga = ga
        self.v = v
        self.y = y
        self.x = x
        self.nr = nr
        self.st = st

    def json_parse(self,json:dict):
        if 'c' in json.keys():
            self.c = json['c']
        if 'e' in json.keys():
            self.e = json['e']
        if 'uid' in json.keys():
            self.uid = json['uid']
        if 'i' in json.keys():
            self.i = json['i']
        if 's' in json.keys():
            self.s = json['s']
        if 'n' in json.keys():
            self.n = json['n']
        if 'puid' in json.keys():
            self.puid = json['puid']
        if 'r' in json.keys():
            self.r = json['r']
        if 'ga' in json.keys():
            self.ga = json['ga']
        if 'v' in json.keys():
            self.v = json['v']
        if 'y' in json.keys():
            self.y = json['y']
        if 'x' in json.keys():
            self.x = json['x']
        if 'nr' in json.keys():
            self.nr = json['nr']
        if 'st' in json.keys():
            self.st = json['st']

    def __str__(self):
        out = 'Star:{'
        out = out + 'c:{0},'.format(self.c)
        out = out + 'e:{0},'.format(self.e)
        out = out + 'uid:{0},'.format(self.uid)
        out = out + 'i:{0},'.format(self.i)
        out = out + 's:{0},'.format(self.s)
        out = out + 'n:{0},'.format(self.n)
        out = out + 'puid:{0},'.format(self.puid)
        out = out + 'r:{0},'.format(self.r)
        out = out + 'ga:{0},'.format(self.ga)
        out = out + 'v:{0},'.format(self.v)
        out = out + 'y:{0},'.format(self.y)
        out = out + 'x:{0},'.format(self.x)
        out = out + 'nr:{0},'.format(self.nr)
        out = out + 'st:{0},'.format(self.st)
        out = out + '}\n'
        return out

    def __repr__(self):
        return self.__str__()


