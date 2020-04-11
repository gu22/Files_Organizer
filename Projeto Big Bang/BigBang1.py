# -*- coding: utf-8 -*-

import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import BigBangCentral
from BigBangCentral import *


import ConsultaBigBang


import BigBangMenu
from BigBangMenu import openarq



import os
from os import  popen

import subprocess

import time

################################################################################
raiz = Tk()
Central(raiz)


def diretorio():
        os.system('explorer '+'Z:\1 - VALE"\"3 - TIG')
        #subprocess.call(['C:/Users/gustavo.santos/Desktop/teste.bat'])

# Menus ##############################################

menubar = Menu(raiz)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)


openmenu = Menu(filemenu, tearoff=0)
filemenu.add_cascade(label='Open',menu= openmenu)
openmenu.add_command(label="Consulta",command = openarq)

filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit")







# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)

editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")

#
optionmenu = Menu(menubar, tearoff=1)
menubar.add_cascade(label="Pastas", menu=optionmenu)

optionmenu.add_command(label="Dir",command= diretorio)

#
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)

helpmenu.add_command(label="About")


#def diretorio():
#        os.system('start'+r'C:\Users\gustavo.santos\Desktop\old')



# ####################################################






# display the menu
raiz.config(menu=menubar)

raiz.mainloop()