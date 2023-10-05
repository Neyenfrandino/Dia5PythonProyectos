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


def devolver_distintos(*args):
    total = 0
    numero_mas_alto = 0
    for arg in args:
        total += arg
    if total > 15:
        if total > numero_mas_alto:
            numero_mas_alto = arg
            print(f'Total: {total} Numero mas alto {numero_mas_alto}')

    else:
        print(f"El numero no supera a 15")


resultado_suma = devolver_distintos(1, 5, 6)


