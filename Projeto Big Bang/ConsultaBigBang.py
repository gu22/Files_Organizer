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

class Consulta():
    def __init__(self):
        def consultar():
            pass

        area = Tk()
        listbox = Listbox(area)
        listbox.pack()

        listbox.insert(END, "a list entry")

        for item in ["one", "two", "three", "four"]:
            listbox.insert(END, item)

        mainloop()



