
#: sempre que a soma das medidas dos segmentos que estão sendo girados for maior que a medida do terceiro segmento, é possível construir um triângulo.

r1 = int(input('Qual o valor da reta 1? '))
r2 = int(input('Qual o valor da reta 2? '))
r3 = int(input('Qual o valor da reta 3? '))

list_r = [r1,r2,r3]
sorted_list_r = sorted(list_r)
property_r = sorted_list_r[0] + sorted_list_r[1]
triangle_rule_one = sorted_list_r[2] < property_r 

if triangle_rule_one:
    print('É possível formar um triângulo! ')
else:
    print('Não é possível formar um triângulo.')
