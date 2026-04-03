#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 14:07:42 2025

@author: dmitrykhramov
"""

class Item:
    
    def __init__(self, item_type:str, stack_size:int, name:str):
        self._item_type = item_type
        self._max_stack_size = stack_size
        self._name = name
        
    @property 
    def name(self):
        return self._name
    
    @property 
    def stackable(self):
        return True if self._max_stack_size > 1 else False
    
    @property 
    def max_stack_size(self):
        return self._max_stack_size