from baraja import Baraja
from mano import Mano

class Juego:
    def __init__(self):
        self.baraja= Baraja()
        self.baraja.barajar()
    
    def jugar(self):
        manoJugador=Mano()
        manoJugador.añadirCarta(self.baraja.sacarCarta())
        print(f"Tu mano es {manoJugador.cartas}")