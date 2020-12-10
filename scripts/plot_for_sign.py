import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb
import numpy as np

def plot_signs(data,path):
    poi_names = list(data.columns[34:45])
    sub = data[poi_names+['Severity']]
    for s in range(1,5):
        x = sub[sub['Severity']==s]
        d = x.sum()[:-1]
        plt.figure(figsize=(15,10))
        plt.bar(poi_names, d/np.sum(d))
        plt.title('Severity: '+str(s))
        plt.figure(figsize=(15,10))
        plt.pie(d/np.sum(d),labels=poi_names)
        plt.title('Severity: '+str(s))
        plt.legend(loc='best')
        plt.savefig(path+'_'+str(s)+'.png',transparent = True)
        
        