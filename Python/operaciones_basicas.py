def digitos_lista(lista):
    aux = 0
    for i in lista:
        while i > 9:
            i = i // 10
            aux += 1
        aux += 1
    return aux

print(digitos_lista(range(10,21)))
