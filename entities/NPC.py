#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 11:51:44 2025

@author: dmitrykhramov
"""

STATUS = {
    "alive": True,
    "unknown": True,
    "dead": False}

class NPC:
    def __init__(self, name: str, hp: int, money: int, location: str, race: str, sex:str, relationship = 0): 
        self.hp = hp
        self.name = name
        self._status = "alive"
        self._money = money
        self._sex = sex
        self._race = race
        self._location = location  
        self._player_relationship = relationship
        
    def give_exp_to(self, player):
        pass
    
    @property
    def status(self):
        return STATUS[self._status]
    
    @property 
    def relationship(self):
        return self._player_relationship

