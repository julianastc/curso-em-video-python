ProductOriginalPrice = float(input("Qual é o preço do produto? R$"))
ProductDescontPrice = ProductOriginalPrice - (ProductOriginalPrice * (5/100)) 
print(f"O produto que custava R${ProductOriginalPrice}, na promoção com desconto de 5% custará R${ProductDescontPrice:.2f}")
