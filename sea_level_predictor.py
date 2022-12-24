import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x,y)

    # Create first line of best fit
    li_res = linregress(x,y)
    x_predict = pd.Series([i for i in range(1880,2051)])
    y_predict = li_res.slope * x_predict + li_res.intercept
    plt.plot(x_predict,y_predict,'r')

    # Create second line of best fit
    new_df = df.loc[df["Year"]>=2000]
    x_2 = new_df["Year"]
    y_2 = new_df["CSIRO Adjusted Sea Level"]
    li_res2 = linregress(x_2, y_2)
    x_2_pred = pd.Series([i for i in range(2000,2051)])
    y_2_pred = li_res2.slope*x_2_pred + li_res2.intercept
    plt.plot(x_2_pred,y_2_pred,"purple")


    # Add labels and title
    ax.set_ylabel("Sea Level (Inches)")
    ax.set_xlabel("Year")
    ax.set_title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()