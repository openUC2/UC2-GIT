#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:05:09 2020

@author: bene
"""

import tkinter as tk

class FullScreenApp(object):
    padding=3
    dimensions="{0}x{1}+0+0"

    def __init__(self, master, **kwargs):
        self.master=master
        width=master.winfo_screenwidth()-self.padding
        height=master.winfo_screenheight()-self.padding
        master.geometry(self.dimensions.format(width, height))


        b = tk.Button(self.master, text="Press me!", command=lambda: self.pressed())
        b.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def pressed(self):
        print("clicked!")

root=tk.Tk()
root.wm_attributes('-fullscreen','true')

app=FullScreenApp(root)

root.mainloop()