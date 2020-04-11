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

def openarq ():
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("exe","*.exe"),("all files","*.*")))
    try:
        subprocess.call([filename])
    except Exception:
        pass

##class Menus():
##    def __init__():
##        os.system('start'+r'C:\Users\gustavo.santos\Desktop\old')

####        # Define settings upon initialization. Here you can specify
##    def __init__(self, master=None):
##
##        # parameters that you want to send through the Frame class.
##        Frame.__init__(self, master)
##        #reference to the master widget, which is the tk window
##        self.master = master
##        #with that, we want to then run init_window, which doesn't yet exist
##        self.init_window()
##
##    #Creation of init_window
##    def init_window(self):
##        # allowing the widget to take the full space of the root window
##        self.pack(fill=BOTH, expand=1)
##
##        # creating a menu instance
##        menu = Menu(self.master)
##        self.master.config(menu=menu)
##
##        # create the file object)
##        filemenu = Menu(menu)
##        menu.add_cascade(label="File", menu=filemenu)
##        filemenu.add_command(label="Sair")
##
##        # create the file object)
##        edit = Menu(menu)
##        menu.add_cascade(label="Edit", menu=edit)
##        edit.add_command(label="Undo")
##
##    def _close(self):
##        self.destroy()
##
##    def diretorio ():







##    def criandomenu(self):
##
##        menubar = Menu(self.master)
##        self.master.config(menu=menubar)
##
##        filemenu = Menu(menubar,tearoff=0)
##        menubar.add_cascade(label="File", menu=filemenu)
##        filemenu.add_command(label="Open")
##        filemenu.add_command(label="Save")
##        filemenu.add_separator()
##        filemenu.add_command(label="Exit")


##root=Tk()
##Menus(root)
##root.mainloop()







