#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 11:40:09 2025

@author: dmitrykhramov
"""
from entities.player import Player
from locations.slums_arena import SlumsArena
from locations.slums_of_ulayim import SlumsOfUlayim
from core.data_manager import DataManager 
import logging

game_info = {
    'name': 'Unnamed',
    'version': "0.0.3c",
    'status': 'in progress',
    'version_name': 'Arena Shop Sell System'
    }

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# Вывод в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# Вывод в файл
file_handler = logging.FileHandler('game.log')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

slumsArena = SlumsArena("SlumsArena_South_Ulayim")
slums = SlumsOfUlayim("SlumsOfUlayim")
locations = {'SlumsArena_South_Ulayim': slumsArena,
             'SlumsOfUlayim': slums
    }

DataManager.load_seller_stock()

def main(is_new_game = True):

    if is_new_game:
        print("Name yourself, you little piece of filth.")
        name = input("Enter your name: ")
        if name == '':
            print("Couldn't even think of a name? Pathetic. Fine — I'll name you myself.")
            name = "Maggot"
        player = Player(name)
        print(f"{name}, huh? Well, let’s see how long you can drag this miserable life of yours."\
              " Your story — if you can call it that — begins in the arena.\n\n\n")
        locations['SlumsArena_South_Ulayim'].quest_first_battle_arena(player)
    else:
        player = Player.load_game()
    while True:
        if player.is_exit or player.location == "End":
            break
        try:
            locations[player.location].enter_location(player)
        except Exception as e:
            logging.error(f"{e}")
            print("Oh, poor baby — too tired to even lift a finger.")
            break
    print("Too tired to play, huh? Wuss.")
    return

def start():
    DataManager.load_item_types()
    while True:
        print("Welcome to the HELL\nDo you want to start?\n"\
              "1. Hell yeah!\n2. Load your pathetic save\n3. No... Mommy, help me!")
        choice = input("What will you choose? ").lower()
        if choice in {'1', 'hell yeah!', 'hell yeah','play', 'new game'}:
            main(True)
        elif choice in {'2', 'load game', 'load', 'load your pathetic save', 'load save'}:
            main(False)
        else:
            print("Go cry to mommy, baby.")
            break

start()

