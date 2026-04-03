#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 11:51:30 2025

@author: dmitrykhramov
"""
from random import randint
import logging

mult_hp = 4
mult_dmg = 2
base_hp = {"easy": 25,
           "normal": 100,
           "hard": 200,
           "boss": 1000}
base_dmg = {"easy": 5,
           "normal": 10,
           "hard": 20,
           "boss": 40}
class Enemy:
    def __init__(self, diff, p_lvl):
        self._difficulty = diff
        self._alive = True
        self.stat = {
            "strength": 1,      # сила
            "dexterity": 1,     # ловкость
            "intelligence": 1,  # интеллект
            "stamina": 1,       # выносливость
            "luck": 1 
            }
        if p_lvl > 5:
            self._level = p_lvl - randint(4, p_lvl)
            self._max_hp = self._hp = base_hp[self._difficulty] + self._level * mult_hp
            self._damage = base_dmg[self._difficulty] + self._level * mult_dmg
            for key in self.stat.keys():
                self.stat[key] = randint(self._level-3, self._level + 3)
        else:
            self._level = 1
            self._max_hp = self._hp = base_hp[self._difficulty]
            self._damage = base_dmg[self._difficulty]
            for key in self.stat.keys():
                self.stat[key] = randint(0, self._level)
            
    def take_damage(self, dmg):
        self._hp -= dmg
        if self._hp <= 0:
            self._alive = False
            
    def _calculate_damage(self):
        return self._damage
    
    def is_alive(self):
        return self._alive
    
    def choose_fight_action(self, player, status="unknown"):
        enemy_choice = randint(1, 4)
        logging.info(f"Enemy choose: {enemy_choice}.")
        if enemy_choice == 1:
            if status != 'dodge':
                if status != 'block':
                    player.take_damage(self._calculate_damage())
                else:
                    print('You blocked it — but not fully. Still hurts, doesn’t it, loser.')
                    player.take_damage(int(self._calculate_damage() / 2))
            else:
                print("You dodged? Don’t let it go to your head. You’re still trash, loser.")
        elif enemy_choice == 2:
            if status != 'dodge':
                if status != 'block':
                    player.take_damage(self._calculate_damage()*1.25)
                else:
                    print('You blocked it — but not fully. Still hurts, doesn’t it, loser.')
                    player.take_damage(int(int(self._calculate_damage() / 2)/2))
            else:
                print("You dodged? Don’t let it go to your head. You’re still trash, loser.")
        else:
            print("Enemy decided raise a shield.")

    def get_state_arena(self):
        if self._max_hp / 2 < self._hp:
            return "Enemy looks still to active for someone who must be killed."
        elif self._max_hp / 3 < self._hp:
            return "You can see fresh blood on enemy's body, but hey, enemy is still standing."
        elif self._max_hp / 4 < self._hp:
            return "You can see that it's hard for your enemy to hold his weapon"\
                "but your enemy still thinks that he can beat you."
        else:
            return "Your enemy fall down in front of you. You still hear gulp sounds from the ground,"\
                " but it's nothing more then the last breathe of dead body."
            
    def give_exp_to(self, player):
        if self._difficulty not in base_hp.keys():
            logging.error(f"ERROR in enemy.give_exp_to: unknown difficulty '{self._difficulty}'")
            return
        if self._difficulty == 'easy':
            player.gain_exp(2)
        elif self._difficulty == 'normal':
            player.gain_exp(5)
        elif self._difficulty == 'hard':
            player.gain_exp(10)
        elif self._difficulty == 'boss':
            player.gain_exp(25)
            
            
    @property 
    def difficulty(self):
        return self._difficulty
            
            