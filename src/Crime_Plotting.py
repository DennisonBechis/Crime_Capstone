import pandas as pd
import numpy as np
from Data_cleaning import *
from matplotlib import pyplot as plt
from Plot_Functions import *
from Folium_Graphing import *

if __name__=="__main__":

    # DF_Copies

    crime_df = pd.read_csv('../data/Crime.csv')

    # Adding columns to df

    crime_df['Year'] = crime_df.apply(lambda x: x['REPORTDATE'][2:4], axis=1)
    crime_df['Month'] = crime_df.apply(lambda x: x['REPORTDATE'][5:7], axis=1)
    crime_df['Key'] = crime_df.apply(lambda row: assign_key_values(row[6]), axis=1)
    crime_df['Tally'] = 1

    # Group By Year

    crime_by_year = crime_df.groupby(crime_df['Year']).agg({'Tally':'sum'}).reset_index()
    year_labels = crime_by_year['Year'].to_numpy()
    total = crime_by_year['Tally'].to_numpy()
    fig1 = plt.figure(figsize=(6,6))
    ax1 = fig1.add_subplot(1,1,1)
    bar_plot(ax1, year_labels, total, 'Year', 'Accidents', color = 'red')

    # Grouping by Month/Year

    crime_by_year_month = crime_df.groupby(['Year','Month']).agg({'Tally':'sum'}).reset_index()
    year_month = crime_by_year_month['Month'].to_numpy()
    total_month = crime_by_year_month['Tally'].to_numpy()
    labels = ['' for x in range(0,len(year_month))]
    fig2 = plt.figure(figsize=(6,6))
    ax2 = fig2.add_subplot(1,1,1)
    bar_plot(ax2, labels, total_month, 'Month', 'Offenses', color = 'red')

    # Grouping by Crime_df / Month

    crime_by_offense_month = crime_df.groupby(['Month','OFFENSE']).agg({'Tally':'sum'}).reset_index()

    # Grouping by Month

    crime_by_month = crime_df.groupby(['Month']).agg({'Tally':'sum'}).reset_index()
    fig3 = plt.figure(figsize=(6,6))
    ax3 = fig3.add_subplot(1,1,1)
    total_offenses_by_month = crime_by_month['Tally'].to_numpy()
    labels = crime_by_month['Month'].to_numpy()
    bar_plot(ax3, labels, total_offenses_by_month, 'Months', 'Offenses', color = 'red')

    # Highest Crimes in Boulder

    crimes_total_offenses = crime_df.groupby(['OFFENSE']).agg({'Tally':'sum'}).reset_index()
    crimes_total_offenses = crimes_total_offenses.sort_values(by=['Tally'], ascending=True)
    labels = crimes_total_offenses['OFFENSE'].to_numpy()
    values = crimes_total_offenses['Tally'].to_numpy()
    fig4 = plt.figure(figsize=(6,6))
    ax4 = fig4.add_subplot(1,1,1)
    horizontal_bar(ax4, labels, values, 'Occurrences', 'Offense', 'Boulder Offenses')

    # New DF with top 6 Offenses

    list_of_offenses = ['Vandalism','Trespassing','Theft From Vehicle', 'Sex Assault', 'Burglary', 'Auto Theft', 'Assault']

    # Generating Folium Heat_Maps

    month_list = ['01','02','03','04','05','06','07','08','09','10','11','12']
    for x in range(0,12):
        heat_map_df = crime_df[crime_df['Month'] == month_list[x]]
        heat_map_folium = Create_folium_map(heat_map_df, 'Y','X')
        longitude = heat_map_df['X'].to_numpy()
        latitude = heat_map_df['Y'].to_numpy()
        name = 'Heatmap' + str(x)
        data = []
        for x in range(0, len(latitude)):
            data.append([latitude[x],longitude[x]])
        folium_crime_heatmap(heat_map_folium, name, data)

    # KDE plot Crime vs Month

    # kde_plot(crime_df['Key'], crime_df['Month'], 'Offense_key', 'Month', 'Offense_density')

    # Generating tally for each OFFENSE in Boulder


    crime_df = clean_report_dates(crime_df, 'REPORTDATE')
    crime_df['Day'] = crime_df.apply(lambda x: x['REPORTDATE'].dayofweek, axis=1)
    crime_df['Season'] = crime_df.apply(lambda row: assign_season_values(row[8]), axis=1)
    crime_df_season_day = crime_df.groupby(['Season','Day']).agg({'Tally':'sum'}).reset_index()

    crime_df_fall = crime_df_season_day[crime_df_season_day['Season'] == 'fall']
    crime_df_spring = crime_df_season_day[crime_df_season_day['Season'] == 'spring']
    crime_df_summer = crime_df_season_day[crime_df_season_day['Season'] == 'summer']
    crime_df_winter = crime_df_season_day[crime_df_season_day['Season'] == 'winter']

    fig5 = plt.figure(figsize=(6,6))
    ax5 = fig5.add_subplot(1,1,1)

    line_plot(ax5, crime_df_fall['Day'].to_numpy(), crime_df_fall['Tally'].to_numpy())
    line_plot(ax5, crime_df_spring['Day'].to_numpy(), crime_df_spring['Tally'].to_numpy())
    line_plot(ax5, crime_df_summer['Day'].to_numpy(), crime_df_summer['Tally'].to_numpy())
    line_plot(ax5, crime_df_winter['Day'].to_numpy(), crime_df_winter['Tally'].to_numpy())
    plt.show()






    # kde_plot(crimes_total_offenses_day['Day'], crimes_total_offenses_day['Tally'])
    # plt.show()
