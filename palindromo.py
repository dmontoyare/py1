

def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    if palabra == palabra[::-1]:
        return True
    elif palabra != palabra[::-1]:
        return False 


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)


    if es_palindromo == True:
        print("La palabra " + palabra + " es un palindromo")
    
    elif es_palindromo == False:
        print("La palabra " + palabra + " no es un palindromo")



if __name__ == '__main__':
    run()
