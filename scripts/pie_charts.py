import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import altair as alt
from altair import Chart
import seaborn as sns
'''
Code to generate pie_charts
'''
def get_top_n(df,n):
    '''
    Create another Dataframe equivalent to df but only taking top n values,
    all others will be combined under the 'other' label. Best use to increase 
    readability of pie charts. Assumption this is a df of count.

    Parameters
    ----------
    df : pd.Dataframe
        pd.Dataframe with labels and count
    n : int
        number of top labels you want visible

    Returns
    -------
    pd.Dataframe

    '''
    assert isinstance(df,pd.DataFrame)
    assert isinstance(n,int)
    sort_by=df.columns[0]
    df=df.sort_values(sort_by,ascending=False)
    top_df = df[:n].copy()
    other=pd.DataFrame(df[n:].sum(),columns=[sort_by])
    df2=pd.concat([top_df,other])
    ind=df2.index.tolist()
    ind[len(ind)-1]='Other'
    df2.index=ind
    return df2
def get_data(df,column,highlight='',exp=False):
    '''
    Generate the data needed for a pie plot from a dataframe of counts

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe which countains a count column and an index as labels
    column : string
        name of column where the count is located
    highlight : string, optional
        DESCRIPTION. The default is ''. If you want an explode and highlight
        a specific state/county/etc. enter string name here.
    exp : bool, optional
        DESCRIPTION. The default is False. Set to true to explode pie at label==highlight

    Returns
    -------
    labels:list
        list of labels
    vals:list
        list of values for labels
    explode:list
        list of len(labels) with zero entries except for highlight location

    '''
    assert isinstance(df,pd.DataFrame)
    assert isinstance(column,str)
    assert isinstance(highlight,str)
    assert isinstance(exp,bool)
    
    labels=df.index.tolist()
    vals=df[column].tolist()
    if exp:
        assert highlight!=''
        highlight_idx=np.where(np.array(labels)==highlight)
        explode=np.zeros(len(labels))
        explode[highlight_idx]=.1
        return labels,vals,explode
    else:
        return labels,vals

def state_pie(data,path):
    state_count=pd.DataFrame(data.groupby('State')['ID'].count())
    top_state_count=get_top_n(state_count,4)
    state_l,state_v,state_e=get_data(top_state_count,'ID','CA',exp=True)
    fig1, ax1 = plt.subplots()
    ax1.pie(state_v, explode=state_e, labels=state_l, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title('Vehicle Accidents by State')
    plt.savefig(path+ 'State_Pie_Chart.png', transparent=True)
    plt.show()
    
def county_pie(CA_data,path):
    county_count=pd.DataFrame(CA_data.groupby('County')['ID'].count())
    top_county_count=get_top_n(county_count,6)
    county_l,county_v,county_e=get_data(top_county_count,'ID','San Diego',exp=True)
    totalc=sum(county_v)
    fig2, ax2 = plt.subplots()
    ax2.pie(county_v,
        shadow=True, startangle=90, radius=2)
    plt.legend(loc='best',labels=['%s, %1.1f%%' % (l, 100*s/totalc) for l, s in zip(county_l, county_v)])
    ax2.axis('equal')
    plt.title('Vehicle Accidents by County in California')
    plt.savefig(path+ 'County_Pie.png', transparent=True)
    plt.show()

def severity_pie(CA_data,path):
    severity_count=pd.DataFrame(CA_data.groupby('Severity')['ID'].count())
    severity_l,severity_v=get_data(severity_count,'ID')
    total=sum(severity_v)
    fig3, ax3 = plt.subplots()
    ax3.pie(severity_v,
        shadow=True, startangle=90)
    plt.legend(loc='best', labels=['%s, %1.1f%%' % (l, 100*s/total) for l, s in zip(severity_l, severity_v)])
    ax3.axis('equal')
    plt.title('Severity of Accidents')
    plt.savefig(path+ 'Severity_Pie.png', transparent=True)
    plt.show()

