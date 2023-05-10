import Class_Tiles
class Room : 
    roomId = 0

    size = 0
    map = [0,0]
    
    def __init__(self,_Id,):
        self.roomId = _Id #ex :
        #creation d'une map en fonction de roomID

        if (self.roomID == 11):
             self.size = 11
             for i in self.size :
                 for j in self.size:
                     if (i == 0 or i == 11):
                         bob # à finir
    
    def getSize(self):
        return self.size
