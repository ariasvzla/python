#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 19:11:34 2018

@author: elian
"""
num=50
iteractions=0
lower_edge=1
upper_edge=100
mid= (upper_edge+lower_edge)//2 
print("is your number "+str(num)+" ?")
while True:
    ans=input("Enter H for guess too HiGH, Enter L for guess too low and C if is correct: ").lower()
    iteractions+=1
   
    if ans=="l":
        lower_edge= mid+1
        mid= (upper_edge+lower_edge)//2  
        print("is your number "+str(mid)+" ? ")
    elif ans=="h":
        upper_edge=mid -1
        mid = (upper_edge+ lower_edge)//2
        print("is your number "+str(mid)+" ?")
    elif ans== "c":
        print("I guessed")
        print("Numer of iteraction:"+ str(iteractions))
        break
      
        
        
        
    
