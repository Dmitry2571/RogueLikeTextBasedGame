#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 10:17:11 2025

@author: dmitrykhramov
"""

import json
import logging

class DataManager:
    quest_type_selection= {
        "main": [100, 499],
        "side": [500, 999],
        "other": [1000, 9999]}
    item_types = None
    seller_stock = None
    
    @staticmethod 
    def load_json(path: str):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    
    @staticmethod
    def load_quest(quest_type):
        quests = {k:v for k,v in DataManager.load_json("progress/quests_data.json").items()\
                  if DataManager.quest_type_selection[quest_type][0] <= int(k) <= DataManager.quest_type_selection[quest_type][1]}
        return quests
    
    @staticmethod 
    def load_location_description():
        desc = {k:v for k,v in DataManager.load_json("locations/location_data.json").items()}
        return desc
    
    @staticmethod 
    def load_item_prices():
        prices = DataManager.load_json("items/items_base_prices.json")["items"]
        return prices
    
    @classmethod
    def load_item_types(cls):
        if cls.item_types is None:
            cls.item_types = cls.load_json("items/item_types.json")
        logging.info(f"ITEM TYPES: {cls.item_types}")

    @classmethod
    def load_seller_stock(cls):
        if cls.seller_stock is None:
            cls.seller_stock = cls.load_json("items/seller_stock.json")
        logging.info(f"SELLER STOCK: {cls.seller_stock}")
    
    @classmethod
    def get_item_types(cls):
        if cls.item_types is None:
            cls.item_types = cls.load_json("items/item_types.json")
        return cls.item_types
    
    @classmethod
    def get_seller_stock(cls, name:str):
        if cls.seller_stock is None:
            cls.seller_stock = cls.load_json("items/seller_stock.json")
        return cls.seller_stock[name]