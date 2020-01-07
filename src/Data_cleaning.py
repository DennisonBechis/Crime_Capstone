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




if __name__ == "__main__":
    df = pd.read_csv('../data/Crime.csv')
    a = clean_report_dates(df, 'REPORTDATE')
    print(a['REPORTDATE'])
    a.info()
