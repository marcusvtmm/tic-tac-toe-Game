
tipo = {
    0:"O",
    1:"X"
}



class Player:
    def __init__(self,type=-1):
        self.type = type

    def setPosition(self,x,y):
        self.position=[]
        self.position.append([x,y])

    def getType(self):
        if self != -1:
            return tipo[self.type]
        else:
            return print("tipo nao existente")

        