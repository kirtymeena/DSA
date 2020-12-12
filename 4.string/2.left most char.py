# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:53:12 2020

@author: Kirty
"""

char = 256
def leftMostChar(s):
    
    res = -1
    visited = [-1]*char
    
    for i in range(len(s)-1,-1,-1):
        if visited[ord(s[i])]==-1:
            visited[ord(s[i])] = i
        else:
            res = i
    return visited
    print(visited)
        
print(leftMostChar(s))
# time complexity=O(n)
# aux space - O(1)