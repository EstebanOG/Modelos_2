cuenta_cifras lista = [if x < 10 then "Una cifra" else "Dos cifras"
                        |x <- lista, odd x]
