import sys

import requests, random
import pandas as pd
import time

data = pd.read_csv("pokemon name and type.csv")
print("Guess the Pokemon Game")
time.sleep(0.5)
print("Press 'Q' for quit")

user_input = input("Enter 'S' for start else type 'Q' for quit: ")
score = 0

if user_input == 'Q':
    sys.exit()
elif user_input == 'S':
    game_should_continue = True
    while game_should_continue:
        random_pokemon = data.loc[random.randint(0, 1045)]
        pokemon_name = random_pokemon['name']
        pokemon_type = random_pokemon['type']
        user_answer = input(f"Enter the pokemon type of the {pokemon_name}: ")
        if user_answer == pokemon_type:
            score += 1
            print(f"Your answer is correct and your overall score is {score}")
        else:
            game_should_continue = False
            print("Your answer is mistake")
            print(f"Your overall score is {score}")







