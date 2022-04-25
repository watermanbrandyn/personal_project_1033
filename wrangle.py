import pandas as pd
import numpy as np

def wrangle_1033():
    '''
    This function takes our 1033 data and creates a dataframe to then prepare.
    It fills the Nulls, corrects datatypes, sets index to the Ship_Date, and creates
    a better representation of total assets given away with the 'total_value' column.
    '''
    # Read the local csv to a dataframe
    df = pd.read_csv('dod_all_states.csv')
    # Change spacing in columns for ease of use
    df.columns = df.columns.str.replace(' ','_')
    # Filling NaN for DEMIL_IC columns
    df.DEMIL_IC = df.DEMIL_IC.fillna(1)
    # Changing Ship_Date to datetime format and setting as index
    df.Ship_Date = pd.to_datetime(df.Ship_Date)
    df = df.set_index(df.Ship_Date)
    df = df.sort_index()
    # changing DEMIL_IC to proper datetype
    df.DEMIL_IC = df.DEMIL_IC.astype(int)
    df.DEMIL_IC = df.DEMIL_IC.astype(object)
    # Feature engineering 'total_value' column to better represent acquisition values
    df['total_value'] = df.Quantity * df.Acquisition_Value
    # Dropping 'Station_Type' column, deemed unnecessary
    df = df.drop(columns='Station_Type')
    # Dropping the first row in the dataframe from 1980
    df = df.iloc[1:, :]
    # Return the df
    return df