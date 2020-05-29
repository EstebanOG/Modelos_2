from random import shuffle


def baraja():
    return [(n,p) for n in ['A','J','Q','K']+[str(x) for x in range(2,11)] for p in ['Picas', 'Corazones', 'Tréboles', 'Diamantes']]

def mezclar(baraja):
    shuffle(baraja)
    return baraja

def sacar_carta(mazo):
    if mazo ==[]:
        pass
    else:
        print(mazo[0])
        sacar_carta(mazo[1:])

def valor_carta(carta):
    if carta[0] in ['J', 'Q', 'K']:
        return 10
    elif carta[0] == 'A':
        return 1
    else:
        return int(carta[0])

def valor_mano(mano):
    if mano == []:
        return 0
    return valor_carta(mano[0]) + valor_mano(mano[1:])

def valor_mano_recargado(mano):
    if mano == []:
        return 0
    elif valor_mano(mano) <= 11 and 1 in [valor_carta(x) for x in mano]:
        return valor_mano(mano) + 10
    else:
        return valor_mano(mano)

def jugar(mazo, jugador, repartidor):
    if len(mazo) > 48:
        jugar(mazo[2:], jugador+[mazo[0]], repartidor+[mazo[1]])
    else: 
        print (jugador, "[Carta oculta," , repartidor[1],"]")
        if len(mazo) > 2 and valor_mano_recargado(jugador) <= 21:
            if input("Pedir carta(s/n): ").capitalize() == "S":
                jugar(mazo[1:], jugador+[mazo[0]], repartidor)
            else:
                if valor_mano_recargado(jugador)<=valor_mano_recargado(repartidor):
                    print (jugador, repartidor)
                    print("Gana el repartidor")
                else:
                    juego_repartidor(mazo,jugador,repartidor)  
        else:
            print("Juego:")
            print (jugador, repartidor)
            print("Gana el repartidor")

def juego_repartidor(mazo,jugador,repartidor):
    print (jugador, repartidor)
    if valor_mano_recargado(repartidor)<valor_mano_recargado(jugador) and valor_mano_recargado(repartidor) < 21:
        juego_repartidor(mazo[1:],jugador,repartidor+[mazo[0]])
    else:
        if valor_mano_recargado(jugador)<=valor_mano_recargado(repartidor) and valor_mano_recargado(repartidor)<=21:
            print("Juego:")
            print (jugador, repartidor)
            print("Gana el repartidor")
        else:
            print("Juego:")
            print (jugador, repartidor)
            print("Gana el jugador")

#print(mezclar(baraja()))
#sacar_carta(mezclar(baraja()))
#print(valor_mano_recargado(mezclar(baraja())[:2]))
jugar(mezclar(baraja()), [], [])