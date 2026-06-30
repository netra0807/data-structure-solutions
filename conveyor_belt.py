# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 04:33:27 2026

@author: netra
"""

class Convey:
    def __init__(self):
        self.belt=[None]*8
    def check_slot(self,slot_id):
        if 0<=slot_id<8:
            return self.belt[slot_id]
        return "Invalid slot Number!!"
    def find_product(self,product_name):
        for i in range(8):
            if self.belt[i]==product_name:
                return f"Product '{product_name}' found at slot {i}."
        return f"Product '{product_name}' not found on the belt."
    def update_slot(self,slot_id,product_name):
        if 0<=slot_id<8:
            self.belt[slot_id]=product_name
            return f"Slot '{slot_id}' updated to '{product_name}'."
        return "Invalid slot Number!!"
    def is_full(self):
        return None not in self.belt
        
b=Convey()
print(b.update_slot(2, "clothes"))
print(b.check_slot(2))
print(b.find_product("clothes"))
print(b.is_full())