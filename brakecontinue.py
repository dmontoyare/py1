# Bracke y continue
# Ciclo for para imprimir los numeros del 1 al 1000 excluyendo los numeros pares





def run():
    for contador in range(1, 11):
        if contador % 2 != 0:
            continue
        print (contador)


    for contador in range(1, 11):
        if contador == 5:
            break
        print (contador)



if __name__ == '__main__':
    run()