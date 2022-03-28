class Game:
    def __init__(self):
        
        
        #Matriz tabuleiro
        self.tabuleiro = []
        for i in range(3):
            linha = []
            for j in range(3):
                linha.append(" [ ] ")
            self.tabuleiro.append(linha)

    #desenha o tabuleiro no prompt
    def drawnGame(self):
        for i in range(3):
            print(self.tabuleiro[i])

    #jogada/turno
    def turn(self,player,x,y):
        if self.tabuleiro[x][y] == "[]":
            player.setPosition(x,y)
            self.tabuleiro[x][y] = "["+player.getType()+"]"
        else:
            pass #WIP
        

    def win(self, posPlayer):
        if (1 in posPlayer) == False:
            return False
        else:
            return True
