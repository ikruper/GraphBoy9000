# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:28:50 2015

@author: ian
"""

from kivy.app import App
from kivy.uix.widget import Widget

class Menu(Widget):
    pass

class GraphBoy9000App(App):
    def build(self):
        return Menu()

if __name__ == "__main__":
    GraphBoy9000App().run()