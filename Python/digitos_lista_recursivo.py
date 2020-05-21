def contar(num):
    if num < 10:
        return 1 
    return contar(num // 10) + 1

def digitos_lista(lista):
    if lista == []:
        return 0
    return contar(lista[0] + digitos_lista(lista[1:]))

print(digitos_lista(list(range(10,21))))