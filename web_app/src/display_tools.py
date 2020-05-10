import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import ImageMagickFileWriter

def init_writer(map_size):
    
    metadata = dict(title='Natural selection', artist='Matplotlib', comment='')
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

    
def png_display(herbivores, carnivores, plantes, filename, map_size):

    fig = plt.figure(figsize=(8,8))
    
    ax = fig.gca()
    ax.set_xticks(np.arange(0, map_size[0]+1, 1))
    ax.set_yticks(np.arange(0, map_size[1]+1, 1))
    plt.grid()
    
    plt.xlim(0, map_size[0])
    plt.ylim(0, map_size[1])
    
    hX, hY = herbivores.get_coords()
    cX, cY = carnivores.get_coords()
    pX, pY = plantes.get_coords()

    plt.plot(cX, cY,color='firebrick',marker="o",linestyle="",markersize=20)
    plt.plot(hX, hY,color='dodgerblue',marker="o",linestyle="",markersize=20)
    plt.plot(pX, pY,color='green',marker="D",linestyle="",markersize=10)
    
    try:
        plt.savefig(filename, dpi=70)
        plt.close()
    except Exception as e:
        print(e, file=sys.stderr)

def png_display_demographie(herbivores, carnivores, plantes,filename):
    
    fig = plt.figure(figsize=(10, 6))
    host = fig.add_subplot(111)
    par1 = host.twinx()
    par2 = host.twinx()
    host.set_xlabel("iterations")
    host.set_ylabel("herbivores")
    par1.set_ylabel("carnivores")
    par2.set_ylabel("plantes")
    
    p1, = host.plot(herbivores.demographie, color = 'dodgerblue', label = "herbivores")
    p2, = par1.plot(carnivores.demographie, color = 'firebrick', label = "carnivores")
    p3, = par2.plot(plantes.demographie, color = 'green', label = "plantes")

    lns = [p1, p2, p3]
    plt.title("Démographies")
    host.legend(handles = lns, loc = 'upper left')
    # right, left, top, bottom
    par2.spines['right'].set_position(('outward', 60))      
    # no x-ticks                 
    #par2.xaxis.set_ticks([])
    # Sometimes handy, same for xaxis
    #par2.yaxis.set_ticks_position('right')
    host.yaxis.label.set_color(p1.get_color())
    par1.yaxis.label.set_color(p2.get_color())
    par2.yaxis.label.set_color(p3.get_color())
    #################################

    # plt.figure(figsize=(10, 6))
    # plt.plot((np.log10(np.array(plantes.demographie) + 1) / (np.array(herbivores.demographie) + 1)), 'orange')
    # plt.title("Log10 plants/herbivore")
    #plt.show()
    
    try:
        plt.savefig(filename, dpi=70)
        plt.close()
    except Exception as e:
        print(e, file=sys.stderr)