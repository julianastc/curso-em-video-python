
numero = int(input("Informe um número: "))

un_numero = int(str(numero)[-1])
dez_numero = int(str(numero)[-2])
cen_numero = int(str(numero)[-3]) 
mi_numero = int(str(numero)[-4])


print("Analisando o número...")

print(f'''
    Unidade: {un_numero}
    Dezena:  {dez_numero}
    Centena: {cen_numero}
    Milhar:  {mi_numero}
''')
