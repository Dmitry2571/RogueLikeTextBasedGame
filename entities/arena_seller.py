#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 16:28:08 2025

@author: dmitrykhramov
"""

from entities.NPC import NPC
from core.data_manager import DataManager
import logging 
from items.inventory import Inventory
from items.weapons import Weapon
#from items.item import Item
#import random

class ArenaSeller(NPC):
    
    def __init__(self, name, location, sex, buy_multiplier=1.0, sell_multiplier=1.0):
        super().__init__(name, 2000, 1000, location, "human", sex)
        self._prices = DataManager().load_item_prices()
        self._item_types = DataManager.get_item_types()
        self._stock_config = DataManager.get_seller_stock(name)
        self._stock = {}
        self._name_to_id = {}
        self.inventory = Inventory(999)
        self._buy_multiplier = buy_multiplier
        self._sell_multiplier = sell_multiplier
        self._load_stock()        
        
    def greetings(self):
        if self.relationship < 15:
            print(f'{self.name} looks at you sternly from behind the counter,'\
                  '"What do you need, fresh blood? Speak or rot."')
                
    def describe_shop(self):
        print("You scan the shop — junk scattered everywhere. By the counter "\
              "hangs a board listing current prices for whatever’s for sale.\n Actual price:")
        try:
            for item, item_info in self._stock.items():
                print(f"You can buy {self._stock[item]['name']} for {self._stock[item]['buy_price']} "\
                      f"coins and sell for {self._stock[item]['sell_price']}. "\
                      f"There are {self._stock[item]['in_stock']} items in stock.")
             
        except Exception as e:
            logging.error(e)
            print("But today it seems empty and the store doesn't sell anything.")
    
    def _load_stock(self):
        # загружаем товары из JSON
        item = None
        for item_data in self._stock_config["fixed_items"]:
            if item_data['id'] in self._item_types:
                item_info = self._item_types[item_data["id"]]
                item_type = item_info["type"]
                
                if item_type == "Weapon":
                    item = Weapon(item_data["name"])
        
                self.inventory.add_item(item, item_data["count"])
                self._stock[item_data['id']] = {
                    'name': self._item_types[item_data['id']]['name'],
                    'sell_price': int(self._prices[item_data['id']]['sell_price'] * self._sell_multiplier),
                    'buy_price': int(self._prices[item_data["id"]]['buy_price'] * self._buy_multiplier),
                    'in_stock': item_data["count"]
                    }
                self._name_to_id[item_info['name'].lower()] = item_data['id']
        logging.info(f'STOCK INFO: {self._stock}.')
            
        #random_choices = random.sample(
        #    self.stock_config["random_pool"],
        #    self.stock_config["random_slots"]
        #)
        #for item_data in random_choices:
        #    item = Item(item_data["name"], stack_size=item_data["count"])
        #    self.inventory.add_item(item, item_data["count"])
        
    def buy(self, player):
        print("What do you want? Don’t keep me waiting, weakling.")
        choice = input("I want ")
        #logging.info(f"Item_types: {self._item_types}.")
        #item_id = self._item_types.get(choice["id"], "error")
        #logging.info(f"Item id: {item_id}.")
        #if item_id == "error":
        #    return
        logging.info(f"Choice: {choice}.\nStock: {self._stock}.\nName-ID: {self._name_to_id}.")
        choice_item_id = self._name_to_id[choice.lower()]
        if choice_item_id in self._stock:
            logging.info("BUY SECTION")
            #print("Yeah? How many? Don’t keep me waiting.")
            #try:
            #    choice_count = int(input("I need "))
            #except Exception:
           #     print("go away, don't waste my time.")
           #     return
           # if choice_count <= self._stock[choice]['in_stock']:
               
            player.buy(self.inventory.remove_return_item(choice, 1), self._stock[choice_item_id]['buy_price'], 1)    
    
    def sell(self, player):
        print("What do you want? Don’t keep me waiting, weakling.")
        choice = input("I want ")
        #logging.info(f"Item_types: {self._item_types}.")
        #item_id = self._item_types.get(choice["id"], "error")
        #logging.info(f"Item id: {item_id}.")
        #if item_id == "error":
        #    return
        logging.info(f"Choice: {choice}.\nStock: {self._stock}.\nName-ID: {self._name_to_id}.")
        choice_item_id = self._name_to_id[choice.lower()]
        if choice_item_id in self._stock:
            logging.info("SELL SECTION")
            #print("Yeah? How many? Don’t keep me waiting.")
            #try:
            #    choice_count = int(input("I need "))
            #except Exception:
           #     print("go away, don't waste my time.")
           #     return
           # if choice_count <= self._stock[choice]['in_stock']:
               
            self.inventory.add_item(player.sell(choice, self._stock[choice_item_id]['sell_price'], 1),1)
            
                
                