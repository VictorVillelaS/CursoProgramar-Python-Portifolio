import tkinter as tk
from tkinter import ttk
from FRONT.frmPreferencias import FrmPreferencias
from FRONT.frmFamiliares import FrmFamiliares
from FRONT.frnPreferenciasDeFamiliares import FrmPreferenciasDeFamiliares


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        tabControl = ttk.Notebook(self)

        tab1 = FrmPreferencias(tabControl)
        tabControl.add(tab1, text='Preferencias')

        tab2 = FrmFamiliares(tabControl)
        tabControl.add(tab2, text='Familiares')
    
        tab3 = FrmPreferenciasDeFamiliares(tabControl)
        tabControl.add(tab3, text="Preferencias de Familiares")

        tabControl.pack(expand=1, fill="both")
