import Tiles


class Room : 
    
    def __init__(self,_Id):
        self.roomId = _Id 
        self.map = []
        
        #creation d'une map en fonction de roomId
        
        #création des tiles, avec des conditions lignes par lignes (le j)
            #Rappel : 0 = sol // 1 = mur // 3 = entrée // 4 = sortie
        
   
        f = open(f"Salle{_Id}.txt")

        tempMap = []
        i = 0
        for line in f.readlines():
            line=line.strip("\n")
            tempMap.append([])
            for c in line:
                tempMap[i].append((Tiles.Tiles(int(c))))
            i = i + 1 
        i = 0
        for i in range(len(tempMap[0])) :
            self.map.append([])
            for j in range(len(tempMap[1])) :
                self.map[i].append(tempMap[j][i]) 
        self.size=len(self.map[0])







    def __repr__(self,_currentScreen,_tilesize):
        for i in range(self.size):
            for j in range(self.size):
                self.map[j][i].__repr__(_currentScreen,_tilesize,j,i)