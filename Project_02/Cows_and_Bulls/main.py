"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Radek Jíša
email: radek.jisa@gmail.com
"""

import random
import time

from game_functions import introduction, get_user_input, evaluate_guess, get_plurals, calculate_time, highscore, credits

Divider = '-' * 80


def play_game(divider: str):
    '''main game loop'''

    print(introduction(divider))
    
    generated_number = list(str(random.randint(1000,9999)))
    attempts = 0
    start_time = None
    
    while True:
        print(f'\n{'Enter the number:'.center(80)}')
        user_number = get_user_input()
        
        if attempts == 0:
            start_time = time.time()
        
        bulls, cows = evaluate_guess(generated_number, user_number)
        bulls_word, cows_word = get_plurals(bulls, cows)
    
        print(f'{bulls_word.capitalize()} {bulls:^34} {cows:^35} {cows_word.capitalize()}')
        attempts += 1
        
        if bulls == 4:
            end_time = time.time()
            break

    mins, secs, score = calculate_time(start_time, end_time)
    high_score = highscore(score)
    print(credits(divider, mins, secs, high_score))


if __name__ == "__main__":
    play_game(Divider)