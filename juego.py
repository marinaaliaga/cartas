from baraja import Baraja
from mano import Mano
from carta import Carta

class Juego:
    def __init__(self):
        self.baraja= Baraja()
        self.baraja.Baraja()
    
    def jugar(self):
        manoJugador=Mano()
        manoJugador.añadirCarta(self.baraja.sacarCarta())
        print(f"Tu mano es{manoJugador.cartas}")
        print(f"Total:{manoJugador.valor}")
        while manoJugador.valor <21:
            accion= input("¿Quieres pedir carta o pasar?").lower()
            if accion == "pedir":
                manoJugador.añadirCarta(self.baraja.sacarCarta())
                print(f"Tu mano es {manoJugador.cartas()}")
                print(f"valor {manoJugador.valor}")
            else:
                print(f"Tu puntuacion final es {manoJugador.valor}")
                return
        if manoJugador.valor ==21:
            print ("ENHORABUENA")
        elif manoJugador. valor <21:
            print("No has llegado a 21")
        else:
            print("Te has pasado")
            
    def __init__(self):
        self.jugador1 = Mano()
        self.jugador2 = Mano()
    
    def repartirCartas(self,cartas_j1, cartas_j2):
        for carta in cartas_j1:
            self.jugador1.añadirCarta(carta)

        for carta in cartas_j2:
            self.jugador2.añadirCarta(carta) 

    def mostrarManos(self):
        print("Mano del jugador 1:")
        self.jugador1.mostrarMano()
        print("Valor total:", self.jugador1.valor)

        print("Mano del jugador 2:")
        self.jugador2.mostrarMano()
        print("Valor total:", self.jugador2.valor)

juego =Juego()

cartas_j1 = [Carta("As",11), Carta("5",5)]
cartas_j2 = [Carta("Rey",10), Carta("3",3)]

juego.repartirCartas(cartas_j1,cartas_j2)
juego.mostrarManos()

if __name__ == '__main__':
    print("JUEGO DE 21")
    juego = Juego()
    juego.jugar()
