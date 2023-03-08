print("Bienvenido")
print("Yo piens un numero y tu lo adivinas")


import random
number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess = input("Adivina el numero del 1 al 10: ")
    if int(guess) == number:
        print("elegiste {}. es correcto, ganaste!".format(guess))
        isGuessRight = True
    else:
        print("elegiste {}. no es correcto, intenta de nuevo.".format(guess))