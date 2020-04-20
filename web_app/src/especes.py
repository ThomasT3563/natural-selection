# ALL DEFINES SPECIES CLASSES

import numpy as np
import random

from src.individus import individus

class espece_herbivore(individus):
    def __init__(self,map_size,initial_coordinates=None):
        super().__init__(map_size,initial_coordinates)

        self.color = "blue"
        self.size = 100
        self.reproduction_threshold = 200
        self.hunger_decay = 4

        direction = random.randint(0,360)
        self.speed = 1.
        self.vec_speed = [self.speed*np.cos(direction),self.speed*np.sin(direction)]
        
        self.nutriment = 200
        self.vision = 5
        
    def reproduce(self,map_size):
        if (self.size > self.reproduction_threshold):
            self.size -= 100
            new_individu = self.__class__(map_size,initial_coordinates=[self.X,self.Y])
            return [new_individu,]
        else:
            return []
    
class espece_plante(individus):
    def __init__(self,map_size,initial_coordinates=None):
        super().__init__(map_size,initial_coordinates)
        self.color = "green"
        self.nutriment = 100
        
        # pour plantes carnivores
        self.speed = 0.7 # == eat distance
        self.vec_speed = [0.,0.]
        self.vision = 0.
        self.size = 0.
    
    def reproduce(self,map_size):
        new_individus = []
        
        if (random.randrange(100) < 2):
            positions = [[0.,1.],[0.,-1.],[1.,0.],[-1.,0.]]
            random.shuffle(positions)
            
            nx = self.X+positions[0][0]
            ny = self.Y+positions[0][1]
            if not((nx>map_size[0] or nx<0) or (ny>map_size[1] or ny<0)):
                new_individus.append(self.__class__(map_size,initial_coordinates=[nx,ny]))
                    
        return new_individus
    

class espece_carnivore(individus):
    def __init__(self,map_size,initial_coordinates=None):
        super().__init__(map_size,initial_coordinates)

        self.color = "red"
        self.size = 200
        self.nutriment = 200
        self.reproduction_threshold = 400
        self.hunger_decay = 4

        direction = random.randint(0,360)
        self.speed = 0.55
        self.vec_speed = [self.speed*np.cos(direction),self.speed*np.sin(direction)]
        
        self.vision = 6
        
    def reproduce(self,map_size):
        if (self.size > self.reproduction_threshold):
            self.size -= 100
            new_individu = self.__class__(map_size,initial_coordinates=[self.X,self.Y])
            return [new_individu,]
        else:
            return []