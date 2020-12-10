import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb
import numpy as np
import calendar
def plot_month(data,path):
    data['Start_Time']=pd.to_datetime(data['Start_Time'])
    fig, ax = plt.subplots(2, 2,figsize = (16,9))
    fig.subplots_adjust(wspace =0.2, hspace =0.35)
    for i, row in enumerate(ax):
        for j, col in enumerate(row):
            data_temp = data[data["Severity"] == (j+1)+2*(i)]
            value_time=data_temp[(data_temp['Start_Time'] > '2017-1-1 00:00:00') & (data_temp['Start_Time'] <= '2020-1-1 00:00:00')]['Start_Time'].values
            col.hist(pd.DatetimeIndex(value_time).month,bins=[1,2,3,4,5,6,7,8,9,10,11,12,13],rwidth=0.8,align = 'left')

            
            col.set_xlabel('Month')
            col.set_ylabel('Accidents')
            col.set_xticks(np.arange(1,13))
            col.set_title('Severity '+str((j+1)+2*(i))+ ' Accidents by Month 2017-2020')
            col.set_xticklabels(calendar.month_abbr[1:13])
    plt.figure()
    value_time=data[(data['Start_Time'] > '2017-1-1 00:00:00') & (data['Start_Time'] <= '2020-1-1 00:00:00')]['Start_Time'].values
    fig, ax= plt.subplots()

    plt.hist(pd.DatetimeIndex(value_time).month,bins=[1,2,3,4,5,6,7,8,9,10,11,12,13],rwidth=0.8,align = 'left')
    ax.set_xticks(np.arange(13))
    ax.set_xticklabels(calendar.month_abbr[0:13])
    plt.title('Accidents by Month 2017-2020')
    plt.xlabel('Month')
    plt.ylabel('Accidents')

    plt.savefig(path, transparent=True)
    plt.figure()
  
def plot_week(data,path):
    data['Start_Time']=pd.to_datetime(data['Start_Time'])
    xticks = [i for i in range(7)]
    xtick_labels = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    fig, ax = plt.subplots(2, 2,figsize = (16,9))
    fig.subplots_adjust(wspace =0.2, hspace =0.35)
    for i, row in enumerate(ax):
        for j, col in enumerate(row):
            data_temp = data[data["Severity"] == (j+1)+2*(i)]
            value_time = data_temp['Start_Time'].values            
            col.hist(pd.DatetimeIndex(value_time).dayofweek,bins=[0,1,2,3,4,5,6,7],rwidth=0.8,align = 'left')        
            col.set_xlabel('Weekday')
            col.set_ylabel('Accidents')
            col.set_xticks(xticks)
            col.set_xticklabels(xtick_labels)
            col.set_title('Severity '+str((j+1)+2*(i))+ ' Accidents by Day of Week')
    plt.figure() 
    
    value_time = data['Start_Time'].values
    fig, ax = plt.subplots()
    
    plt.hist(pd.DatetimeIndex(value_time).dayofweek,bins=[0,1,2,3,4,5,6,7],rwidth=0.8,align = 'left')

    ax.set_xticks(xticks)
    ax.set_xticklabels(xtick_labels)
    plt.title('Accidents by Day of Week')
    plt.xlabel('Weekday')
    plt.ylabel('Accidents')
    plt.savefig(path, transparent=True)
    plt.figure()

def plot_day(data,path):
    xticks = [i for i in range(24)]
    fig, ax = plt.subplots(2, 2,figsize = (16,9))
    fig.subplots_adjust(wspace =0.2, hspace =0.35)
    for i, row in enumerate(ax):
        for j, col in enumerate(row):
            data_temp = data[data["Severity"] == (j+1)+2*(i)]
            value_time = data_temp['Start_Time'].values            

            col.hist(pd.DatetimeIndex(value_time).hour,bins=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],rwidth=0.8,align = 'left')
            col.set_xlabel('Hour of Day')
            col.set_ylabel('Accidents')
            col.set_xticks(xticks)
            col.set_title('Severity '+str((j+1)+2*(i))+ ' Accidents Occurances by Hour')
    plt.figure()
    
    value_time = data['Start_Time'].values
    fig, ax = plt.subplots()

    plt.hist(pd.DatetimeIndex(value_time).hour,bins=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],rwidth=0.8,align = 'left')

    ax.set_xticks(xticks)
    plt.title('Accident Occurances by Hour' )
    plt.xlabel('Hour of Day')
    plt.ylabel('Accident')
    plt.savefig(path, transparent=True)
    plt.figure()