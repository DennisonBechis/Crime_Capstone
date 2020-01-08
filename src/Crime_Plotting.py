import pandas as pd
import numpy as np
from Data_cleaning import clean_report_dates
from matplotlib import pyplot as plt
from Plot_Functions import *
from Folium_Graphing import *

def assign_key_values(offense):
    if offense == 'Vandalism':
        return 1
    elif offense == 'Sex Assault':
        return 2
    elif offense == 'Trespassing':
        return 3
    elif offense == 'Burglary':
        return 4
    elif offense == 'Theft From Vehicle':
        return 5
    elif offense == 'Assault':
        return 6
    elif offense == 'Incident':
        return 7
    elif offense == 'Auto Theft':
        return 8
    else:
        return 0



if __name__=="__main__":

    # DF_Copies

    Crime_df = pd.read_csv('../data/Crime.csv')

    # Adding columns to df

    Crime_df['Year'] = Crime_df.apply(lambda x: x['REPORTDATE'][2:4], axis=1)
    Crime_df['Month'] = Crime_df.apply(lambda x: x['REPORTDATE'][5:7], axis=1)
    Crime_df['Key'] = Crime_df.apply(lambda row: assign_key_values(row[6]), axis=1)
    Crime_df['Tally'] = 1

    # Group By Year

    Crime_by_year = Crime_df.groupby(Crime_df['Year']).agg({'Tally':'sum'}).reset_index()
    Year_labels = Crime_by_year['Year'].to_numpy()
    Total = Crime_by_year['Tally'].to_numpy()
    fig1 = plt.figure(figsize=(6,6))
    ax1 = fig1.add_subplot(1,1,1)
    Bar_plot(ax1, Year_labels, Total, 'Year', 'Accidents', color = 'red')

    # Grouping by Month/Year

    Crime_by_year_month = Crime_df.groupby(['Year','Month']).agg({'Tally':'sum'}).reset_index()
    Year_month = Crime_by_year_month['Month'].to_numpy()
    Total_month = Crime_by_year_month['Tally'].to_numpy()
    labels = ['' for x in range(0,len(Year_month))]
    fig2 = plt.figure(figsize=(6,6))
    ax2 = fig2.add_subplot(1,1,1)
    Bar_plot(ax2, labels, Total_month, 'Month', 'Offenses', color = 'red')

    # Grouping by Crime_df / Month

    Crime_by_offense_month = Crime_df.groupby(['Month','OFFENSE']).agg({'Tally':'sum'}).reset_index()

    # Grouping by Month

    Crime_by_month = Crime_df.groupby(['Month']).agg({'Tally':'sum'}).reset_index()
    fig3 = plt.figure(figsize=(6,6))
    ax3 = fig3.add_subplot(1,1,1)
    Total_offenses_by_month = Crime_by_month['Tally'].to_numpy()
    labels = Crime_by_month['Month'].to_numpy()
    Bar_plot(ax3, labels, Total_offenses_by_month, 'Months', 'Offenses', color = 'red')

    # Highest Crimes in Boulder

    Crimes_total_offenses = Crime_df.groupby(['OFFENSE']).agg({'Tally':'sum'}).reset_index()

    # New DF with top 6 Offenses

    list_of_offenses = ['Vandalism','Trespassing','Theft From Vehicle', 'Sex Assault', 'Burglary', 'Auto Theft', 'Assault']

    # Generating Folium Heat_Maps

    month_list = ['01','02','03','04','05','06','07','08','09','10','11','12']
    for x in range(0,12):
        Heat_map_df = Crime_df[Crime_df['Month'] == month_list[x]]
        Heat_map_folium = Create_folium_map(Heat_map_df, 'Y','X')
        longitude = Heat_map_df['X'].to_numpy()
        latitude = Heat_map_df['Y'].to_numpy()
        name = 'Heatmap' + str(x)
        data = []
        for x in range(0, len(latitude)):
            data.append([latitude[x],longitude[x]])
        folium_crime_heatmap(Heat_map_folium, name, data)
    plt.show()

    # KDE plot Crime vs Month

    # kde_plot(Crime_df['Key'], Crime_df['Month'], 'Offense_key', 'Month', 'Offense_density')
