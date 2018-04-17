#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 19:11:34 2018

@author: elian
"""


class QuestionAndAnswer():
    
    num = None
    iteractions = 0
    lower_edge = 1
    upper_edge = 100
    mid = (upper_edge+lower_edge)//2
    
    
    def __init__(self,numVal = 70):
        self.num=numVal

    def handle_answer(self, inStr):
        print ("User typed : %s" % (inStr,) )
        print (self.mid)
        print (self.num)

    
    def handle_Input(self):
        ans = str(input("Enter H for guess too HiGH, Enter L for guess too low and C if is correct: ")).lower()
        
        return ans
        
    def handle_interactions(self):
        self.iteractions += 1
        
        return self.iteractions
        

    
    def askAnswer(self):
    
        
        running = True
        while running:
            ans = self.handle_Input()
            
            if ans == "l":
                self.lower_edge = self.mid+1
                self.mid = (self.upper_edge+self.lower_edge)//2
                print("is your number "+str(self.mid)+" ? ")
                self.handle_interactions()
                
            elif ans == "h":
                self.upper_edge=self.mid - 1
                self.mid = (self.upper_edge + self.lower_edge)//2
                print("is your number "+str(self.mid)+" ?")
                
                self.handle_interactions()
                
                
            elif ans== "c":
                print("I guessed")
                print("Numer of iteraction:"+ str(self.iteractions))
                running = False
                
        
        print ("Thank you, Exiting")
        input("Good Bye")
        #exit(0)
            
userCheck = QuestionAndAnswer()

userCheck.askAnswer()
    
