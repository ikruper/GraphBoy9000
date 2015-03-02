# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:10:58 2015

@author: ian
"""

import numpy
import pylab

def DrawLine(x_values, y_values):
    lbf_x_values = numpy.array(x_values)
    lbf_y_values = numpy.array(y_values)
    lbf_values = numpy.polyfit(lbf_x_values, lbf_y_values, 1)
    pylab.plot([x_values[0], x_values[-1]], [lbf_values[1]+
                lbf_values[0]*x_values[0], 
                lbf_values[1]+lbf_values[0]*x_values[-1]], 'k--')
    print("Equation of best fit line: "+str(lbf_values[0])+"x + "+
                str(lbf_values[1]))
    print("Done!")