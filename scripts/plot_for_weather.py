import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb
import numpy as np

def plot_tem(data, path):
    for s in range(1, 5):
        t = data[data.Severity == s]['Temperature(F)'].values
        # Clip for better visualization
        t = t[np.isnan(t) == False]
        print('Temperature mean: ' + str(t.mean()))
        plt.figure()
        sb.distplot(t, kde=False, norm_hist=True)
        plt.title('Severity: ' + str(s))
        plt.yticks(np.linspace(0, 0.1, 11))
        plt.xlim(0, 100)
        
        plt.savefig(path+'Severity'+str(s)+'.png', format='png',transparent = True)
        plt.show()
        
        plt.close()



def plot_visibility(data,path):
    sevlist = []
    for s in range(1, 5):
        value_vis2 = data.loc[data["Severity"] == s]['Visibility(mi)'].values
        sevlist.append(np.histogram(value_vis2, bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))

    scaledsum = np.zeros(11)  # count of accidents * severity level
    acount = np.zeros(11)  # count of accidents used for calucations
    prob = [np.zeros(11), np.zeros(11), np.zeros(11), np.zeros(11)]
    ex = [np.zeros(11), np.zeros(11), np.zeros(11), np.zeros(11)]
    ex_squared = [np.zeros(11), np.zeros(11), np.zeros(11), np.zeros(11)]
    expected_v_squared = [np.zeros(11), np.zeros(11), np.zeros(11), np.zeros(11)]
    expected_v = np.zeros(4)
    variance = np.zeros(4)
    for i in range(4):
        for j in range(11):
            scaledsum[j] = scaledsum[j] + sevlist[i][0][j] * (i + 1)
            acount[j] += sevlist[i][0][j]
            prob[i][j] = (sevlist[i][0][j]) / np.sum(sevlist[i][0])
            ex[i][j] = prob[i][j] * sevlist[i][1][j]
            ex_squared[i][j] = (prob[i][j]) * (sevlist[i][1][j] ** 2)
        expected_v[i] = np.sum(ex[i])
        expected_v_squared[i] = np.sum(ex_squared[i])
        variance[i] = expected_v_squared[i] - expected_v[i] ** 2
        plt.bar(list(range(0, 11)), prob[i])
        plt.title('Severity: ' + str(i + 1) + '\nExpected Visibility: E(x)= ' + str(
            expected_v[i].round(2)) + '\nVariance: Var(x)= ' + str(variance[i].round(2)))
        plt.xlabel('Visibility')
        plt.ylabel('P(Visibility | Accident Occurs)')
        plt.figure()

    expected_severity = np.zeros(11)
    for i in range(11):
        expected_severity[i] = scaledsum[i] / acount[i]
    # print(expected_severity)
    # print(prob[1])
    plt.figure()
    plt.bar(list(range(0, 11)), expected_severity)
    plt.title('Expected Accident Severity Given Visibility')
    plt.xlabel('Visibility')
    plt.ylabel('Expected Accident Severity')
    plt.ylim(2, 3)
    plt.savefig(path,format='png',transparent = True)
    plt.show()

    plt.close()
    


