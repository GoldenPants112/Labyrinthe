import Class_Tiles

class Room : 
    
    def __init__(self,_Id):
        self.roomId = _Id 
        self.map = []
        #creation d'une map en fonction de roomId
        
        #création des tiles, avec des conditions lignes par lignes (le j)
            #Rappel : 1001 = sol // 1002 = mur // 1003 = entrée // 1004 = sortie
        
        if (self.roomId == 1):
            self.size = 11
            for j in range(self.size) :
                self.map.append([])
                for i in range(self.size) :
                    
                    #1ere et 11e ligne (que des murs)
                    if (j == 0 or j == 10):
                        self.map[i].append(Class_Tiles.Tiles(1002))

                    #2e ligne
                    if (j == 1):

                        if ((i >= 5 and i <= 7) or i == 9):
                            self.map[i].append(Class_Tiles.Tiles.__init__(1001))

                        if ( (i >= 0 and i <= 4) or i == 8 or i == 10):
                            self.map[i].append(Class_Tiles.Tiles.__init__(1002))
                        
                    #3e ligne    
                    if (j == 2): 

                        if (i == 0 or i == 4 or i == 10):
                            self.map[i].append(Class_Tiles.Tiles.__init__(1002))

                        else :
                            self.map[i].append(Class_Tiles.Tiles.__init__(1001))

                    #4e ligne
                    if(j == 3):
                        if(i == 3 or i == 5 or i == 9) :
                            self.map[i].append(Class_Tiles.Tiles.__init__(1001))
                        else :
                            self.map[i].append(Class_Tiles.Tiles.__init__(1002))

                    #5e ligne
                    if (j == 4):
                        if(i == 0 or i == 2 or i == 8 or i == 10 ):
                            self.map[i].append(Class_Tiles.Tiles.__init__(1002))
                        else:
                            self.map[i].append(Class_Tiles.Tiles.__init__(1001))
                    
                    #6e ligne
                    if (j == 5):
                        if (i == 0):
                            self.map[i].append(Class_Tiles.Tiles.__init__(1003))
                        if (i == 1 or i == 3 or i == 7 or i == 9):
                            self.map[i].append(Class_Tiles.Tiles.__init__(1001))
                        if (i == 10):
                            self.map[i].append(Class_Tiles.Tiles.__init__(1004))
                        else:
                            self.map[i].append(Class_Tiles.Tiles.__init__(1002))
                    
                    #7e ligne
                    if(j == 6):
                        if (i == 1 or i == 7 or (i >= 3 and i <= 5)):
                            self.map[i].append(Class_Tiles.Tiles.__init__(1001))
                        else:
                            self.map[i].append(Class_Tiles.Tiles.__init__(1002))

                    #8e ligne
                    if(j == 7):
                        if (i == 1 or i == 3 or i == 7 or i == 9):
                            self.map[i].append(Class_Tiles.Tiles.__init__(1001))
                        else:
                            self.map[i].append(Class_Tiles.Tiles.__init__(1002)) 

                    #9e ligne
                    if(j == 8):
                        if (i == 0 or i == 2 or i == 4 or i == 8 or i == 10):
                            self.map[i].append(Class_Tiles.Tiles.__init__(1002))
                        else:
                            self.map[i].append(Class_Tiles.Tiles.__init__(1001))

                    #10e ligne
                    if(j == 9):
                        if (i == 0 or i == 6 or i == 10):
                            self.map[i].append(Class_Tiles.Tiles.__init__(1002))
                        else:
                            self.map[i].append(Class_Tiles.Tiles.__init__(1001))  

    def __repr__(self):
        for j in self.size:
            for i in self.size:
                self.map[i,j].__repr__(self.size)

                