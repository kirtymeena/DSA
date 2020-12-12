# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:38:56 2020

@author: Kirty
"""
def display_hash(HashTable):
    for i in range(len(HashTable)):
        print(i,end=" ")
        
        for j in HashTable[i]:
            print("-->", end = " ")
            
            print(j, end = " ")
        print()
        
bucket = 10   #size of the hashtable called bucket
HashTable = [[] for _ in range(bucket)]

def Hashing(key):
    return key % len(HashTable)

def insert(HashTable,key,value):
    hash_key = Hashing(key)
    HashTable[hash_key].append(value)

def remove(HashTable,key,value):
    k = Hashing(key)
    HashTable[k].remove(value)
    
    
insert(HashTable,10,'delhi')
insert(HashTable,9,'Mumbai')
insert(HashTable,20,'Rajasthan')

remove(HashTable,10,'Rajasthan')
display_hash(HashTable)
      
"""
- channing is a method to avaiod collision
- channing uses linked list(list as a hash table) to store keys

load factor = n/m

m= no. of slots in hash table
n = no.of keys to be inserted 

expected chain length = load factor 

search = O(1+load factor)

insert = O(1+load factor)

""" 
