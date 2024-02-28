#For each digit between 0-9, the program will print a confirmation 
#for the entered value or print "invalid inputs" for all other numbers.


number = int(input("Digite um número: "))

if (number == 0):
    print("Entered 0")
elif (number == 1):
    print("Entered 1")
else:
    print("\033[31mInvalid number")
