from scipy.spatial.distance import squareform
import numpy as np
import matplotlib.pyplot as plt


n_data=100



with open("cc.dat",'r')as f:
    lines = f.readlines()


cc_list=[]

for line in lines:
    cc_list.append(float(line.strip()))


sample_list=[]

n_half = int(n_data/2)
for i in np.arange(0,n_half):
    sample_list.append("x")
for i in np.arange(0,n_half):
    sample_list.append("y")


squ = squareform(cc_list)

def draw_heatmap(data, labels):
    fig, ax = plt.subplots(figsize=(5,5))
#    heatmap = ax.pcolor(data, cmap=plt.cm.Blues)
    heatmap = ax.pcolor(data,cmap='Reds',vmax=1.0)

    ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)

    ax.invert_yaxis()
    ax.xaxis.tick_top()

    ax.set_xticklabels(labels,rotation=90, minor=False)
    ax.set_yticklabels(labels, minor=False)
    ax.set_title('heatmap conform')
    fig.colorbar(heatmap, ax=ax,label='colorbar label')
    plt.savefig('image.png')
    plt.show()

    return heatmap

draw_heatmap(squ,sample_list)

