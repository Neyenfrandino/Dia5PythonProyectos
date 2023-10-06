#
#
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
# devolver_en_orden_alfabetico('fantastico')
#






