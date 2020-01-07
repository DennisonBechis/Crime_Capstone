import pandas as pd
import numpy as np
from Data_cleaning import clean_report_dates






if __name__=="__main__":
    Crime_df = pd.read_csv('../data/Crime.csv')

    Crime_df_year = Crime_df.copy()
    # Crime_Data = clean_report_dates(df, 'REPORTDATE')

    # Group By Year
    Crime_df_year['Year'] = Crime_df_year.apply(lambda x: int(x['REPORTDATE'][0:4]), axis=1)
    Crime_df_year['Tally'] = 1
    Crime_df_year = Crime_df_year.groupby(Crime_df_year['Year']).agg({'Tally':'sum'}).reset_index()

    Year = Crime_df_year['Year'].to_numpy()
    Total = Crime_df_year['Tally'].to_numpy()

    # newdf_grouped = newdf.groupby(newdf['levels']).agg({'Mean Charge':'mean'}).reset_index()



    print(Crime_df_year)
