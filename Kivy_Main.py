# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:28:50 2015

@author: ian
"""

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.screenmanager import ScreenManager, Screen
#import kivy.base as Base
import pylab
import Line_Conditioning

class Menu(GridLayout):
    x_vals = []
    y_vals = []
    lbf = ''
    rsq = ''
    val_counter = 0
    ser_counter = 0
    def get_current_value(self, *args):
        try:
            self.x_vals.append(float(self.ids['x_value'].text))
            self.y_vals.append(float(self.ids['y_value'].text))
            self.ids['x_value'].text = ""
            self.ids['y_value'].text = ""
            self.val_counter += 1
            self.ids['current_value'].text = "Value "+str(self.val_counter + 1)
        except ValueError:
            pass
    
    def new_series(self, *args):
        if (self.ser_counter < 5):
            if (self.ids['dots_radio'].active == True):
                pylab.plot(self.x_vals, self.y_vals, 'o', label=self.ids['data_series_label'].text)
            elif (self.ids['line_radio'].active == True):
                pylab.plot(self.x_vals, self.y_vals, label=self.ids['data_series_label'].text)
            Line_Conditioning.Padding(self.x_vals, self.y_vals)
            self.x_vals = []
            self.y_vals = []
            self.ser_counter += 1
            self.val_counter = 1
            self.ids['data_series_label'].text = ""
            self.ids['current_value'].text = "Value "+str(self.val_counter)
            self.ids['x_value'].text = ""
            self.ids['y_value'].text = ""
            self.ids['lbf_check'].active == False
    
    def submit(self, *args):
        pylab.title(self.ids['graph_title'].text)
        pylab.xlabel(self.ids['xaxis_label'].text)
        pylab.ylabel(self.ids['yaxis_label'].text)
        pylab.grid(b=True, which="both")
        if (self.ids['dots_radio'].active == True):
            pylab.plot(self.x_vals, self.y_vals, 'o', label=self.ids['data_series_label'].text)
        elif (self.ids['line_radio'].active == True):
           pylab.plot(self.x_vals, self.y_vals, label=self.ids['data_series_label'].text)
        Line_Conditioning.Padding(self.x_vals, self.y_vals)
        if (self.ids['lbf_check'].active == True and self.ser_counter == 0):
            lbf, rsq = Line_Conditioning.DrawLine(self.x_vals, self.y_vals)
            self.ids['lbf_equation'].text = lbf
            self.ids['r_squared'].text = rsq
        pylab.legend(loc='best')
        pylab.show()
        
class Results(GridLayout):
    pass

class MyScreenManager():
    pass

class GraphBoy9000App(App):
    def build(self):
        menu = Menu()
        return menu

if __name__ == "__main__":
    GraphBoy9000App().run()