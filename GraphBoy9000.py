# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 16:09:12 2015

@author: ian
"""

import pylab
import numpy

name_plot = raw_input("Name of plot: ")
x_lbl = raw_input("X axis label: ")
y_lbl = raw_input("Y axis label: ")
series_ct = 1

while (True):
    #Initial questions
    series_name = raw_input("Name of data series " + str(series_ct) +": ")
    if series_name == None:
        series_name = ""        
    num_elements = input("How many elements: ")
    
    x_values = []
    y_values = []
    
    
    #Value input loop
    for item in range(0, num_elements):
        value = raw_input("Enter point "+ str(item + 1) + " x,y: ")
        temp = value.split(",")
        x_values.append(temp[0])
        y_values.append(temp[1])            
        
    x_values = [float(i) for i in x_values]
    y_values = [float(i) for i in y_values]

    pylab.plot(x_values, y_values, label=series_name)
    
    
    #Line of best fit calculation and prompt
    lbf_choice = raw_input("Would you like a line of best fit for the series y/n: ")
    if lbf_choice == "y" or lbf_choice == "Y":
        lbf_x_values = numpy.array(x_values)
        lbf_y_values = numpy.array(y_values)
        lbf_values = numpy.polyfit(lbf_x_values, lbf_y_values, 1)
        pylab.plot([x_values[0], x_values[-1]], [lbf_values[1]+
                    lbf_values[0]*x_values[0], 
                    lbf_values[1]+lbf_values[0]*x_values[-1]], 'k--')

    
    #Prompt for another data series
    an_choice = raw_input("Would you like to add another data series y/n: ")
    series_ct += 1
    if an_choice == "n" or an_choice == "N":
        print("Equation of best fit line: "+str(lbf_values[0])+"x + "+
                    str(lbf_values[1]))
        print("Done!")
        break
    

#Graph formatting things
pylab.xlabel(x_lbl)
pylab.ylabel(y_lbl)
pylab.title(name_plot)
pylab.grid(b=True, which="both")
pylab.legend(loc="right")
pylab.show()
pylab.plot()