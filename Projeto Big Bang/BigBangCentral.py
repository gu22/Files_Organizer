# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import os
from os import popen

import subprocess

import time

#Criando classe para executar na celula principal

class Central(object):
    def __init__ (self,central=None):

        def calibragem ():
            self.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("exe","*.exe"),("all files","*.*")))
            subprocess.call([self.filename])




        self.slotum = Frame(central)
        self.slotum['pady']= 5
        self.slotum.pack()

        self.slotdois = Frame (central)
        self.slotdois['padx']= 20
        self.slotdois.pack()

        self.slottres = Frame (central)
        self.slottres.pack()

        self.slotquatro = Frame (central)
        self.slotquatro.pack()

        self.cal = Button(self.slotum, text ="Calibragem", command = calibragem)
        self.cal.pack(side=LEFT)

        self.ext = Button(self.slotum, text ="Extração de dados")
        self.ext.pack(side=LEFT)






#root=Tk()
#Central(root)
#root.mainloop()


