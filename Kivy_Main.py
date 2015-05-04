# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:28:50 2015

@author: ian
"""

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
import kivy.base as Base

import pylab
import Line_Conditioning

class Menu(GridLayout):
    x_vals = [[] for i in range(5)]
    y_vals = [[] for i in range(5)]
    data_labels = []
    lbf = ''
    rsq = ''
    val_counter = 0
    ser_counter = 0
    
    def current_value(self, *args):
        try:
            self.x_vals[self.ser_counter].append(float(self.ids['x_value'].text))
            self.y_vals[self.ser_counter].append(float(self.ids['y_value'].text))
            self.ids['x_value'].text = ""
            self.ids['y_value'].text = ""
            self.val_counter += 1
            self.ids['current_value'].text = "Value "+str(self.val_counter + 1)
        except ValueError:
            pass
    
    def new_series(self, *args):
        if (self.ser_counter < 5):
            self.data_labels.append(self.ids['data_series_label'].text)
            self.ser_counter += 1
            self.val_counter = 0
            self.ids['current_value'].text = "Value "+str(self.val_counter + 1)
            self.ids['current_series'].text = "Series "+str(self.ser_counter + 1)
            self.ids['data_series_label'].text = ""
            
    def undo_entry(self, *args):
        if (self.val_counter > 0):
            self.ids['x_value'].text = str(self.x_vals[self.ser_counter][len(self.x_vals[self.ser_counter])-1])
            self.ids['y_value'].text = str(self.y_vals[self.ser_counter][len(self.y_vals[self.ser_counter])-1])
            del(self.x_vals[self.ser_counter][len(self.x_vals[self.ser_counter])-1])
            del(self.y_vals[self.ser_counter][len(self.y_vals[self.ser_counter])-1])
            self.val_counter -= 1
            self.ids['current_value'].text = "Value "+str(self.val_counter + 1)
    
    def delete_series(self, *args):
        if (self.ser_counter > 0):
            del(self.x_vals[self.ser_counter])
            del(self.y_vals[self.ser_counter])
            self.ser_counter -= 1
            self.val_counter = len(self.x_vals[self.ser_counter])
            self.ids['current_value'].text = "Value "+str(self.val_counter)
            self.ids['current_series'].text = "Series "+str(self.ser_counter + 1)
            self.ids['x_value'].text = str(self.x_vals[self.ser_counter][len(self.x_vals[self.ser_counter])-1])
            self.ids['y_value'].text = str(self.y_vals[self.ser_counter][len(self.y_vals[self.ser_counter])-1])
        
    def submit(self, *args):
        pylab.title(self.ids['graph_title'].text)
        pylab.xlabel(self.ids['xaxis_label'].text)
        pylab.ylabel(self.ids['yaxis_label'].text)
        pylab.grid(b=True, which="both")
        for series in range(self.ser_counter + 1):
            if (self.ids['dots_radio'].active == True):
                pylab.plot(self.x_vals[series], self.y_vals[series], 'o', label=self.ids['data_series_label'].text)
            elif (self.ids['line_radio'].active == True):
               pylab.plot(self.x_vals[series], self.y_vals[series], label=self.ids['data_series_label'].text)
            Line_Conditioning.Padding(self.x_vals[series], self.y_vals[series])         
        if (self.ids['lbf_check'].active == True and self.ser_counter == 0):
            lbf, rsq = Line_Conditioning.DrawLine(self.x_vals, self.y_vals)
            self.ids['lbf_equation'].text = lbf
            self.ids['r_squared'].text = rsq
        pylab.legend(loc='best')
        pylab.show()
        pylab.plot()
        
    def exit_app(self, *args):
        Base.sys.exit()


class GraphBoy9000App(App):
    def build(self):
        Config.set('graphics', 'height', '700')
        menu = Menu()
        return menu

if __name__ == "__main__":
    GraphBoy9000App().run()