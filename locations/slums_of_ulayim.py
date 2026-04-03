#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 16:17:52 2025

@author: dmitrykhramov
"""

from locations.location import Location

class SlumsOfUlayim (Location):
    
    def __init__(self, name):
        super().__init__(name)
            
    #Определение локальных команд с точки входа в локацию            
    def _handle_local_command(self, choice: str) -> bool:
        if choice in {'arena', 'go to arena', 'go arena'}:
            self.player.move('SlumsArena_South_Ulayim')
            self.player = None
            return True
        elif choice in {'desperate street', 'go to desperate street'}:
            self.player.move('Desperate_Street')
            self.player = None
            return True
        else:
            print("Try again, loser.")
        return False
    
    def flop(self):
        print("describe flop. rent a room or leave")
        
    def spoon(self):
        print("describe tavern. buy a food, sell food.")
        
    
        
        