#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 11:40:48 2025

@author: dmitrykhramov
"""
from entities.enemy import Enemy
from items.weapons import Weapon
from items.item import Item
from items.inventory import Inventory
from progress.achievements import Achievements
from random import randint
from progress.quests import Quest
import logging

class Player:
    GLOBAL_COMMANDS = {"inventory", "inv", "save", "load", "exit", "exit game"}
    def __init__(self, name):
        self._name = name
        self._hp = 100
        self._exp = 0
        self._gold = 100
        self._base_damage = 2
        self._base_defense = 1
        self._weapon = Weapon("Rusty Blade")        
        self._lvl = 1
        self._available_points = 0
        self._stats = {
            "strength": 1,      # сила
            "dexterity": 1,     # ловкость
            "intelligence": 1,  # интеллект
            "stamina": 1,       # выносливость
            "luck": 1           # удача
        }
        self._alive = True
        self._current_location = "Main"
        self._achievements = Achievements()
        self._quest = Quest()
        self._exit = False
        self.completed_quests = set()
        self.failed_quests = set()
        self.in_progress_quests = {"100"}
        self._inventory = Inventory()
        self._inventory.add_item(self._weapon, 1)
        if self._name == "Mario":
            self._achievements.update_achievements("Plumber's Dream")
    
    def move(self, area):
        self._current_location = area
        logging.info(f"Player change location. New location: {area}")
        
    def handle_global_command(self, command)-> bool:
        if command not in Player.GLOBAL_COMMANDS:
            return False
        
        
        if command in {"inventory", "inv"}:
            self._inventory.show_items()
            return True
        elif command == "exit game":
            self._exit = True
            return True
        return False
        
    def start_quest_battle(self, enemy: Enemy):
        if enemy.difficulty == "easy":
            print("You’re still clumsy as hell — but look! Your opponent’s just as bad. "\
                  "Dodging? Blocking? No way. ")
            choice = input("All you’re thinking is: go for a strong blow or a lunge? ").lower()
            if choice in ["dodge", "dodging"]:
                print("You try to dodge way too early — and tumble flat on your face. "\
                      "While you’re lying there like a whipped dog, "\
                      "your opponent stumbles over their own feet and "\
                      "crashes to the ground. The crowd erupts in laughter, "\
                      "jeering for you both to get the hell out "\
                      "and stop disgracing the name of arena fighters.")
                self._achievements.update_achievements("Laughed Out of the Arena")
                return
            elif choice in ["block", "blocking"]:
                print("You drop into a defensive stance, breathing hard, "\
                      "waiting for the attack — but the enemy trips over "\
                      "nothing and faceplants right in front of you. "\
                      "The other fighters watching burst out laughing at "\
                      "your pathetic guard, shouting for you both to get off "\
                      "the arena floor and stop disgracing what real fighters stand for.")
                self._achievements.update_achievements("Laughed Out of the Arena")
                return
            elif choice in ["lunge", "thrust", "stab"]:
                print("You tighten your grip on the blade and lunge at the rushing enemy."\
                      "This fool’s as green as you, and twice as clumsy."\
                      "The enemy stumbles, and your blade sinks deep even before "\
                      "the body completes the fall.")
            elif choice in ["strong blow", "blow", "hard blow"]:
                print("Gripping your blade, you take a wide swing and put all "\
                      "your strength into the blow. Unfortunately, you hit with "\
                      "the spine of the blade — but even that sent the enemy "\
                      "crashing down, screaming in pain.")
        else:
            print("You’re still clumsy as hell — but look! Your opponent’s just as bad. "\
                  "However, your instincts tell you to be cautious. "\
                  "You might need to block or dodge their attacks.")
            choice = input("All you’re thinking is: go for a strong blow or a lunge? Or maybe you should block or dodge? ").lower()
            if choice in ["dodge", "dodging"]:
                print("You hesitate for a moment — and suddenly your opponent is charging, "\
                      "blade raised. You barely hit the ground, rolling awkwardly. "\
                      "Getting up, you quickly assess the situation.")
            elif choice in ["block", "blocking"]:
                print("You lose precious seconds — and now your opponent looms over you, "\
                      "swinging wide. All you manage is raising your blade to block — "\
                      "and somehow, you survive.")
            elif choice in ["lunge", "thrust", "stab"]:
                print("You tighten your grip on the blade and lunge at the rushing enemy."\
                      "This fool’s as green as you, and twice as clumsy."\
                      "The enemy stumbles, and your blade sinks deep even before "\
                      "the body completes the fall.")
            elif choice in ["strong blow", "blow", "hard blow"]:
                print("Gripping your blade, you take a wide swing and put all "\
                      "your strength into the blow. Unfortunately, you hit with "\
                      "the spine of the blade — but even that sent the enemy "\
                      "crashing down, screaming in pain.")
        
        self.combat(enemy)
        if self._alive == False:
            return
        print("You stare down at the bloody corpse. There is nothing else to do.")
        del enemy
        print("The arena fighters still smirk at you — but since you’ve "\
              "passed the trial and won your fight (even if it was against "\
              "a pathetic weakling), no one will stop you from leaving the arena now.")
        return

            
    def combat(self, enemy):
        while enemy.is_alive():
            battle_status = "unknown"
            choice = input("You look at enemy and decide to ").lower()
            if choice in {"dodge", "dodging"}:
                    print("You try to dodge way too early — and tumble flat on your face. "\
                          "While you’re lying there like a whipped dog, "\
                          "your opponent stumbles over their own feet and "\
                          "crashes to the ground. The crowd erupts in laughter, "\
                          "jeering for you both to get the hell out "\
                          "and stop disgracing the name of arena fighters.")
                    battle_status = "dodge" 
            elif choice in {"block", "blocking"}:
                    print("You drop into a defensive stance, breathing hard, "\
                          "waiting for the attack — but the enemy trips over "\
                          "nothing and faceplants right in front of you. "\
                          "The other fighters watching burst out laughing at "\
                          "your pathetic guard, shouting for you both to get off "\
                          "the arena floor and stop disgracing what real fighters stand for.")
                    battle_status = "block"
            elif choice in {"lunge", "thrust", "stab"}:
                print("You tighten your grip on the blade and lunge at the rushing enemy."\
                      "This fool’s as green as you, and twice as clumsy."\
                      "The enemy stumbles, and your blade sinks deep even before "\
                      "the body completes the fall.")
                battle_status = "lunge"
                enemy.take_damage(self.damage)
                logging.info(f"Damage {self.damage}")
            elif choice in {"strong blow", "blow", "hard blow"}:
                print("Gripping your blade, you take a wide swing and put all "\
                      "your strength into the blow. Unfortunately, you hit with "\
                      "the spine of the blade — but even that sent the enemy "\
                      "crashing down, screaming in pain.")
                battle_status = "blow"
                enemy.take_damage(self.damage * 1.25)
                logging.info(f"Damage {self.damage * 1.25}")
            else:
                print("You froze. Couldn’t think of a damn thing.")
                
            print(enemy.get_state_arena())
            if enemy.is_alive() == False:
                enemy.give_exp_to(self)
                return
            if (battle_status == 'dodge' and self._stats["dexterity"] <= enemy.stat["dexterity"]) or\
            (battle_status == 'block' and self._stats["strength"] < enemy.stat["strength"]):
                battle_status = "unknown"
                logging.info("Failed to block or dodge.")
            enemy.choose_fight_action(self, battle_status)
            if self._alive == False:
                return
     
    def take_damage(self, dmg):
        self._hp -= dmg
        if self._hp <= 0:
            self._alive = False
            self.dead_end()
            
    def dead_end(self):
        print("You fall on the ground breatheless. You are fresh meat for rat."\
              "Now, you won't be able to breathe because you are dead, fool.")
        self._achievements.update_achievements("Dead End")
    
    def complete_quest(self, quest_id:str):
        self._quest.mark_completed(quest_id, self)
        self.in_progress_quests.remove(quest_id)
        self.completed_quests.add(quest_id)
        
    def fail_quest(self,quest_id:str):
        self._quest.mark_failed(quest_id)
        self.in_progress_quests.remove(quest_id)
        self.failed_quests.add(quest_id)
    
    def exp_needed_for_level(self, lvl:int) -> int:
        if lvl <= 10:
            return int(100 * (1.5 ** (lvl - 1)))
        else:
            return int(50 * (lvl ** 2))
    
    def _check_level_up(self):
        while self._exp >= self.exp_needed_for_level(self._lvl + 1):
            self.level_up()
            self._base_damage += 2 * self._lvl
            
    def level_up(self):
        self._lvl += 1
        self._available_points = 3
        
    def update_stats(self, stat_name):
        if stat_name in self._stats.keys() and self._available_points > 0:
            self._available_points -= 1
            self._stats[stat_name] += 1
            
    def gain_exp(self, amount):
        self._exp += amount
        logging.info(f'Current exp: {self._exp}.')
        
    def buy(self, item:Item, price, count=1):
        self._inventory.add_item(item, count)
        self._gold -= price
        logging.info(f"Current balance: {self._gold} coins.")
        
    def sell(self, item_name:str, price, count=1):
        item = self._inventory.remove_return_item(item_name, 1)
        self._gold += price
        logging.info(f"Current balance: {self._gold} coins.")
        logging.info(f"Current item: {item}.")
        return item
    
    @classmethod
    def load_game(cls):
        return cls
    
    @property 
    def damage(self):
        return self._base_damage + self._weapon.damage\
            + self._stats['strength'] * randint(0, self._base_damage)
    
    @property 
    def lvl(self):
        return self._lvl
    
    @property 
    def location(self):
        return self._current_location
    
    @property 
    def is_alive(self):
        return self._alive
    
    @property 
    def is_exit(self):
        return self._exit
    
    @property 
    def gold(self):
        return self._gold
    