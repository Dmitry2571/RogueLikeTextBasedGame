#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 11:57:43 2025

@author: dmitrykhramov
"""
from entities.enemy import Enemy
from entities.arena_seller import ArenaSeller
from locations.location import Location
import logging
 
class SlumsArena(Location):
    """
    Класс определяющий арену в трущобах. Самая примитивная арена.
    В ней есть сама арена для боев, магазин и больше ничего.
    """
    def __init__(self, name):
        super().__init__(name)
        self.Tarn = ArenaSeller("Tarn", self.name, "male", buy_multiplier=2, sell_multiplier=0.5)
        
    #Определение локальных команд с точки входа в локацию            
    def _handle_local_command(self, choice: str) -> bool:
        if super()._handle_local_command(choice):
            return True
        
        if choice in {'challenge', 'attack', 'fight', 'duel'}:
            self.enter_arena()
        elif choice in {'go to shop', 'shop'}:
            self.shop()
        elif choice in {'leave', 'leave arena', 'exit', 'go to exit'}:
            self.player.move('SlumsOfUlayim')
            self.player = None
            return True
        else:
            print("Try again, loser.")
        return False
    
    #Вход в боевую зону, где игрок может выбрать противника
    def enter_arena(self):
        print('You enter the arena. You can see a lot of blood around', end='')
        if self.player.lvl < 15:
            print(', sending shivers down your spine.')
        else:
            print(', but that only makes you more excited.') 
        print("You wander the arena and spot all kinds of bloodthirsty fighters — "\
              "weaklings, equals, and monsters way outta your league. "\
              "\nYou can leave or pick a fighter to challenge. What do you choose?")
        choice = input("'fight'... unless you're backing out like a "\
                       "dog with its tail between its legs — then go. ")
        if choice.lower() == 'fight':
            if self.player.lvl < 15:
                print("You look around warily at the guys near the wall, even weaklings terrify you.")
            else:
                print("You look down on the crowd near the walls, "\
                      "even the fighters who look stronger don't scare you a bit.")
            self.choose_enemy()
            
        else:
            print("Scram, you whelp!\n")
                
    #Первый квест игры - победа в бою, в случае провала - вылет из игры
    def quest_first_battle_arena(self, player):
        self.player = player
        self.player.move(self.name)
        print('You enter the arena. You can see a lot of blood around, sending'\
              ' shivers down your spine.\nYou wander the arena and spot all '\
              'kinds of bloodthirsty fighters — weaklings, equals, and monsters'\
              ' way outta your league.\nYou can leave or pick a fighter to challenge. What do you choose?')
        choice = input("'fight'... unless you're backing out like a "\
                       "dog with its tail between its legs — then go. ").lower()
        if choice != 'fight':
            print("Scram, you whelp!\n")
            self._fail_first_quest_if_active()
            return
            
        print("You look around warily at the guys near the wall, even weaklings terrify you.")
        choice_enemy = input("Who's gonna bleed? A weakling, your equal, or a monster? ").lower()
        if choice_enemy in {"weak", "weakling", "weaker"}:
            enemy = Enemy(diff="easy", p_lvl = self.player.lvl)
        elif choice_enemy == "equal":
            enemy = Enemy(diff="normal", p_lvl = self.player.lvl)
        elif choice_enemy in {"stronger", "monster", "strongest"}:
            print('The fighters look at you with mockery, but at the same time '\
                  'with respect. They push forward a fighter who matches your strength.')
            enemy = Enemy(diff="normal", p_lvl = self.player.lvl)
        else:
            print("You were afraid to make a choice and ran away.")
            self._fail_first_quest_if_active()
            return
        self._start_battle_message()
        self.player.start_quest_battle(enemy)    
        if self.player.is_alive and "100" not in self.player.failed_quests:
            self.player.complete_quest("100")
        else:
            self._fail_first_quest_if_active()
            self.player.move("End")
            self.player = None
            
    def _fail_first_quest_if_active(self):
        if "100" in self.player.in_progress_quests:
            self.player.fail_quest("100")
    
    #выбор противника по 3-м уровням: слабак, равный, сильный
    def choose_enemy(self):
        choice_enemy = input("Who's gonna bleed? A weakling, your equal, or a monster? ").lower()
        if choice_enemy in {"weak", "weakling", "weaker"}:
            enemy = Enemy(diff="easy", p_lvl = self.player.lvl)
        elif choice_enemy == "equal":
            enemy = Enemy(diff="normal", p_lvl = self.player.lvl)
        elif choice_enemy in {"stronger", "monster", "strongest"}:
            enemy = Enemy(diff="hard", p_lvl = self.player.lvl)
        else:
            print("You were afraid to make a choice and ran away.")
            return
        logging.info(f"Enemy created. Enemy stats: {enemy.stat}.")
        self._start_battle_message()
        self.player.combat(enemy)
    
    #Вывод сообщение о начале боя на арене
    def _start_battle_message(self):
        print("The blood rushes to your temples, your heart drums in your ears. "\
              "You grip your weapon, assume a fighting stance — ready to "\
              "fight to the death.\nThe enemy takes position. A gong sounds, "\
              "signaling the start of a bloody battle.\nBefore you know it, you "\
              "notice how the enemy is already rushing at you.")
        
    #Базовый магазин. Купи-продай, поболтай и вали.    
    def shop(self):
        print("You step into a grimy hole-in-the-wall shop tucked beneath the arena.")
        self.Tarn.greetings()
        while True:        
            choice = input("Well, I...")
            if self.player.handle_global_command(choice):
                if self.player.is_exit:
                    break
                continue
            if choice in {"want to buy", "buy", "purchase"}:
                self.Tarn.buy(self.player)
            elif choice in {"want to sell", "sell", "pawn"}:
                self.Tarn.sell(self.player)
            elif choice in {"look around", "just look", "browse", "see items"}:
                self.Tarn.describe_shop()
            elif choice in {"nothing"}:
                print("You're standing there like an idiot and looking at the seller.")
            else:
                print("You left the store in silence.")
                break
            print('"Did you need anything else, fresh blood?')
        print(self.description)
        
    