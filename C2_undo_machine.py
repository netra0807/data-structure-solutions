# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 03:16:15 2026

@author: netra
"""

#2
class TextEditor:
    def __init__(self):
        self.stack=[]
    def type(self,char:str):
        self.stack.append(char)
    def undo(self):
        if self.stack:
            self.stack.pop()
    def getText(self)->str:
        return "".join(self.stack)
editor=TextEditor()
editor.type('H')
editor.type('i')
editor.type('!')
print(editor.getText())
editor.undo()
print(editor.getText())
