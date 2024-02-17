complete_name = str(input('Qual seu nome completo? '))

formated_name = complete_name.lower().strip()
rule_verification = 'silva' in formated_name

print(f'Seu nome tem Silva? {rule_verification}')