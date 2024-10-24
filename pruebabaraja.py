from baraja import Baraja

miBaraja = Baraja()
miBaraja.mostrarCartas()

if miBaraja.quedanCartas():
    print("Hay cartas")
else:
    print("No quedan cartas.")

while miBaraja.quedanCartas():
        carta = miBaraja.sacarCarta()
        numCartas = miBaraja.contar()
        print(f"{carta} Quedan {numCartas}")