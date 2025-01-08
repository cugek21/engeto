print('Sčítání:  \'+\'')
print('Odčítání: \'-\'')
print('-' * 20)

valid_operators = ['+', '-']

while True:
    choice = input('Vyber si operaci:').strip()
    if choice in valid_operators:
        number_1 = input('Zadej první číslo:').strip()
        number_2 = input('Zadej druhé číslo:').strip()
        if number_1.isdigit() and number_2.isdigit():
            add = int(number_1) + int(number_2)
            sub = int(number_1) - int(number_2)
            print(f'{number_1} {choice} {number_2} = {add if choice == '+' else sub}')
            next = input('Chcete provést další operaci?(\'a\' pro ano, jakákoliv jiná klávesa pro ne):').strip()
            if next == 'a':
                continue
            else:
                exit()
    else:
        print('Nezadali jste platný operátor, zkuste to znovu.')