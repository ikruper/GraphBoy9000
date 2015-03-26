# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 16:09:12 2015

@author: Ian
"""


import pylab
import Line_Conditioning

name_plot = raw_input("Name of plot: ")
x_lbl = raw_input("X axis label: ")
y_lbl = raw_input("Y axis label: ")
series_ct = 1

while (True):
    x_values = []
    y_values = []
    
    #Initial questions
    series_name = raw_input("Name of data series " + str(series_ct) +": ")
    if series_name == None:
        series_name = ""
    points_choice = raw_input("Line(1) or points only(2): ")        
    num_elements = input("How many elements: ")
    
    
    #Value input loop
    for item in range(0, num_elements):
        value = raw_input("Enter point "+ str(item + 1) + " x,y: ")
        temp = value.split(",")
        x_values.append(float(temp[0]))
        y_values.append(float(temp[1]))            

    #Plotting points
    if points_choice == '1':
        pylab.plot(x_values, y_values, label=series_name)
    if points_choice == '2':
        pylab.plot(x_values, y_values, 'o', label=series_name)
    Line_Conditioning.Padding(x_values, y_values)
    
    
    #Line of best fit calculation and prompt
    if series_ct == 1:    
        lbf_choice = raw_input("Would you like a line of best fit for the series y/n: ")
        if lbf_choice == "y" or lbf_choice == "Y":
            Line_Conditioning.DrawLine(x_values, y_values)
            break

    #Prompt for another data series
    if series_ct < 6:
        an_choice = raw_input("Would you like to add another data series y/n: ")
        series_ct += 1
        if an_choice == "n" or an_choice == "N":
            print("Done!")
            break
        
    else:
        print("Done!")
        break
    

#Graph formatting things
pylab.xlabel(x_lbl)
pylab.ylabel(y_lbl)
pylab.title(name_plot)
pylab.grid(b=True, which="both")
pylab.legend(loc="right")
pylab.show()