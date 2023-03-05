#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 00:26:59 2023

@author: tomthomas
"""


import pandas as pd
from matplotlib import pyplot as plt

#This function is helpful for reading in and preprocessing rail revenue data in preparation for further analysis, particularly where the "Time period" column is crucial for examining trends over time.
def readData1():
    #The Excel file is read using the Pandas read excel() function, and the resulting DataFrame is then assigned to the variable data2.
    data2 = pd.read_excel("/Rail Revenue.xlsx")
    #sets the index of the data2 to be the "Time period" column when creating a new DataFrame with the name data2_updated.
    data2_updated=data2.set_index('Time period')
    #to remove the last column from the DataFrame data2_updated
    data2_updated=data2_updated.drop(data2_updated.columns[-1], axis=1)
    #data2 and data2_updated are the two variables that the function returns. Whereas data2_updated has the same DataFrame with the 'Time period' column used as the new index, data2 contains the original DataFrame read in from the Excel file.
    return data2,data2_updated

#creating a two-level pie chart for two time periods.    
def piePlot(data2_updated):
    #Choosing the information and calculating the total revenue for each period
    a = data2_updated.loc['Apr 2020 to Mar 2021']
    b = data2_updated.loc['Apr 2021 to Mar 2022']
    total1 = round(sum(a),2)
    total2 = round(sum(b),2)
    # Create subplots for each time period
    fig, (ax1, ax2) = plt.subplots(2, 1,figsize=(8,10))
    #Creating a pie chart for the years 2021–2022, adding a title and the total value.
    ax1.pie(data2_updated.loc['Apr 2021 to Mar 2022'], labels=data2_updated.columns, autopct='%1.1f%%', colors=['red', 'green', 'blue', 'purple','orange'])
    ax1.set_title('Great Britain, 2020–2021, proportion of passenger revenue by ticket type',fontweight='bold')
    ax1.text(0, 0, f'Total Revenue: £{total1:,} Millions',ha='left', va='baseline', transform=ax1.transAxes, fontsize=10, fontweight='bold')
    #Creating a pie chart for the years 2020–2021, adding a title and the total value.
    ax2.pie(data2_updated.loc['Apr 2020 to Mar 2021'], labels=data2_updated.columns, autopct='%1.1f%%', colors=['red', 'green', 'blue', 'purple','orange'])
    ax2.set_title('Great Britain, 2021–2022, proportion of passenger revenue by ticket type',fontweight='bold')
    ax2.text(0, 0, f'Total Revenue: £{total2:,} Millions',ha='left', va='baseline', transform=ax2.transAxes, fontsize=10, fontweight='bold')
    #Save the figure
    plt.savefig("Pieplot.png",dpi=100)
    #Show the figure
    plt.show()
    return

#main code that will be executed once the script has been run
if __name__ == "__main__":
    #readData1() is used to read data into the bar and pie charts.
    result3, result4 = readData1()
    #using the data read in from the readData1() method, calls the piePlot() function to produce a pie plot.
    piePlot(result4)
    
    
    
    
    
    