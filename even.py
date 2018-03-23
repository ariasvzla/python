#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:08:38 2018

@author: elian
"""

def check_is_even(num):
        if num%2 == 0:
            print("The number is even")
        else:
            print("The number is not even")
            return;
def check_is_div_4(num):
    if num%4==0:
        print("Number is multiply by 4")
    else:
        print("And the number is NOT divide by 4")
        return;

def check_div(num,check):
    if num%check == 0:
        print("Number is divide evenly by", check)
    else: 
        print("number is NOT evenly divide by", check)
        return;
        
num=int(input("Enter a number: "))
check_is_even(num)
check_is_div_4(num)
ans=input("Would you like to check if the number is divide by a specific number?: ").lower()

while True:
    if ans=="yes":
        check=int(input("Enter a divisor: "))
        check_div(num,check)
        break
    elif ans == "no":
        print("Thank you, see you later")
        break
    else: 
        print("Please enter yes or no") 
        ans=input("Would you like to check if the number is divide by a specific number?: ").lower()
    



