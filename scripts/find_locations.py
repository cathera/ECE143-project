import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from geopy import distance


class Location(object):
    def __init__(self,a,b):
        """
        class to act as a location node 
        :a: float
        :b: float
        """
        self._lat=a
        self._lon=b
        self._neighbors=[]
        
    def add_neighbor(self, other):
        assert isinstance(other, Location)
        if other not in self._neighbors:
            self._neighbors.append((other))
        if self not in other._neighbors:
            other.add_neighbor(self)
    def get_neighbors(self):
        return int(len(self._neighbors))
    def get_neighbors_list(self):
        return self._neighbors
    def get_coords(self):
        return ((self._lat), (self._lon))

def find_most_accidents(data,d): 
    '''
    Function that finds coordinates with most accidents within d distance of data set
    param data: dataframe to use
    type data: pandas.dataframe
    param d: distance in yards to use at radius
    type d: int  

    ''' 
    assert isinstance(data,pd.DataFrame) and isinstance(d, int)
    df=data.sort_values(by=['Start_Lat', 'Start_Lng']) #sort coordinate directions to minimize iteration time
    longs=list(df['Start_Lng'].values)
    lats=list(df['Start_Lat'].values)

    ids=df['ID'].values

    locs=[]
    maxneighbors=0 
    indx=0 # used to save index of location with most neighbors

    for i in range(int(len(ids))):# create a location class for each of the 
        lats[i]=round(lats[i],6)
        longs[i]=round(longs[i],6)
        a=Location(lats[i],longs[i])
        locs.append(a)

    for i in range(int(len(ids))):
        for j in range(i+1,int(len(ids))):
            dist=distance.distance((lats[i],longs[i]), (lats[j],longs[j])).km * 1093.61
            if  dist>d: # check if lat distance is greater than 100 yards, if so break this loop to eliminate unneeded computations.
                break
            if dist<=d: # if point to point distance is less than 100 years, add it to that locations neighbor list
                locs[i].add_neighbor(locs[j])
                if locs[i].get_neighbors()>maxneighbors:
                    maxneighbors=locs[i].get_neighbors()
                    indx=i


    print('area with max neighbors of: ',locs[indx].get_neighbors(),' at list index: ',indx,' with coords: ',locs[indx].get_coords())
    return (locs[indx].get_neighbors(),locs[indx].get_coords())