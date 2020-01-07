import pandas as pd
import folium
from folium.plugins import MarkerCluster
from folium.plugins import HeatMap
from folium.map import Layer

def folium_crime_heatmap(map_object, save_name, data,
                 zoom_start=12,
                 min_opacity=0.2, radius=9,
                 max_zoom=1, auto_play=True):

    HeatMap(data, min_opacity=min_opacity,
                   max_val=float(60),
                   radius=radius,
                   max_zoom=max_zoom ).add_to(map_object)

    return map_object.save( '../images/'+ save_name + '.html')

def Create_folium_map(dataframe, lat_name, long_name, zoom_start = 13):

    return folium.Map(location = [df[lat_name].mean(), df[long_name].mean()], zoom_start=zoom_start)


if __name__== '__main__':

    df = pd.read_csv('../data/Crime.csv')

    longitude = df['X'].to_numpy()
    latitude = df['Y'].to_numpy()

    m = Create_folium_map(df, 'Y','X')

    data = []
    for x in range(0, len(latitude)):
        data.append([latitude[x],longitude[x]])

    folium_crime_heatmap(m, 'Heat_Map', data)
