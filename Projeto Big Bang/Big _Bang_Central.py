# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import os
from os import  popen

import subprocess

import time

#Criando clase para executar na celula principal

class Central:
    def _init_ (self,central = None):

        self.slotum = Frame(central)
        self.slotum.pack()

        self.slotdois = Frame (central)
        self.slotdois.pack()

        self.slottres = Frame (central)
        self.slottres.pack()

        self.slotquatro = Frame (central)
        self.slotquatro.pack()


