userReply = input("Necesitas entregar un  paquete ?").capitalize()

if userReply == "Si":
    print("podemos ayudarte")
else:
      print("Ta bueno")
         # sirve para salir de la ejecucion del programa


userReply = input("Que te gustaria comprar, estampas,fotos o dibujos?").capitalize()

if userReply == "estampas":
    print("son 10 pesos")
elif userReply == "fotos":
    print("son 3 pesos")
elif userReply=="dibujos":
    print("son 20 pesos")
else:
    print("Vuelva pronto")
         # sirve para salir de la ejecucion del programa
