#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 17:40:43 2025

@author: dmitrykhramov
"""

class Achievements:
    
    def __init__(self):
        self.achievements = {"Laughed Out of the Arena": False,
                             "Dead End": False,
                             "Plumber's Dream": False
            }
        self.describe_achievements = {"Laughed Out of the Arena": "Pathetic display. "\
                    "They kicked you out before you could embarrass yourself more.",
                    "Dead End": "Game over. You are dead, fool.",
                    "Plumber's Dream": "Go save some ‘royal’ drunk from the sewer."
            }
        self.completed_achievements = 0
        self.total_achievements = len(self.achievements.keys())
        
    def update_achievements(self, title):
        if title in self.achievements and not self.achievements[title]:
            print(f"You've reached the '{title}' achievement. {self.describe_achievements[title]}")
            self.achievements[title] = True
            self.completed_achievements += 1
            print(f"You've got {self.completed_achievements} of {self.total_achievements} achievements, loser!")