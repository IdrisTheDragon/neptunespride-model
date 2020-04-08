import typing

from model.tech import Tech


class Player:
    def __init__(self,total_industry:int=None,regard:int=None,total_science:int=None,uid:int=None,ai:int=None,huid:int=None,total_stars:int=None,total_fleets:int=None,total_strength:int=None,alias:str=None,tech:Tech=None,avatar:int=None,conceded:int=None,ready:int=None,total_economy:int=None,missed_turns:int=None,karma_to_give:int=None,researching:str=None,War:typing.Dict[str,int]=None,stars_abandoned:int=None,cash:int=None,researching_next:str=None,Countdown_to_war:typing.Dict[str,int]=None):
        self.total_industry = total_industry
        self.regard = regard
        self.total_science = total_science
        self.uid = uid
        self.ai = ai
        self.huid = huid
        self.total_stars = total_stars
        self.total_fleets = total_fleets
        self.total_strength = total_strength
        self.alias = alias
        self.tech = tech
        self.avatar = avatar
        self.conceded = conceded
        self.ready = ready
        self.total_economy = total_economy
        self.missed_turns = missed_turns
        self.karma_to_give = karma_to_give
        self.researching = researching
        self.War = War
        self.stars_abandoned = stars_abandoned
        self.cash = cash
        self.researching_next = researching_next
        self.Countdown_to_war = Countdown_to_war

    def json_parse(self,json:dict):
        if 'total_industry' in json.keys():
            self.total_industry = json['total_industry']
        if 'regard' in json.keys():
            self.regard = json['regard']
        if 'total_science' in json.keys():
            self.total_science = json['total_science']
        if 'uid' in json.keys():
            self.uid = json['uid']
        if 'ai' in json.keys():
            self.ai = json['ai']
        if 'huid' in json.keys():
            self.huid = json['huid']
        if 'total_stars' in json.keys():
            self.total_stars = json['total_stars']
        if 'total_fleets' in json.keys():
            self.total_fleets = json['total_fleets']
        if 'total_strength' in json.keys():
            self.total_strength = json['total_strength']
        if 'alias' in json.keys():
            self.alias = json['alias']
        if 'tech' in json.keys():
            a = Tech()
            a.json_parse(json['tech'])
            self.tech = a
        if 'avatar' in json.keys():
            self.avatar = json['avatar']
        if 'conceded' in json.keys():
            self.conceded = json['conceded']
        if 'ready' in json.keys():
            self.ready = json['ready']
        if 'total_economy' in json.keys():
            self.total_economy = json['total_economy']
        if 'missed_turns' in json.keys():
            self.missed_turns = json['missed_turns']
        if 'karma_to_give' in json.keys():
            self.karma_to_give = json['karma_to_give']
        if 'researching' in json.keys():
            self.researching = json['researching']
        if 'war' in json.keys():
            self.war = json['war']
        if 'stars_abandoned' in json.keys():
            self.stars_abandoned = json['stars_abandoned']
        if 'cash' in json.keys():
            self.cash = json['cash']
        if 'researching_next' in json.keys():
            self.researching_next = json['researching_next']
        if 'countdown_to_war' in json.keys():
            self.countdown_to_war = json['countdown_to_war']

    def __str__(self):
        out = 'Player:{'
        out = out + 'total_industry:{0},'.format(self.total_industry)
        out = out + 'regard:{0},'.format(self.regard)
        out = out + 'total_science:{0},'.format(self.total_science)
        out = out + 'uid:{0},'.format(self.uid)
        out = out + 'ai:{0},'.format(self.ai)
        out = out + 'huid:{0},'.format(self.huid)
        out = out + 'total_stars:{0},'.format(self.total_stars)
        out = out + 'total_fleets:{0},'.format(self.total_fleets)
        out = out + 'total_strength:{0},'.format(self.total_strength)
        out = out + 'alias:{0},'.format(self.alias)
        out = out + 'tech:{0},'.format(self.tech)
        out = out + 'avatar:{0},'.format(self.avatar)
        out = out + 'conceded:{0},'.format(self.conceded)
        out = out + 'ready:{0},'.format(self.ready)
        out = out + 'total_economy:{0},'.format(self.total_economy)
        out = out + 'missed_turns:{0},'.format(self.missed_turns)
        out = out + 'karma_to_give:{0},'.format(self.karma_to_give)
        out = out + 'researching:{0},'.format(self.researching)
        out = out + 'War:{0},'.format(self.War)
        out = out + 'stars_abandoned:{0},'.format(self.stars_abandoned)
        out = out + 'cash:{0},'.format(self.cash)
        out = out + 'researching_next:{0},'.format(self.researching_next)
        out = out + 'Countdown_to_war:{0},'.format(self.Countdown_to_war)
        out = out + '}\n'
        return out

    def __repr__(self):
        return self.__str__()


