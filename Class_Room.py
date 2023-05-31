import Class_Tiles


class Room : 
    
    def __init__(self,_Id):
        self.roomId = _Id 
        self.map = []
        #creation d'une map en fonction de roomId
        
        #création des tiles, avec des conditions lignes par lignes (le j)
            #Rappel : 0 = sol // 1 = mur // 3 = entrée // 4 = sortie
        
        if (self.roomId == 1):
            f = open("Salle1.txt")
            i = 0
            for line in f.readlines():
                line=line.strip("\n")
                self.map.append([])
                for c in line:
                    self.map[i].append((Class_Tiles.Tiles(int(c))))
                i = i + 1 
            self.size=len(self.map[0])
        if (self.roomId == 2):
            f = open("Salle2.txt")
            i = 0
            for line in f.readlines():
                line=line.strip("\n")
                self.map.append([])
                for c in line:
                    self.map[i].append((Class_Tiles.Tiles(int(c))))
                i = i + 1
            self.size=len(self.map[0])
        

    def __repr__(self,_currentScreen,_tilesize):
        for j in self.size:
            for i in self.size:
                self.map[i][j].__repr__(_currentScreen,_tilesize,i,j)