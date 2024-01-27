from math import hypot
cateto_oposto = int(input("Qual é o cateto oposto? "))
cateto_adjascente = int(input("Qual é o cateto adjascente? "))
hipotenusa = hypot(cateto_oposto, cateto_adjascente) 
print(f"O valor da hipotenusa é {hipotenusa:.0f}.")