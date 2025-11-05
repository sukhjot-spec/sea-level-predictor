import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    #Use Pandas to import the data from epa-sea-level.csv.
    df = pd.read_csv('data/epa-sea-level-CLEANED.csv')

    #Using matplotlib to create a scatter plot with the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    #first line of best fit using linregress
    line1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(df['Year'].min(), 2051, 1)
    y1 =  x1*line1.slope + line1.intercept

    plt.plot(x1, y1)

    #Plotting a new line of best fit just using the data from year 2000 through the most recent year in the dataset and Making the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
    df_new = df[df['Year'] >= 2000]

    #second line of best fit using linregress
    line2 = linregress(df_new['Year'], df_new['CSIRO Adjusted Sea Level'])
    x2 = np.arange(2000,2051,1)
    y2 = x2*line2.slope + line2.intercept

    plt.plot(x2, y2)

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    plt.savefig('sea_level_plot.png')
    return plt.gca()