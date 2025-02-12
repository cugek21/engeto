"""
game_functions.py: druhý projekt do Engeto Online Python Akademie

author: Radek Jíša
email: radek.jisa@gmail.com
"""

def introduction(divider: str) -> str:
    ''' return introduction message'''

    return f'''
{divider}
{'ENGETO ONLINE ACADEMY'.center(80)}
{'presents'.center(80)}
{divider}\n
{'BULLS and COWS'.center(80)}\n
{'aka'.center(80)}
{'\'Mastermind\''.center(80)}\n
{divider}\n
{'I\'ve generated a random 4 digit number for you.'.center(80)}
{'Guess which one is it.'.center(80)}\n
{divider}'''


def get_user_input() -> list:
    '''get the user's guess and validate it'''

    while True:
        user_number = input(f'{'':>38}').strip()

        if not user_number.isdigit():
            print(f'\n{'NOT a number! Enter the number:'.center(80)}')

        elif len(user_number) != 4:
            print(f'\n{'NOT 4 digits! Enter the number:'.center(80)}')

        elif user_number.startswith('0'):
            print(f'\n{'CANNOT start with zero! Enter the number:'.center(80)}')

        else:
            break

    return list(user_number)


def evaluate_guess(generated_number: list, user_number: list) -> tuple:
    '''evaluate the user's guess and compare with the generated number'''

    bulls = 0 #correct position
    cows = 0 #correct position, wrong position
    generated_number_copy = generated_number.copy()

    for position in range(4):
        if generated_number_copy[position] == user_number[position]:
            bulls += 1
            generated_number_copy[position] = None
            user_number[position] = None

    for position in range(4):
        if user_number[position] is not None and user_number[position] in generated_number_copy:
            cows +=1
            generated_number_copy[generated_number_copy.index(user_number[position])] = None
        
    return bulls,  cows


def get_plurals(bulls: int, cows: int) -> tuple:
    '''to handle pluralization'''

    bulls_word = 'bull ' if bulls == 1 else 'bulls'
    cows_word = 'cow ' if cows == 1 else 'cows'
    
    return bulls_word, cows_word


def calculate_time(start_time: float, end_time: float) -> tuple:
    '''to calculate the time taken to play the game'''

    time_elapsed = end_time - start_time
    minutes = time_elapsed // 60
    seconds = time_elapsed % 60
    
    return int(minutes), int(round(seconds)), int(round(time_elapsed))


def highscore(score: int) -> int:
    '''update and return highscore'''

    try:
        with open(r'highscore.txt', "r") as file:
            high_score = file.readline()
            if score < int(high_score):
                high_score = score

    except (FileNotFoundError, ValueError):
        high_score = score
    
    with open (r'highscore.txt', "w") as file:
        file.write(str(high_score))

    return int(high_score)


def credits(divider: str , mins: int, secs: int, high_score: int) -> str:
    '''rerturn ending credits with highscore'''

    minutes_label = '' if mins == 0 else f'{mins} min and '
    highscore_label = f'''
{divider}
{'CONGRATULATIONS!'.center(80)}
{'You won in ' + f'{minutes_label}{secs} sec.':^80}
{divider}
{'PERSONAL BEST'.center(80)}
{str(high_score) + ' sec':^80}
{divider}'''

    return highscore_label