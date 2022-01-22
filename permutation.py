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

def jumble(word):       #function to jumble the word
    question ="".join(random.sample(word,len(word)))
    return question

def thank(pl1, pl2, p1, p2):   #function to print the points of player
    print(pl1, ' point is:', p1)           
    print(pl2, ' point is:', p2)
    print("well played! \n Thank you for playing this game\n")
       
def play():               #function to print name of player and ask to guess the correct word
    player1 =input("player1, enter your name\n")
    player2 =input("player2, enter your name\n")
    pp1 = 0
    pp2 = 0
    value = 0
    while(1):
         pick_value =choose()
         qu = jumble(pick_value)
         print("Guess the correct word\n")
         print(qu)
         if value%2 == 0:
             print(player1, "your turn\n")
             ans = input('what is in my mind\n')
             if ans==pick_value:
                 pp1= pp1+1
                 print('your score is:', pp1)
             else:
                 print('better luck next time \n the ans is', pick_value)
             c= int(input('want to play more? enter 0 for no and 1 for yes'))
             #c=int(c)
             if c==0:
                thank(player1, player2, pp1, pp2)
                break
         else:
            print(player2, "your turn")
            ans = input('what is in my mind\n')
            if ans==pick_value:
                pp2= pp2+1
                print('your score is:', pp2)
            else:
                print('better luck next time \n the ans is', pick_value)
            c= int(input('want to play more?'))
            #ac=int(c)
            if c==0:
                thank(player1, player2, pp1, pp2)
                break
         value = value+1
           
play()