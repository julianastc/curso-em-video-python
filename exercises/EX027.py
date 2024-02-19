complete_name = str(input('Digite seu nome: '))

formated_name = complete_name.strip().title()
split_name = formated_name.split()
first_name = split_name[0]
last_name = split_name[-1]

print(f'''Muito prazer em te conhecer! 
    Seu primeiro nome é {first_name}
    Seu último nome é {last_name}
''')