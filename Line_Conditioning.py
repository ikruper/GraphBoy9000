# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:10:58 2015

@author: ian
"""

import numpy
import pylab
from scipy import stats

def DrawLine(x_values, y_values):
    lbf_x_values = numpy.array(x_values)
    lbf_y_values = numpy.array(y_values)
    lbf_values = numpy.polyfit(lbf_x_values, lbf_y_values, 1)
    pylab.plot([x_values[0], x_values[-1]], [lbf_values[1]+
                lbf_values[0]*x_values[0], 
                lbf_values[1]+lbf_values[0]*x_values[-1]], 'k--')
    slope, intercept, r_value, p_value, std_err = stats.linregress(lbf_x_values
                ,lbf_y_values)
    if (slope == 0):
#        best_fit_line = 'y = '+str(intercept)
        best_fit_line = 'y = '+'{0:.5f}'.format(intercept)
    elif (intercept == 0):
#        best_fit_line = 'y = '+str(slope)+'x'
        best_fit_line = 'y = '+'{0:.5f}'.format(slope)+'x'
    elif (intercept < 0):
        best_fit_line = 'y = '+'{0:.5f}'.format(slope)+'x - '+'{0:.5f}'.format(abs(intercept))
    else:
        best_fit_line = 'y = '+'{0:.5f}'.format(slope)+'x'+'x + '+'{0:.5f}'.format(abs(intercept))
    r_squared = str(r_value**2)
    return best_fit_line, r_squared
    
def Padding(x_values, y_values):
#    pylab.plot(x_values[len(x_values)-1]+(0.2*(x_values[len(x_values)-1]-x_values[0]))
#                , y_values[0], visible=False)
    pylab.plot(x_values[len(x_values)-1]+(0.2*(x_values[len(x_values)-1]-x_values[0])),
                        y_values[len(y_values)-1]+(0.2*(y_values[len(y_values)-1]-y_values[0])),
                        x_values[0]-(0.2*(x_values[len(x_values)-1]-x_values[0])),
                        y_values[0]-(0.2*(y_values[len(y_values)-1]-y_values[0])), visible=False)