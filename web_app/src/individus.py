# INDIVIDUAL CLASS

import random
import numpy as np

class individus(object):
    def __init__(self,map_size,initial_coordinates=None):
        
        if initial_coordinates:
            self.X = initial_coordinates[0]
            self.Y = initial_coordinates[1]
        else:
            self.X = random.randint(1,(map_size[0]-1)*10.)/10
            self.Y = random.randint(1,(map_size[1]-1)*10.)/10
            
        self.dead_state = False
    
    def search_food(self,nourriture):
        """
            Look for food
                if food is close : EAT it
                if food is in vision field : redirection towards it
                if none : keep moving in same direction
        """
        
        if (nourriture.nombre_individus > 0):
            food_x,food_y = nourriture.get_coords()

            food_distance = np.sqrt((food_x-self.X)**2+(food_y-self.Y)**2)
            fd_min = np.min(food_distance)

            # eating close food
            if (fd_min <= self.speed):
                index = np.where(food_distance==fd_min)[0][0]

                self.size += nourriture.list_individus[index].nutriment
                del(nourriture.list_individus[index])
                nourriture.nombre_individus -= 1

        if (nourriture.nombre_individus > 0):
            # redirection toward closest food
            if (fd_min <= self.vision):
                index = np.where(food_distance==fd_min)[0][0]
                
                FD = max(1e-5,fd_min)
                self.vec_speed = [self.speed*(food_x[index]-self.X)/FD,self.speed*(food_y[index]-self.Y)/FD]

        # else keep same direction
        return None
    
    def move(self,map_size):
        # acceleration nulle
        a = 0
        # equation du mouvement t=1
        self.X += 0.5*a + self.vec_speed[0]
        self.Y += 0.5*a + self.vec_speed[1]
        
        if (self.X > map_size[0]):
            self.X = map_size[0]
            self.vec_speed[0] = -self.vec_speed[0]
        elif (self.X < 0.):
            self.X = 0.
            self.vec_speed[0] = -self.vec_speed[0]
        
        if (self.Y > map_size[1]):
            self.Y = map_size[1]
            self.vec_speed[1] = -self.vec_speed[1]
        elif (self.Y < 0.):
            self.Y = 0.
            self.vec_speed[1] = -self.vec_speed[1]

        return None
    
    def starve(self):
        """
            Return its alive/dead states
        """
        if (self.size>self.hunger_decay):
            self.size -= self.hunger_decay
        else:
            self.dead_state = True
            
        return self.dead_state