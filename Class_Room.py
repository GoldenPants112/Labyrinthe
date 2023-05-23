import Class_Tiles


class Room : 
    
    def __init__(self,_Id):
        self.roomId = _Id 
        self.map = []
        #creation d'une map en fonction de roomId
        
        #création des tiles, avec des conditions lignes par lignes (le j)
            #Rappel : 1 = sol // 2 = mur // 3 = entrée // 4 = sortie
        
        


        if (self.roomId == 1):
            
            f = open("Salle1.txt")
            i = 0
            for line in f.readlines:
                self.map.append([])
                for c in line:
                    self.map[i].append((Class_Tiles.Tiles(int(c))))
                i = i + 1 

    def __repr__(self,_currentScreen,_screenSize):
        for j in self.size:
            for i in self.size:
                