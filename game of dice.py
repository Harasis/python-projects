# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:54:52 2019

@author: user
"""

import random
import time

roll_agn = "Y"

while roll_agn == "Y" or roll_agn == "y":
    print("\nRolling the Dice--")
    time.sleep(3)
    
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    print("The Number Is--:")
    
    print("Dice 1=", dice1, "\nDice 2=", dice2)
    
    if dice1 == dice2:
        print("YOU WON !")
    else:
        print("KEEP TRYING!")

    roll_agn = input("\nDo u want to roll again? (y/n)")        
        