import time
import random
import sys
import os

from src.display_tools import png_display, png_display_demographie
from src.population import population
# from src.individus import individus
from src.especes import espece_herbivore, espece_plante, espece_carnivore


class SimulationError(Exception):
    pass


class Simulation(object):
    """
        WIP : faire classe simulation mere et classes filles de types de simu
        Wrapper class to handle a whole simulation
    """
    
    def __init__(self, map_size):
        self.map_size = map_size
        self.n_iter = 0
        self.n_iter_max = 10 #5000 
        self.list_pictures = []
        
        # population objects initialisation
        self.herbivores = population(nombre_individus=10, map_size = self.map_size, espece = espece_herbivore)
        self.plantes = population(nombre_individus = 10, map_size = self.map_size, espece = espece_plante)
        self.carnivores = population(nombre_individus = 5, map_size = self.map_size, espece = espece_carnivore)
        

    def next_iteration(self):
        # random generation
        self.plantes.reproduce()
        self.plantes.generate(0.5, espece_plante)

        # food
        self.carnivores.search_food(self.herbivores)
        self.carnivores.reproduce()
        self.carnivores.deplacement()
        self.carnivores.starve()
        self.carnivores.search_food(self.herbivores)
        #carnivores.generate(0.02, espece_carnivore)
        self.herbivores.search_food(self.plantes)
        self.herbivores.reproduce()
        self.herbivores.deplacement()
        self.herbivores.starve()
        #herbivores.generate(0.08, espece_herbivore)

        # collect stats
        self.plantes.demographie.append(self.plantes.nombre_individus)
        self.carnivores.demographie.append(self.carnivores.nombre_individus)
        self.herbivores.demographie.append(self.herbivores.nombre_individus)

        # simulation safety
        if self.plantes.nombre_individus>400:
            raise SimulationError("Too many entities")
        if self.carnivores.nombre_individus==0:
            raise SimulationError("Not enough entities")
    
    def delete(self):
        """WIP delete all pictures in self.list_pictures."""
        pass
    
    def display(self,filename=None):
        # WIP : to change
        print("function display called", file=sys.stderr)
        if filename is None:
            filename = f'./simulation_pict_{random.randint(0,1e5)}.png'
        png_display(self.herbivores, self.carnivores, self.plantes,filename, self.map_size)
        self.list_pictures.append(filename)
        return filename
    
    def display_demographic(self,filename=None):
        print("function display_demographic called", file=sys.stderr)
        if filename is None:
            filename = f'./simulation_pict_{random.randint(0,1e5)}.png'
        png_display_demographie(self.herbivores, self.carnivores, self.plantes,filename)
        self.list_pictures.append(filename)
        return filename
    
    def run_whole_simulation(self):
        for i in range(self.n_iter_max):
            self.next_iteration()
        return None
            
if __name__=="__main__":
    
    # global parameters
    map_size = [40,40]
    
    # define & run & display & delete simulation
    simu = Simulation( map_size = map_size, file = sys.stdout)
    simu.run_whole_simulation()
    picture_path = simu.display()
    simu.delete()
    
    print(f"Display picture generated: {picture_path}")