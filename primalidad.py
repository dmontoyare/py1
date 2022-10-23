
def es_primo(numero):
    caja = 0

    for i in range(1, numero + 1): 
        if i == 1 or i == numero:
            continue 
        if numero % i == 0:
            caja += 1


    if caja == 0:
        return True
    elif caja != 0:
        return False 

def run():
    print("""Bienvenido al identificador de numeros primos,
por favor siga las instrucciones para indentificar 
si un numero es primo 
 """)
      
    numero = int(input("Escribe el numero que deseas evaluar: "))
    if es_primo(numero) == True:
        print("Apreciado usuario, el numero es primo")
    elif es_primo(numero) == False:
        print("Apreciado usuario, el numero NO es primo")




if __name__ == '__main__':
    run()