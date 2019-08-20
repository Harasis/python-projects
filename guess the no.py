# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:04:05 2019

@author: user
"""

import random

no = random.randrange(1,50)

win = "False"

play_agn = "y"

while play_agn == "Y" or play_agn == "y":
    rem = 6
    
    while rem>0:
        guess = int(input("your guess is -"))
        rem = rem - 1
        if guess>no:
            print("Input is too high. You have", rem , "chances left")
        
        elif guess<no:
            print("Input is too low. You have", rem , "chances left")
    
        else:
            print("you guessed it correct")
            win = "True"
            rem = 0
            
    if win == "False":
        print("you loose. the correct no is" , no)
    
    play_agn = input("\nplay again? (y/n)")
    
        