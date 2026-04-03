#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 09:24:53 2025

@author: dmitrykhramov
"""
from core.data_manager import DataManager
import logging

class Quest:
    QUEST_STATES = {
        "locked",      # недоступен
        "available",   # доступен, но не начат
        "active",      # в процессе
        "completed",   # завершён
        "failed"       # провален
        }
    
    def __init__(self):
        self._main_quests = self.load_quest("main")
        self._side_quests = self.load_quest("side")
        self._other_quests = self.load_quest("other")
        self._all_quests = {}
        self._all_quests.update(self._main_quests)
        self._all_quests.update(self._side_quests)
        self._all_quests.update(self._other_quests)
        self._quests_states = {}
        self._quests_names = {}
        for quest_id, data in self._all_quests.items():
            self._quests_states[quest_id] = data.get("initial_state", "locked")
            self._quests_names[quest_id] = data.get("name")
            
    def load_quest(self, quest_type: str):
        return DataManager.load_quest(quest_type)
    
    def mark_completed(self, quest_id, player):
        self._quests_states[quest_id] = "completed"
        quest_name = self._quests_names[quest_id]
        player.gain_exp(int(self._all_quests[quest_id]['exp']))
        print(f"Oh, congrats. You managed to complete the “{quest_name}” quest — but you’re still a loser.")
        
    def mark_failed(self, quest_id):
        self._quests_states[quest_id] = "failed"
        quest_name = self._quests_names[quest_id]
        print(f"Oh, congrats. You managed to FAIL the “{quest_name}” quest — you’re even more a loser than I thought.")
        
    def get_failed_quests(self):
        pass        
    
    