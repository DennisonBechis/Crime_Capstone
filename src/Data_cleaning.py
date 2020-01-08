import pandas as pd
import numpy as np

def clean_report_dates(dataframe , date_column):
    """
    # cleans and formats date correctly
    # dataframe - dataframe (DATAFRAME)
    # date_column - Name of date column (STRING)
    # returns date column as datetime64[ns]
    """

    dataframe['REPORTDATE'] = dataframe.apply(lambda x: x['REPORTDATE'][0:10], axis=1)
    dataframe['REPORTDATE'] = pd.to_datetime(dataframe['REPORTDATE'])
    return dataframe

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

def assign_season_values(months):
    winter = [12,1,2]
    spring = [3,4,5]
    summer = [6,7,8]
    fall = [9,10,11]

    if int(months) in winter:
        return 'winter'
    elif int(months) in spring:
        return 'spring'
    elif int(months) in summer:
        return 'summer'
    elif int(months) in fall:
        return 'fall'
