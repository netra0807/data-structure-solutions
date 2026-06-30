# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 05:01:22 2026

@author: netra
"""

class GPSNavigation:
    def __init__(self):
        self.current_place=None
        self.history_stack=[]
        self.forward_stack=[]
    def visit(self,place):
        if self.current_place is not None:
            self.history_stack.append(self.current_place)
        self.current_place=place
        self.forward_stack.clear()
        return f"Arrived at:{self.current_place}"
    def back(self):
        if not self.history_stack:
            return "Cannot go back,You are at the starting checkpoint."
        self.forward_stack.append(self.current_place)
        self.current_place=self.history_stack.pop()
        return f"returned back to:{self.current_place}"
    def forward(self):
        if not self.forward_stack:
            return "Cannot go forward ! No forward history available."
        self.history_stack.append(self.current_place)
        self.current_place=self.forward_stack.pop()
        return f"Moved forward to:{self.current_place}"
g=GPSNavigation()
print(g.visit("checkpoint1"))
print(g.visit("checkpoint2"))
print(g.back())
print(g.forward())