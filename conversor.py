

# 


menu = """
Bienvenido al conversior de monedas 💰
Escriba el numero correspondiente a la divisa que desea convertir

1 - Peso colombiano
2 - Peso argentino
3 - Peso mexicano
"""
opcion = int(input(menu))

if opcion == 1:
    pesos = input ("¿Cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 4000
    dolares = pesos / valor_dolar 
    dolares= round(dolares, 2)
    dolares = str(dolares)
    print ("Tienes $" + dolares + " dólares")

elif opcion == 2:
    esos = input ("¿Cuantos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar 
    dolares= round(dolares, 2)
    dolares = str(dolares)
    print ("Tienes $" + dolares + " dólares")

elif opcion == 3:
    pesos = input ("¿Cuantos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dola1r = 24
    dolares = pesos / valor_dolar 
    dolares= round(dolares, 2)
    dolares = str(dolares)
    print ("Tienes $" + dolares + " dólares")

else: 
    print("Por favor escribe una opcion correcta")

