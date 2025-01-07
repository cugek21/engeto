"""
project_01.py: first project for Engeto Online Python Akademie

author: Radek Jisa
email: radek.jisa@gmail.com
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

user_data = {
    'bob': '123', 
    'ann': 'pass123', 
    'mike': 'password123', 
    'liz': 'pass123'
}

attempts = 5
separator = '-' * 40
exit_str = 'All attempts used. Terminating program.'

#Login
login = True
login_count = 0
while login:
    username = input('Enter username:').strip()
    login_count += 1
    if username in user_data:
        password = input('Enter password:')
        if password == user_data.get(username):
            login = False
        elif login_count < attempts:
            print('Wrong password. {} attempt(s) remaining.'.format(attempts - login_count))
        else:
            print(exit_str)
            exit()
    elif login_count < attempts:
        print('Unknown username. {} attempt(s) remaining.'.format(attempts - login_count))
    else:
        print(exit_str)
        exit()


#Invitation
print(separator)
print('Welcome to the app, {}.'.format(username.capitalize()))
print('We have 3 texts to be analyzed.')
print(separator)

#Text selection
selection = True
selection_count = 0
while selection:
    text_num = input('Enter a number btw. 1 and 3 to select:').strip()
    selection_count += 1
    if text_num.isdigit():
        if int(text_num) in range(1,4):
            selection = False
        elif selection_count < attempts:
            print('Number isn`t in range. {} attempt(s) remaining.'.format(attempts - selection_count))
        else:
            print(exit_str)
            exit()
    elif selection_count < attempts:
        print('That isn`t number. {} attempt(s) remaining.'.format(attempts - selection_count))
    else:
        print(exit_str)
        exit()

selected_text = TEXTS[int(text_num) - 1]

print(separator)


#Stats
title = 0
upper = 0
lower = 0
numeric = 0
sum_ = 0

for word in selected_text.split():
    if word.istitle():
        title += 1
    if word.isupper() and word.isalpha():
        upper += 1
    if word.islower():
        lower += 1
    if word.isnumeric():
        numeric += 1
        sum_ += int(word)

print('There are {} words in the selected text.'.format(len(selected_text.split())))
print('There are {} titlecase words.'.format(title))
print('There are {} uppercase words.'.format(upper))
print('There are {} lowercase words.'.format(lower))
print('There are {} numeric strings.'.format(numeric))
print('The sum of all the numbers {}.'.format(sum_))


print(separator)
print('{:3}|{:^20}|{}'.format('LEN','OCCURANCES','NR.'))
print(separator)

#Graph
occurancy = {}
for word in selected_text.split():
    occurancy.setdefault(len(word.strip(',.')), 0)
    occurancy[len(word.strip(',.'))] += 1

occurancy_sort = dict(sorted(occurancy.items()))
for graph in occurancy_sort:
    print('{:3}|{:<20}|{}'.format(graph,'*' * occurancy_sort.get(graph), occurancy_sort.get(graph)))

print('{:-^40}'.format(' THE END '))