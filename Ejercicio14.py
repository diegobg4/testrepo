from unittest import result


def suma_filas(m):
    resultado = [0] * len(m)
    print(resultado)
    for i in range(len(m)):
        suma = 0
        for x in range(len(m[i])):
            suma = suma + m[i][x]
        resultado[i] = suma
    return resultado

v1 = [[1,1,2,1],[1,1,1,1], [2,2]]

print(suma_filas(v1))