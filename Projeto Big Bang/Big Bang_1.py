# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import os
from os import  popen

import subprocess

import time

from BigBangCentral import Central

################################################################################

raiz = Tk()


Central(raiz)
raiz.mainloop()