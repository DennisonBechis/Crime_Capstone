import folium
from folium.plugins import MarkerCluster
from folium.plugins import HeatMap
from folium.map import Layer

def folium_crime_heatmap(map_object, save_name, data, zoom_start=12, min_opacity=0.3):

    '''
        Inputs:
            map_object  : Initialized map object
            save_name   : File name for HeatMap
            data        : List of lists [ [latitudes_list], [longitudes_list] ]
            min_opacity : Heat color opacity
    '''

    auto_play = True
    max_zoom = 1
    radius = 11
    min_opacity = 0.3

    HeatMap(data, min_opacity=min_opacity,
                   max_val=float(60),
                   radius=radius,
                   max_zoom=max_zoom ).add_to(map_object)

    return map_object.save( '../images/'+ save_name + '.html')

def Create_folium_map(dataframe, latitude_name, longitude_name, zoom_start = 13):

    '''
        Inputs:
            dataframe       : Pandas dataframe
            latitude_name   : Column name containing latitudes
            longitude_name  : Column name containing longitude
            zoom_start      : Starting Zoom position on map
    '''

    return folium.Map(location = [dataframe[latitude_name].mean(), dataframe[longitude_name].mean()], zoom_start=zoom_start)
