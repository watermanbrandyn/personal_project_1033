# Dataframe and numeric manipulations
import pandas as pd
import numpy as np

# Visualizations
import matplotlib.pyplot as plt
import seaborn as sns

# Stats
import scipy.stats as stats


def yearly_viz(df, y):
    '''
    This produces an output visualization for the summed yearly acquisition in total_value for equipment. 
    '''
    plt.figure(figsize=(13,6))
    plt.ylabel('Total Value $')
    plt.title('Total Acquisition By Year')
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    y.resample('Y').sum().plot()
    plt.show()


def quantity_viz(df):
    '''
    This produces an output visualization for the summed yearly acquisition in Quantity for equipment. 
    '''
    y = df.Quantity
    plt.figure(figsize=(13,6))
    plt.ylabel('Total Quantity')
    plt.title('Total Acquisition By Year')
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    y.resample('Y').sum().plot()


def top_three(df):
    '''
    This outputs visualizations for the top three states (TX, CA, TN) in terms of total_value of acquisitions. It produces a daily resampling visual.
    '''
    y_t = df.total_value[df.State == 'TX']
    plt.figure(figsize=(9,5))
    plt.ylabel('Total Value $')
    plt.title('Total Acquisition By Year (TX)')
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    y_t.resample('D').sum().plot()
    plt.show()

    y_c = df.total_value[df.State == 'CA']
    plt.figure(figsize=(9,5))
    plt.ylabel('Total Value $')
    plt.title('Total Acquisition By Year (CA)')
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    y_c.resample('D').sum().plot()
    plt.show()

    y_tn = df.total_value[df.State == 'TN']
    plt.figure(figsize=(9,5))
    plt.ylabel('Total Value $')
    plt.title('Total Acquisition By Year (TN)')
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    y_tn.resample('D').sum().plot()
    plt.show()

def overlap_viz(df):
    '''
    This produces a visualization of the overlap for the top 150 purchases from each State/Region based on acquisition total_value. 
    The peak dictionary contains the top 150 largest purchases (by total_value) by each State/Region.
    '''
    peak = {}
    locales = df.State.unique()
    for x in locales:
        y = df.total_value[df.State == x]
        peak.update({x: y.nlargest(150)})
    
    for p in peak:
        plt.title('Overlap of Largest 150 Acquisitions')
        plt.ylabel('Acquisition Value $')
        plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
        peak[p].plot()


def ttest_by_State(df):
    '''
    This function conducts a One-Sample one-tailed t-test for the average acquisition value for every State/Region. It outputs a print statement
    for each State/Region that is proven statistically significant. 
    '''
    locales = df.State.unique()
    alpha = .05
    df_mean = df.total_value.mean()
    print(f'The average acquisition by total_value: {df_mean}\n')
    for x in locales:
        # H0: The mean of x acquisitions = the mean of all acquisitions.
        # HA: The mean of x acquisitions > the mean of all acquisitions. 
        x_set = df.total_value[df.State == x]
        t, p = stats.ttest_1samp(x_set, df_mean)
        if p/2 > alpha:
            reject = False
        elif t < 0:
            reject = False
        else:
            reject = True

        if reject:
            print(f'We reject the null hypothesis. {x} mean of acquisitions is > than the mean of all acquisitions.')

    
