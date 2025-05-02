import tkinter as tk
from tkinter import messagebox, ttk
import sv_ttk as sv
import webbrowser

# Liste pour stocker les pseudos
pseudos = []

# Fonction pour ouvrir un lien
def ouvrir_lien_mit():
    webbrowser.open("http://example.com/")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Chronomètre, Projet STI2D")
fenetre.geometry("500x400")
fenetre.configure(bg="#1c1c1c")
fenetre.resizable(False, False)
sv.set_theme("dark")

style = ttk.Style()
style.configure("Large.Accent.TButton", padding=(20, 10), font=("Arial", 14))

# Effet de fondu pour le titre
def effet_fondu(opacity=0):
    if opacity <= 1.0:
        couleur = f"#{int(opacity * 255):02x}{int(opacity * 255):02x}{int(opacity * 255):02x}"
        titre.config(foreground=couleur)
        fenetre.after(50, effet_fondu, opacity + 0.05)

description = "3, 2, 1… GO ! Le chronomètre ne ment jamais !"
def afficher_texte(index=0):
    if index < len(description):
        texte_intro.config(text=description[:index+1])
        fenetre.after(50, afficher_texte, index+1)

titre = ttk.Label(fenetre, text="\u23F1 Le Grand Décompte!\nSerez-vous plus rapide que le temps ?", justify="center", font=("Arial", 18, "bold"), background="#1c1c1c", foreground="white")
titre.pack(pady=20)
effet_fondu()

texte_intro = ttk.Label(fenetre, text="", font=("Arial", 10, "bold"), background="#1c1c1c", foreground="white")
texte_intro.pack(pady=6)
afficher_texte()

cadre_boutons = ttk.Frame(fenetre)
cadre_boutons.place(relx=0.5, rely=0.55, anchor="center")

btn_jouer = ttk.Button(cadre_boutons, style="Large.Accent.TButton", text="Contre-La-Montre")
btn_quitter = ttk.Button(cadre_boutons, style="Large.Accent.TButton", text="Quitter", command=fenetre.destroy)
fenetre.after(1500, lambda: (btn_jouer.pack(pady=15), btn_quitter.pack(pady=15)))

# Mentions légales
mention_license = ttk.Label(fenetre, text="Projet d'STI2D sous licence ", font=("Arial", 8), background="#1c1c1c", foreground="white")
mention_license.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-30)

lien_mit = tk.Label(fenetre, text="MIT", fg="white", bg="#1c1c1c", font=("Arial", 8, "underline"), cursor="hand2")
lien_mit.place(relx=0.0, rely=1.0, anchor="sw", x=134, y=-28)
lien_mit.bind("<Button-1>", lambda e: ouvrir_lien_mit())

mention_copyright = ttk.Label(fenetre, text="Copyright © Congia Vanille, Dubus Yanis", font=("Arial", 8), background="#1c1c1c", foreground="white")
mention_copyright.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)

fenetre.mainloop()
