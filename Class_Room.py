import Class_Tiles
class Room : 
    map = [0,0]
    roomId = 0
    size = 0
    def __init__(self,_maps,_Id,_size):
        self.size = _size
        self.map = _maps 
        self.roomId = _Id
   
    def getSize(self):
        return self.size
