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

    offense_dictionary = {'Vandalism': 1, 'Sex Assault':2, 'Trespassing':3, 'Burglary':4,
                          'Theft From Vehicle':5,'Assault':6, 'Incident':7, 'Auto Theft':8}

    if offense in offense_dictionary.keys():
        return offense_dictionary[offense]
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
