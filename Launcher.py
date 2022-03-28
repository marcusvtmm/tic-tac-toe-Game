from re import A
from Game import Game
from Player import Player



jogo = Game()

jogador1 = Player(0) #Bolinha
jogador2 = Player(1) #Cruzinha
running = True
while running:
    
    jogo.turn(jogador1, 1, 2)
    jogo.drawnGame()
    running = not jogo.win()

print("Parabens cabaço")