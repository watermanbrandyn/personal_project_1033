import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

def rfm_df(df):
    '''
    This function takes in our original df and returns a rfm_df that calculated RFM metrics, assigns rankings, and then segments the Agencies by their
    combined rankings. The weights for the rankings are .15 for Recency, .28 for Frequency, and .57 for Monetary (total_value) metrics. 
    '''
    # Calculating Recency
    df_recency = df.groupby(by='Agency_Name', as_index=False)['Ship_Date'].max()
    df_recency.columns = ['Agency_Name', 'LastPurchaseDate']
    recent_date = df_recency['LastPurchaseDate'].max()
    df_recency['Recency'] = df_recency['LastPurchaseDate'].apply(lambda x: (recent_date - x).days)
    # Calculating Frequency
    frequency_df = df.drop_duplicates().groupby(by=['Agency_Name'], as_index=False)['Ship_Date'].count()
    frequency_df.columns = ['Agency_Name', 'Frequency'] 
    # Calculating Monetary Value
    df['Total'] = df['total_value']
    monetary_df = df.groupby(by='Agency_Name', as_index=False)['Total'].sum()
    monetary_df.columns = ['Agency_Name', 'Monetary']
    # Merging the three dataframes
    rf_df = df_recency.merge(frequency_df, on='Agency_Name')
    rfm_df = rf_df.merge(monetary_df, on='Agency_Name').drop(columns='LastPurchaseDate')
    
    # Assigning ranks based on 'stats'
    rfm_df['R_rank'] = rfm_df['Recency'].rank(ascending=False)
    rfm_df['F_rank'] = rfm_df['Frequency'].rank(ascending=True)
    rfm_df['M_rank'] = rfm_df['Monetary'].rank(ascending=True)

    # normalizing the rank of the 'customers'
    rfm_df['R_rank_norm'] = (rfm_df['R_rank']/rfm_df['R_rank'].max())*100
    rfm_df['F_rank_norm'] = (rfm_df['F_rank']/rfm_df['F_rank'].max())*100
    rfm_df['M_rank_norm'] = (rfm_df['F_rank']/rfm_df['M_rank'].max())*100

    rfm_df.drop(columns=['R_rank', 'F_rank', 'M_rank'], inplace=True)

    # Calculating RFM score
    rfm_df['RFM_Score'] = .15 *rfm_df['R_rank_norm'] + .28 * rfm_df['F_rank_norm'] + .57 * rfm_df['M_rank_norm']
    rfm_df['RFM_Score'] *= .05
    rfm_df = rfm_df.round(2)

    # Rating customers bsaed on RFM Score
    rfm_df['Agency_Segment'] = np.where(rfm_df['RFM_Score'] > 4.5, "Top User", 
                                    (np.where(rfm_df['RFM_Score'] > 4, "High Use", 
                                             (np.where(rfm_df['RFM_Score'] > 3, "Medium Use",
                                                      (np.where(rfm_df['RFM_Score'] > 1.6, "Low Use", "Lowest Use")))))))

    # Creating a dictionary to map to rfm_df to incorporate the State column from df
    agency_dict = dict (zip(df['Agency_Name'], df['State']))
    # Maping the dictionary to a new 'State' column in the rfm_df
    rfm_df['State'] = rfm_df['Agency_Name'].map(agency_dict)

    # Return the rfm_df
    return rfm_df


def rfm_pie(rfm_df):
    plt.pie(rfm_df.Agency_Segment.value_counts(),
       labels=rfm_df.Agency_Segment.value_counts().index,
       autopct='%.0f%%')
    plt.show()