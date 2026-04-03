#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 22:16:00 2025

@author: dmitrykhramov
"""

from items.item import Item

class Weapon (Item):
    weapon_dmg = {"Rusty Blade": 10
        }
    
    def __init__(self, weaponName):
        super().__init__("weapon", 1, weaponName)
        self._dmg = Weapon.weapon_dmg[self._name]
        
    @property 
    def damage(self):
        return self._dmg