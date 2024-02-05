complete_name = str(input("Digite seu nome completo: "))
#analisando dados .. maisculas, minusculas, total letras, primeiro nome e quantas letraas
upper_name = complete_name.upper()
lower_name = complete_name.lower()
total_carac_name = complete_name.__len__()
first_name = complete_name.split(" ")[2] 
total_carac_first_name =  first_name.__len__()

print(f'''Analisando seu nome...
    Seu nome em maiúsculas é {upper_name}
    Seu nome em minuscúlas é {lower_name}
    Seu nome tem ao todo {total_carac_name} letras
    Seu primeiro nome é {first_name} e ele tem {total_carac_first_name} letras''')