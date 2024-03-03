#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ela vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. 
#prestação = valorcasa / tempo  < salario * 0.30 

total_price = float(input('Qual o valor total da casa? '))
total_time = int(input('Em quantos anos quer pagar? '))
total_salary = float(input('Qual seu salário? '))

total_time_months = total_time * 12

installment = total_price / total_time_months

rule_installment = installment < (total_salary * 0.30)
if rule_installment:
    print(f'\033[32mAprovado!\033[mO valor da prestação será de {installment:.2f}! ')
else: 
    print(f'\033[31mReprovado!\033[mA prestação excedeu o limite. ')