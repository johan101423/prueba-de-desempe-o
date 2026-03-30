

# numeric and word validation

def pedirNumero(msg, tipo):
    terminate =     True
    while terminate :
        try:
            if tipo == "int":
                pedir = int(input(msg))
            elif tipo == "float":
                pedir = float(input(msg))
            
            if pedir < 0:
                print("ENTER POSITIVE NUMBER")
                continue

            return pedir

        except:
            print("Option  not valid") 




def pedirNumero2():

    seguir=True
    while seguir:
        try:
            numero=int(input())
            seguir=False
            return numero
        except ValueError:
            print("option not")


         

def pedirPalabra(msg):
    terminate = 0
    while terminate == 0:
        try:
            pedir = str(input(msg))
            if pedir.isalpha() == False:
                print("Por favor colocar solo una palabra")
                continue
            return pedir
        except:
            print("option not valid") 

