# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 00:56:02 2022

@author: sweta
"""
import random
def choose():
    words = ['entertainment', 'enterprise', 'solution', 'labbour', 'stereotype', 'donkey', 'dianosourous', 'depth', 'sources', 'natures', 'naptune']
    pick = random.choice(words)
    return pick

def jumble(word):
    question ="".join(random.sample(word,len(word)))
    return question

def thank(pl1, pl2, p1, p2):
    print(pl1, ' point is:', p1)
    print(pl2, ' point is:', p2)
    print("well played! \n Thank you for playing this game\n")
       

           
play()