# carro 60 por dia 0,15 por km 
DaysUsed = int(input("Quantos dias foram usados? "))
KmUsed = float(input("Quantos kilometros foram rodados? "))
TotalValue = (DaysUsed * 60) + (KmUsed * 0.15)
print(f"O total a pagar é {TotalValue:.2f}")
