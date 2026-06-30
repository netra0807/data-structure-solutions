# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 03:16:28 2026

@author: netra
"""

from collections import deque

class Printer:
    def __init__(self):
        self.urgent_queue=deque()
        self.normal_queue=deque()
    def add_job(self,document_name:str,is_urgent:bool):
        if is_urgent:
            self.urgent_queue.append(document_name)
        else:
            self.normal_queue.append(document_name)
    def print_next_job(self)->str:
        if self.urgent_queue:
            return f"Printing Urgent:{self.urgent_queue.popleft()}"
        if self.normal_queue:
            return f"Printing Normal:{self.normal_queue.popleft()}"
        return "No printing jobs in queue"
p=Printer()
p.add_job("Report.pdf", is_urgent=True)
p.add_job("product.pdf", is_urgent=False)
p.add_job("Invoice.pdf", is_urgent=False)
p.add_job("Emergency.pdf", is_urgent=True)
print(p.print_next_job())
print(p.print_next_job())

