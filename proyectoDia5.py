
# def chequear_3_cifras(lista_3):
#     lista = []
#     lista_no_3_cifras = []
#     for e in lista_3:
#         if e in range(100, 1000):
#             lista.append(e)
#         else:
#             lista_no_3_cifras.append(e)
#     return lista, lista_no_3_cifras
#
#
#
#
# resultado = chequear_3_cifras([100, 99, 123, 1000])
# print(resultado)
#
#
# def desempacador_tuple(tuple):
#     for e in tuple:
#         mis_tuples = list(tuple)
#         tuple_lista1 = mis_tuples[0]
#         tuple_lista2 = mis_tuples[1]
#
#     print(tuple_lista1[1])
#     print(tuple_lista2[0])
#
#
# desempacador_tuple(resultado)
#
#
# precios_cafe =[('capuchino', 3.5), ('expresso', 2.2), ('moka', 1.9)]
#
# def precio_mas_alto_cafe(cafes_precio):
#     precios_mayor_cafe = 0
#     cafe_mas_caro = ''
#
#
#     for cafe, precio in cafes_precio:
#         if precio > precios_mayor_cafe:
#             precios_mayor_cafe = precio
#             cafe_mas_caro = cafe
#         else:
#             pass
#     return (cafe_mas_caro, precios_mayor_cafe)
#
#
#
#
#
# resultado = precio_mas_alto_cafe(precios_cafe)
# print(resultado)
#
#
# def suma(*args):
#     total = 0
#
#     for arg in args:
#         total += arg
#     return total
#
# resultado_suma = int(suma(77, 22, 125))
# print(resultado_suma)
#
#
#
# def suma(num1, num2, *args, **kwargs):
#     print(f'El primer valor es {num1}')
#     print(f'El segundo valor es {num2}')
#
#     for arg in args:
#         print(f'Arg es = a {arg}')
#     for clave, valor in kwargs.items():
# 	    print(f'{clave}:{valor}')
#
# suma(55, 33, 178, 66, 417, 555, x =789, y = 456, z = 2369 )




# # Proyecto numero 1
# Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
# Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el número de valorintermedio.

# def devolver_distintos(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     if total > 15:
#             print(f'Total: {total} Numero mas alto {max(args)}')
#
#     elif total < 15 and total in range(10, 16):
#         print(f"El numero se encuentra entre 10 y 15, el numero es: {total} ")
#     else:
#         print(f'Tu numero no supera a 15 ni se encuentra en el rango'
#               f' y el numero mas bajo es: {min(args)}')
#
# resultado_suma = devolver_distintos(1, 10, 33)




# Proyecto numero 2
# Escribe una función (puedes ponerle cualquier nombre que
# quieras) que reciba cualquier palabra como parámetro, y que
# devuelva todas sus letras únicas (sin repetir) pero en orden
# alfabético.

# def devolver_en_orden_alfabetico(palabra):
#     lista = []
#
#     for letra in palabra:
#         if letra not in lista:
#             lista.append(letra)
#
#     lista.sort()
#     print(' '.join(lista))
#
# devolver_en_orden_alfabetico('entretenido')



#Proyecto numero 3
# Escribe una función que requiera una cantidad indefinida de
# argumentos. Lo que hará esta función es devolver True si en
# algún momento se ha ingresado al numero cero repetido dos
# veces consecutivas.
#
#
# def ceros_cosecutivos(*args):
#     for i in range(len(args) - 1):
#         if args[i] == args[i + 1]:
#             return True
#     return False
#
#
# if ceros_cosecutivos(0, 2, 5, 0):
#     print('True')
# else:
#     print('False')




# # Proyecto numero 4
#Escribe una función llamada contar_primos() que requiera un
# solo argumento numérico.
# Esta función va a mostrar en pantalla todos los números
# primos existentes en el rango que va desde cero hasta ese
# número incluido, y va a devolver la cantidad de números
# primos que encontró.
# Aclaración, por convención el 0 y el 1 no se consideran primos.
# def contar_primos(num):
#     numero_usuario = int(num) + 1
#     numeros_primos = 2
#     indice = 0
#
#     for numero in range(numeros_primos, numero_usuario):
#         es_primo = True
#
#         for divisor in range(2, numero):
#             if numero % divisor == 0:
#                 es_primo = False
#                 break
#
#         if es_primo:
#             print(f"{numero} es primo")
#             indice += 1
#
#     print(f"La cantidad de numeros primos que encontramos en {num} es: {indice}")
#
# contar_primos(50)







from random import choice

palabras_lista = ['planta', 'naturaleza', 'ecosistema', 'magia', 'fantasia', 'realidad', 'vida', 'trading', 'pasion']
aleatorio = choice(palabras_lista).lower()
def mensaje_a_usuario():
    cantidad_letras_palabra = len(aleatorio)
    print(f'La palabra que salio al azar tiene {cantidad_letras_palabra} caracteres '
          f'Usted cuenta con 6 vidas para adivinar la palabra.')
    return cantidad_letras_palabra

def representacion_letras_en_guiones(cantidad):
    cantidad_giunes = list('_') * cantidad
    return cantidad_giunes

def pedir_usuario_letra():
    # print(aleatorio)
    mi_lista_guines = guiones
    vidas = 6 - 1
    letras_ingresadas = set()
    letras_adivinadas = set()
    while vidas != 0 - 1:
        letra_usuario = input('Dime una letra: ').lower()
        if letra_usuario.isalpha() and len(letra_usuario) == 1:
            if letra_usuario in letras_ingresadas:
                print(f'La letra "{letra_usuario}" ya ha sido ingresada antes.')
                letras_ingresadas.add(letra_usuario)
            else:
                letras_ingresadas.add(letra_usuario)
                while letra_usuario in aleatorio:
                    for i, letra in enumerate(aleatorio):
                        if letra == letra_usuario:
                            mi_lista_guines[i] = letra_usuario
                            letras_adivinadas.add(letra_usuario)


                    print('\n')
                    print(f"Letras ingresadas{letras_ingresadas}")
                    print(f'Letras correctas: {letras_adivinadas}')
                    print(mi_lista_guines)

                    if letras_adivinadas == set(aleatorio):
                        print('¡Felicidades! Has adivinado todas las letras.')
                        break
                    print('\n')
                    letra_usuario = input('Dime una letra: ').lower()

                else:
                    print(f'La letra que elegiste "{letra_usuario}" no esta en la palabra, te quedan {vidas} vidas')
                    letras_ingresadas.add(letra_usuario)
                    print(f"Letras ingresadas{letras_ingresadas}")

            vidas -= 1
        else:
            print(f'Haz elegido un caracter no correspondiente')

cantidad_caracteres = mensaje_a_usuario()
guiones = representacion_letras_en_guiones(cantidad_caracteres)

pedir_usuario_letra()


