#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 13:47:46 2025

@author: dmitrykhramov
"""

from items.item import Item
import logging

class Inventory:
    
    def __init__(self, max_slots=10):
        self._items = {}  # {'item_id': count}
        self._max_slots = max_slots
        self._item_index = {} 

    def add_item(self, item: Item, count=1):
        logging.info(f"Adding {count} of {item.name}.")

        if count <= 0:
            return

        remaining = count

        # 1. Заполняем существующие стаки
        if item.stackable:

            for item_id, data in self._items.items():
                current_item = data["item"]

                if current_item.name != item.name:
                    continue

                current_count = data["count"]

                free_space = (
                    current_item.max_stack_size
                    - current_count
                )

                if free_space <= 0:
                    continue

                add_count = min(free_space, remaining)

                self._items[item_id]["count"] += add_count
                remaining -= add_count

                logging.info(
                    f"Added {add_count} to slot {item_id}. "
                    f"Remaining: {remaining}"
                )

                if remaining == 0:
                    print(
                        f"You shoved your {item.name} into your bag. "
                        f"Good job, hoarder."
                    )

                    # альтернатива:
                    # print(
                    #     f"More {item.name}? Sure, why not. "
                    #     f"Stuffed it in."
                    # )

                    return

        # 2. Создаём новые слоты
        while remaining > 0:

            if len(self._items) >= self._max_slots:
                print(
                    "Pathetic. Your pockets are stuffed "
                    "like a beggar’s. Can’t carry more junk, loser."
                )

                logging.info(
                    f"Inventory full. "
                    f"Could not add {remaining} of {item.name}."
                )

                return

            item_id = self.find_next_id()

            if item.stackable:
                add_count = min(
                    item.max_stack_size,
                    remaining
                )
            else:
                add_count = 1

            self._items[item_id] = {
                "item": item,
                "count": add_count
            }

            if item.name in self._item_index:
                self._item_index[item.name].append(item_id)
            else:
                self._item_index[item.name] = [item_id]

            remaining -= add_count

            logging.info(
                f"Added {add_count} of {item.name} "
                f"to slot {item_id}. "
                f"Remaining: {remaining}"
            )

        print(
            f"You shoved your {item.name} into your bag. "
            f"Good job, hoarder."
        )

        # альтернатива:
        # print(
        #     f"More {item.name}? Sure, why not. "
        #     f"Stuffed it in."
        # )

    def find_next_id(self):
        for i in range(1, self._max_slots + 1):
            if i not in self._items:
                return i
        return None

    def remove_item(self, item:Item, count=1):
        # уменьшение или удаление
        pass
    
    def find_id(self, item_name):
        logging.info(f"Item name = {item_name}.")
        logging.info(f"Item index = {self._item_index}.")
        logging.info(f"{item_name in self._item_index}")
        if item_name in self._item_index:
            logging.info(f"Item index: {self._item_index[item_name][-1]}.")
            return self._item_index[item_name][-1]
        return -1
    
    def remove_id(self, item_id):
        if item_id in self._items:
            item_name = self._items[item_id]['item'].name
            self._item_index[item_name].pop()
            del self._items[item_id]
    
    def remove_return_item(self, item_name:str, count=1):
        # уменьшение или удаление
        logging.info("REMOVE RETURN SECTION.")
        item_id = self.find_id(item_name)
        logging.info(f"Item id: {item_id}.")
        if item_id == -1:
            print(f"You can't find {item_name}.")
            return
        else:
            count_item = self._items[item_id]['count']
            logging.info(f"Count item: {count_item}.")
            item = self._items[item_id]['item']
            logging.info(f"Item : {item}.")
            if count_item == count:
                self.remove_id(item_id)
                logging.info(f"Removed {item.name} from inventory.")
            return item
                

    def get_item_count(self, item_id):
        pass
        #return self._items.get(item_id, 0)

    def show_items(self):
        logging.info(f"Items: {self._items}.")
        for i in self._items.keys():
            print(f"Slot {i}: Item: {self._items[i]['item'].name}, count: {self._items[i]['count']}.")