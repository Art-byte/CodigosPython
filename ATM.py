print("Bienvenido al banco de pytho")
restart = ('Y')
chances = 3
balance = 999.12

while chances >= 0:
    pin = int(input("Porfavor, ingrese su pin de 4 digitos: "))
    if(pin==1234):
        print("Has ingresado el pin correctamente")
        print("Selecciona 1 para ver tu balance")
        print("Selecciona 2 para ver withdralw")
        print("Selecciona 3 para pagar")
        print("Selecciona 4 para salir")

        while restart not in('n','N0','no','N'):
            print("Has ingresado el pin correctamente")
            print("Selecciona 1 para ver tu balance")
            print("Selecciona 2 para ver withdralw")
            print("Selecciona 3 para pagar")
            print("Selecciona 4 para salir")
            option = int(input("Que es lo que deseas hacer?: "))
            if(option == 1):
                print("Tu balance es: $",balance)
                restart = input('Te gustaria regresar?')
                if restart in('n','N0','no','N'):
                    print('Gracias')
                    break
            elif(option == 2):
                option2 =('y')
                withdrawl = float(input('algo que no se como se dice en espaniol 10,20,40,60,60,100 for other enter:1'))


