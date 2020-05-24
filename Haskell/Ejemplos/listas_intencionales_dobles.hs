longitud lista = sum[1|x <- lista]

mostrar_vocales frase = [letra |letra <- frase, letra `elem` ['a', 'e', 'i', 'o', 'u']]

sumar_vocales frase_c = sum[1 | x <- (mostrar_vocales frase_c)]