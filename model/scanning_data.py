import typing

from model.fleet import Fleet
from model.star import Star
from model.player import Player


class Scanning_data:
    def __init__(self,fleets:typing.Dict[str,Fleet]=None,fleet_speed:float=None,paused:int=None,productions:int=None,tick_fragment:float=None,now:int=None,tick_rate:int=None,production_rate:int=None,stars:typing.Dict[str,Star]=None,stars_for_victory:int=None,game_over:int=None,started:int=None,start_time:int=None,total_stars:int=None,production_counter:int=None,trade_scanned:int=None,tick:int=None,trade_cost:int=None,name:str=None,player_uid:int=None,admin:int=None,turn_based:int=None,war:int=None,players:typing.Dict[str,Player]=None,turn_based_time_out:int=None):
        self.fleets = fleets
        self.fleet_speed = fleet_speed
        self.paused = paused
        self.productions = productions
        self.tick_fragment = tick_fragment
        self.now = now
        self.tick_rate = tick_rate
        self.production_rate = production_rate
        self.stars = stars
        self.stars_for_victory = stars_for_victory
        self.game_over = game_over
        self.started = started
        self.start_time = start_time
        self.total_stars = total_stars
        self.production_counter = production_counter
        self.trade_scanned = trade_scanned
        self.tick = tick
        self.trade_cost = trade_cost
        self.name = name
        self.player_uid = player_uid
        self.admin = admin
        self.turn_based = turn_based
        self.war = war
        self.players = players
        self.turn_based_time_out = turn_based_time_out

    def json_parse(self,json:dict):
        if 'fleets' in json.keys():
            self.fleets = {}
            for x,y in json['fleets'].items():
                a = Fleet()
                a.json_parse(y)
                self.fleets[x] = a
        if 'fleet_speed' in json.keys():
            self.fleet_speed = json['fleet_speed']
        if 'paused' in json.keys():
            self.paused = json['paused']
        if 'productions' in json.keys():
            self.productions = json['productions']
        if 'tick_fragment' in json.keys():
            self.tick_fragment = json['tick_fragment']
        if 'now' in json.keys():
            self.now = json['now']
        if 'tick_rate' in json.keys():
            self.tick_rate = json['tick_rate']
        if 'production_rate' in json.keys():
            self.production_rate = json['production_rate']
        if 'stars' in json.keys():
            self.stars = {}
            for x,y in json['stars'].items():
                a = Star()
                a.json_parse(y)
                self.stars[x] = a
        if 'stars_for_victory' in json.keys():
            self.stars_for_victory = json['stars_for_victory']
        if 'game_over' in json.keys():
            self.game_over = json['game_over']
        if 'started' in json.keys():
            self.started = json['started']
        if 'start_time' in json.keys():
            self.start_time = json['start_time']
        if 'total_stars' in json.keys():
            self.total_stars = json['total_stars']
        if 'production_counter' in json.keys():
            self.production_counter = json['production_counter']
        if 'trade_scanned' in json.keys():
            self.trade_scanned = json['trade_scanned']
        if 'tick' in json.keys():
            self.tick = json['tick']
        if 'trade_cost' in json.keys():
            self.trade_cost = json['trade_cost']
        if 'name' in json.keys():
            self.name = json['name']
        if 'player_uid' in json.keys():
            self.player_uid = json['player_uid']
        if 'admin' in json.keys():
            self.admin = json['admin']
        if 'turn_based' in json.keys():
            self.turn_based = json['turn_based']
        if 'war' in json.keys():
            self.war = json['war']
        if 'players' in json.keys():
            self.players = {}
            for x,y in json['players'].items():
                a = Player()
                a.json_parse(y)
                self.players[x] = a
        if 'turn_based_time_out' in json.keys():
            self.turn_based_time_out = json['turn_based_time_out']

    def __str__(self):
        out = 'Scanning_data:{'
        out = out + 'fleets:{0},'.format(self.fleets)
        out = out + 'fleet_speed:{0},'.format(self.fleet_speed)
        out = out + 'paused:{0},'.format(self.paused)
        out = out + 'productions:{0},'.format(self.productions)
        out = out + 'tick_fragment:{0},'.format(self.tick_fragment)
        out = out + 'now:{0},'.format(self.now)
        out = out + 'tick_rate:{0},'.format(self.tick_rate)
        out = out + 'production_rate:{0},'.format(self.production_rate)
        out = out + 'stars:{0},'.format(self.stars)
        out = out + 'stars_for_victory:{0},'.format(self.stars_for_victory)
        out = out + 'game_over:{0},'.format(self.game_over)
        out = out + 'started:{0},'.format(self.started)
        out = out + 'start_time:{0},'.format(self.start_time)
        out = out + 'total_stars:{0},'.format(self.total_stars)
        out = out + 'production_counter:{0},'.format(self.production_counter)
        out = out + 'trade_scanned:{0},'.format(self.trade_scanned)
        out = out + 'tick:{0},'.format(self.tick)
        out = out + 'trade_cost:{0},'.format(self.trade_cost)
        out = out + 'name:{0},'.format(self.name)
        out = out + 'player_uid:{0},'.format(self.player_uid)
        out = out + 'admin:{0},'.format(self.admin)
        out = out + 'turn_based:{0},'.format(self.turn_based)
        out = out + 'war:{0},'.format(self.war)
        out = out + 'players:{0},'.format(self.players)
        out = out + 'turn_based_time_out:{0},'.format(self.turn_based_time_out)
        out = out + '}\n'
        return out

    def __repr__(self):
        return self.__str__()


