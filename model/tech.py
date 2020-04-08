import typing

from model.scanning import Scanning
from model.propulsion import Propulsion
from model.terraforming import Terraforming
from model.research import Research
from model.weapons import Weapons
from model.banking import Banking
from model.manufacturing import Manufacturing


class Tech:
    def __init__(self,scanning:Scanning=None,propulsion:Propulsion=None,terraforming:Terraforming=None,research:Research=None,weapons:Weapons=None,banking:Banking=None,manufacturing:Manufacturing=None):
        self.scanning = scanning
        self.propulsion = propulsion
        self.terraforming = terraforming
        self.research = research
        self.weapons = weapons
        self.banking = banking
        self.manufacturing = manufacturing

    def json_parse(self,json:dict):
        if 'scanning' in json.keys():
            a = Scanning()
            a.json_parse(json['scanning'])
            self.scanning = a
        if 'propulsion' in json.keys():
            a = Propulsion()
            a.json_parse(json['propulsion'])
            self.propulsion = a
        if 'terraforming' in json.keys():
            a = Terraforming()
            a.json_parse(json['terraforming'])
            self.terraforming = a
        if 'research' in json.keys():
            a = Research()
            a.json_parse(json['research'])
            self.research = a
        if 'weapons' in json.keys():
            a = Weapons()
            a.json_parse(json['weapons'])
            self.weapons = a
        if 'banking' in json.keys():
            a = Banking()
            a.json_parse(json['banking'])
            self.banking = a
        if 'manufacturing' in json.keys():
            a = Manufacturing()
            a.json_parse(json['manufacturing'])
            self.manufacturing = a

    def __str__(self):
        out = 'Tech:{'
        out = out + 'scanning:{0},'.format(self.scanning)
        out = out + 'propulsion:{0},'.format(self.propulsion)
        out = out + 'terraforming:{0},'.format(self.terraforming)
        out = out + 'research:{0},'.format(self.research)
        out = out + 'weapons:{0},'.format(self.weapons)
        out = out + 'banking:{0},'.format(self.banking)
        out = out + 'manufacturing:{0},'.format(self.manufacturing)
        out = out + '}\n'
        return out

    def __repr__(self):
        return self.__str__()


