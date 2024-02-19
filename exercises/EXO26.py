frase = str(input('Digite uma frase: '))

formated_frase = frase.lower().strip()
total_a = formated_frase.count('a')
first_position_a = formated_frase.find('a')
last_positon_a = formated_frase.rfind('a')


print(f'''A letra "A" aparece {total_a} vezes.
    A primeira letra "A" apareceu na posição {first_position_a}.
    A última letra "A" apareceu na posição {last_positon_a} .
    ''')