# CLASS POPULATION

import numpy as np
import random

class population(object):
    def __init__(self,nombre_individus,map_size,espece):
        self.map_size = map_size
        self.list_individus = [espece(self.map_size) for _ in range(int(nombre_individus))]
        self.nombre_individus = len(self.list_individus)
        assert(len(self.list_individus)==self.nombre_individus), str(len(self.list_individus))+'!='+str(self.nombre_individus)
        self.demographie = [self.nombre_individus,]
    
    def generate(self,number,espece):
        if number < 1.:
            if (random.randrange(100) < number*100):
                self.list_individus.append(espece(self.map_size))
        else:
            for i in range(number):
                self.list_individus.append(espece(self.map_size))
        self.nombre_individus = len(self.list_individus)
    
    def get_coords(self):
        list_X = []
        list_Y = []
        for individu in self.list_individus:
            list_X.append(individu.X)
            list_Y.append(individu.Y)
        return np.array(list_X),np.array(list_Y)
    
    def deplacement(self):
        [individu.move(self.map_size) for individu in self.list_individus]
    
    def search_food(self,nourriture):
        [individu.search_food(nourriture) for individu in self.list_individus]
        
    def starve(self):
        for idx,individu in enumerate(self.list_individus):
            if individu.starve():
                del(self.list_individus[idx])
                self.nombre_individus -= 1
                
    def reproduce(self):
        new_individus = []
        for individu in self.list_individus:
            new_individus.extend(individu.reproduce(self.map_size))
        
        self.list_individus.extend(new_individus)
        self.nombre_individus = len(self.list_individus)