#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 00:19:21 2023

@author: tomthomas
"""


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#This function is helpful for reading in and preprocessing rail revenue data in preparation for further analysis, particularly where the "Time period" column is crucial for examining trends over time.
def readData1():
    #The Excel file is read using the Pandas read excel() function, and the resulting DataFrame is then assigned to the variable data2.
    data2 = pd.read_excel("/Users/Shared/Previously Relocated Items/Security/Tom/DS/7PAM2000 Applied Data Science 1/Rail Revenue.xlsx")
    #sets the index of the data2 to be the "Time period" column when creating a new DataFrame with the name data2_updated.
    data2_updated=data2.set_index('Time period')
    #to remove the last column from the DataFrame data2_updated
    data2_updated=data2_updated.drop(data2_updated.columns[-1], axis=1)
    #data2 and data2_updated are the two variables that the function returns. Whereas data2_updated has the same DataFrame with the 'Time period' column used as the new index, data2 contains the original DataFrame read in from the Excel file.
    return data2,data2_updated

#to be plotting a bar graph of the "Total passenger revenue" data against the "Time period" column in the given DataFrame.
def barPlot(data):
    #the process of giving x and y values
    x = data['Time period']
    y = data['Total passenger revenue']
    # Create the barplot figure 20 inches wide by 17 inches tall.
    plt.figure(figsize=(20,17))
    plt.bar(x, y)
    #to vertically rotate the x-labels for readability
    plt.xticks(rotation=90)
    # Add labels and a title
    plt.xlabel('Time period',fontsize=16, fontweight='bold')  
    plt.ylabel('Income in millions(GBP)',fontsize=16, fontweight='bold')
    plt.title('Great Britains rail passenger revenue from April 2010 to March 2022',fontsize=16, fontweight='bold')
    #saving the barplot as a picture file
    plt.savefig("/Users/Shared/Previously Relocated Items/Security/Tom/DS/7PAM2000 Applied Data Science 1/Barplot.png",dpi=100)
    # Display the plot
    plt.show()
    return

#main code that will be executed once the script has been run
if __name__ == "__main__":
    #readData1() is used to read data into the bar and pie charts.
    result3, result4 = readData1()
    #using the data read in from the readData1() method, calls the barPlot() function to produce a bar plot.
    barPlot(result3)

    
    
    
    
    
    
    