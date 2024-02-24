
numero = int(input("Informe um número: "))

un_numero = numero // 1 % 10
dez_numero = numero // 10 % 10
cen_numero = numero // 100 % 10
mi_numero = numero // 1000 % 10


print("Analisando o número...")

print(f'''
    Unidade: {un_numero}
    Dezena:  {dez_numero}
    Centena: {cen_numero}
    Milhar:  {mi_numero}
''')
