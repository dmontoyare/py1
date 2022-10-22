


def conversor(tipo_pesos, valor_dolar):
    pesos = input ("¿Cuantos pesos" + tipo_pesos+ "tienes?: ")
    pesos = float(pesos)
    valor_dolar = valor_dolar
    dolares = pesos / valor_dolar 
    dolares= round(dolares, 2)
    dolares = str(dolares)
    print ("Tienes $" + dolares + " dólares")



menu = """
Bienvenido al conversior de monedas 💰
Escriba el numero correspondiente a la divisa que desea convertir

1 - Peso colombiano
2 - Peso argentino
3 - Peso mexicano
"""
opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 4000)

elif opcion == 2:
    conversor("argentinos", 65)

elif opcion == 3:
   onversor("mexicanos", 56)

else: 
    print("Por favor escribe una opcion correcta")
   
