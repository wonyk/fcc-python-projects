import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', header=0)

    # Create scatter plot
    df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level', title='Rise in Sea Level', xlabel='Year', ylabel='Sea Level (inches)')

    # Create first line of best fit
    bfline1 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    xlist = []
    ylist = []
    for i in range(1880, 2051):
        xlist.append(i)
        ylist.append(i * bfline1.slope + bfline1.intercept)
    # Plot a red line
    plt.plot(xlist, ylist, 'r-', label='From year 1880')

    # Create second line of best fit
    df_new = df[df['Year'] >= 2000]
    bfline2 = linregress(x=df_new['Year'], y=df_new['CSIRO Adjusted Sea Level'])
    xlist2 = []
    ylist2 = []
    for i in range(2000, 2051):
        xlist2.append(i)
        ylist2.append(i * bfline2.slope + bfline2.intercept)
    # Plot red dashed line
    plt.plot(xlist2, ylist2, 'r--', label='From year 2000')
    plt.legend(loc='best')
   
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()