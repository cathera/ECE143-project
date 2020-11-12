import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import folium
from folium.plugins import HeatMap
data = pd.read_csv('data/US_Accidents_June20.csv')
data = data[data['State']=='CA']

# show the Severity 4 to reduce load time
data = data.loc[data["Severity"] == 3]

x = data.Start_Lat.values.astype(np.float64)
y = data.Start_Lng.values.astype(np.float64)
data['count'] = 1
incidents = folium.map.FeatureGroup()
san_map = folium.Map(location = [36.7783,-119.4179],zoom_start=6)
# for lat, lng, in zip(x, y):
#     incidents.add_child(
#         folium.CircleMarker(
#             [lat, lng],
#             radius=7, # define how big you want the circle markers to be
#             color='yellow',
#             fill=True,
#             fill_color='red',
#             fill_opacity=0.4
#         )
#     )
HeatMap(data=data[['Start_Lat', 'Start_Lng', 'count']].groupby(['Start_Lat', 'Start_Lng']).sum().reset_index().values.tolist(), radius=8, max_zoom=13).add_to(san_map)

# san_map.add_child(incidents)
san_map.save('Severity3.html')
