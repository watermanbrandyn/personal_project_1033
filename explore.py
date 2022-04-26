# Dataframe and numeric manipulations
import pandas as pd
import numpy as np

# Visualizations
import matplotlib.pyplot as plt
import seaborn as sns

def overall_viz(df, y):
    '''
    
    '''
    plt.figure(figsize=(13,6))
    plt.ylabel('Total Value $')
    plt.title('Total Acquisitions')
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    y.plot()
    plt.show()


def clearer_viz(df, y):
    '''
    
    '''
    plt.figure(figsize=(13,6))
    plt.ylabel('Total Value $')
    plt.title('Total Acquisition')
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    y.resample('Y').sum().plot()
    plt.show()
