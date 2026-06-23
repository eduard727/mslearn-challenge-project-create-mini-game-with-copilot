import random

score_win = 0
score_lose = 0
score_draw = 0

opciones = {
    "1": "Piedra",
    "2": "Papel",
    "3": "Tijeras",
}

while True:
    print("Menú:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijeras")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    print('\n')

    computadora = str(random.randint(1,3))
    print(f"Computadora eligió {computadora}")

    if opcion == "4":
        print("Saliendo...")
        break
    elif opcion == "1":
        print("Has elegido opción Piedra")
    elif opcion == "2":
        print("Has elegido opción Papel")
    elif opcion == "3":
        print("Has elegido opción Tijeras")
    else:
        print("Opción no válida. Intenta de nuevo.")
        continue

    computadora = str(random.randint(1, 3))
    print('\n')
    print(f"Has elegido: {opciones[opcion]}")
    print(f"Computadora eligió: {opciones[computadora]}")

    if opcion == computadora:
        print('\n')
        print("Empate")
        print('\n')
        score_draw += 1
    elif (opcion == "1" and computadora == "3") or (opcion == "2" and computadora == "1") or (opcion == "3" and computadora == "2"):
        print('\n')
        print("¡Has ganado!")
        print('\n')
        score_win += 1
    else:
        print('\n')
        print("Has perdido.")
        print('\n')
        score_lose += 1

    print(f"Puntuación - Ganadas: {score_win}, Perdidas: {score_lose}, Empates: {score_draw}")

print("Fin del programa")


