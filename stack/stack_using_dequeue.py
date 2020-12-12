# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 10:27:33 2020

@author: Kirty
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DeQueue:
    def __init__(self):
        self.head = None
       