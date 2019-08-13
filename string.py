# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 00:05:29 2019

@author: OCEAN
"""

import random
movies = ['tarzan','jumangi','titanic','matrix','robot','simbaa','kedarnath','andhadhun']
film  = list(random.choice(movies))
guess = []
for i in range(len(film)):
    guess.append('_')
for i in guess:
    print(i,end=" ")
while '_' in guess :
    alpha = input("Guess an alphabet")
    while alpha in film:
        index = film.index(alpha)
        print(index)
        film[index]=' '
        guess[index]=alpha
    for i in guess:
        print(i,end=" ")

print("\nYou have successfully guessed the film")