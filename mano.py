from carta import Carta

class Mano:
    def __init__(self):
        self.cartas =[]
        self.valor = 0

    def añadirCarta(self,carta):
        self.cartas.append(carta)
        for carta in self.cartas:
            if carta.valor in ["Jota","Reina","Rey"]:
                self.valor =10
            elif carta.valor == "As": 
                 self.valor +=11
            else:
                self.valor += int (carta.valor)

    def mostrarMano(self):
        for carta in self.cartas:
            print(carta)

class Juego:
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