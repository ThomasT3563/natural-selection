import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import ImageMagickFileWriter

def init_writer(map_size):
    
    metadata = dict(title='Natural selection', artist='Matplotlib',comment='')
    writer = ImageMagickFileWriter(fps=7, metadata=metadata)
    
    fig = plt.figure(figsize=(8,8))
    ax = fig.gca()

    ax.set_xticks(np.arange(0, map_size[0]+1, 1))
    ax.set_yticks(np.arange(0, map_size[1]+1, 1))
    plt.grid()
    
    plt.xlim(0, map_size[0])
    plt.ylim(0, map_size[1])

    graph_c, = plt.plot([],[],color='firebrick',marker="o",linestyle="",markersize=20)
    graph_h, = plt.plot([],[],color='dodgerblue',marker="o",linestyle="",markersize=20)
    graph_p, = plt.plot([],[],color='green',marker="D",linestyle="",markersize=10)
    
    #a.set_color('red')
    #a.set_marker
    #a.set_label
    
    return writer,fig,graph_h,graph_p,graph_c
    
    
def update_writer(writer,graph_h,graph_p,graph_c,herbivores,plantes,carnivores):
    
    position_X,position_Y = herbivores.get_coords()
    graph_h.set_data(position_X,position_Y)
    
    position_X,position_Y = carnivores.get_coords()
    graph_c.set_data(position_X,position_Y)
    
    position_X,position_Y = plantes.get_coords()
    graph_p.set_data(position_X,position_Y)
    
    writer.grab_frame()