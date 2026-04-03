#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 16:31:17 2025

@author: dmitrykhramov
"""

from core.data_manager import DataManager 

class Location:
    
    _descriptions_cache = None
    
    def __init__(self, name):
        self.name = name
        self.player = None
        self.description = self._load_description()
        
    def enter_location(self, player):
        self.player = player
        print(self.description)
        
        while True:
            choice = input("You decide ")
            if self.player.handle_global_command(choice):
                if self.player.is_exit:
                    break
                continue
            
            if self._handle_local_command(choice):
                break
            
            
    def _handle_local_command(self, choice: str) -> bool:
        print("Try again, loser.")
        return False
        
     
    def _load_description(self) -> str:
        if Location._descriptions_cache is None:
            Location._descriptions_cache = DataManager.load_location_description()
        
        loc_data = Location._descriptions_cache.get(self.name)
        if loc_data is None:
            return f"[MISSING DESCRIPTION FOR: {self.name}]"
        return loc_data.get("description", "[NO DESCRIPTION FIELD]")