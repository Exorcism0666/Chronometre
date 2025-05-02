import sv_ttk as sv
from tkinter import ttk

def appliquer_theme():
    sv.set_theme("dark")

def configurer_styles():
    style = ttk.Style()
    style.configure("Large.Accent.TButton", padding=(20, 10), font=("Arial", 14))
