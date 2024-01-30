def jugar_cachipun():
    marcador_A = 0
    marcador_B = 0

    while True:
        jugada_A = input("Jugador A, elige tijera, papel o piedra: ")
        jugada_B = input("Jugador B, elige tijera, papel o piedra: ")

        if jugada_A == jugada_B:
            print("Empate")
        elif (
            (jugada_A == "tijera" and jugada_B == "papel")
            or (jugada_A == "papel" and jugada_B == "piedra")
            or (jugada_A == "piedra" and jugada_B == "tijeras")
        ):
            print("A gana la ronda")
            marcador_A += 1
        else:
            print("B gana la ronda")
            marcador_B += 1
        print(f"A: {jugada_A}\nB: {jugada_B}")
        print(f"{marcador_A} - {marcador_B}")

        if marcador_A == 3:
            print("¡Jugador A ha ganado el juego!")
            break
        elif marcador_B == 3:
            print("¡Jugador B ha ganado el juego!")
            break
if __name__ == "__main__":
    jugar_cachipun()