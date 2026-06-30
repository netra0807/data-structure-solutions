# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 04:44:28 2026

@author: netra
"""

class TollPlaza:
    def __init__(self):
        self.capacity=5
        self.queue=[None]*self.capacity
        self.front=-1
        self.rear=-1
    def enqueue(self,vehicle):
        if(self.rear+1)%self.capacity==self.front:
            return "Toll Plaza Full! Vehicle must wait."
        if self.front==-1:
            self.front=0
        self.rear=(self.rear+1)%self.capacity
        self.queue[self.rear]=vehicle
        return f"Vehicle '{vehicle}'entered the toll lane."
    def dequeue(self):
        if self.front==-1:
            return "No vehicle in the toll lane!"
        removed_vehicle=self.queue[self.front]
        self.queue[self.front]=None
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.front=(self.front+1)%self.capacity
        return f"Vehicle '{removed_vehicle}' cleared the toll."

toll=TollPlaza()
print(toll.enqueue("Car A"))
print(toll.enqueue("Car B"))
print(toll.dequeue())
print(toll.enqueue("Car C"))
