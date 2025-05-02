import tkinter as tk
from tkinter import ttk
from styles import appliquer_theme, configurer_styles
from utils import ouvrir_lien_mit, effet_fondu, afficher_texte
from player_setup import afficher_fenetre_joueurs
from constants import DESCRIPTION

def creer_interface():
    fenetre = tk.Tk()
    fenetre.title("Chronomètre, Projet STI2D")
    fenetre.geometry("500x400")
    fenetre.configure(bg="#1c1c1c")
    fenetre.resizable(False, False)

    appliquer_theme()
    configurer_styles()

    titre = ttk.Label(
        fenetre,
        text="\u23F1 Le Grand Décompte!\nSerez-vous plus rapide que le temps ?",
        justify="center",
        font=("Arial", 18, "bold"),
        background="#1c1c1c",
        foreground="white"
    )
    titre.pack(pady=20)
    effet_fondu(titre, fenetre)

    texte_intro = ttk.Label(fenetre, text="", font=("Arial", 10, "bold"), background="#1c1c1c", foreground="white")
    texte_intro.pack(pady=6)
    afficher_texte(texte_intro, fenetre, DESCRIPTION)

    cadre_boutons = ttk.Frame(fenetre)
    cadre_boutons.place(relx=0.5, rely=0.55, anchor="center")

    btn_jouer = ttk.Button(cadre_boutons, style="Large.Accent.TButton", text="Contre-La-Montre", command=lambda: afficher_fenetre_joueurs(fenetre))
    btn_quitter = ttk.Button(cadre_boutons, style="Large.Accent.TButton", text="Quitter", command=fenetre.destroy)

    fenetre.after(1500, lambda: (btn_jouer.pack(pady=15), btn_quitter.pack(pady=15)))

    mention_license = ttk.Label(fenetre, text="Projet d'STI2D sous licence ", font=("Arial", 8), background="#1c1c1c", foreground="white")
    mention_license.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-30)

    lien_mit = tk.Label(fenetre, text="MIT", fg="white", bg="#1c1c1c", font=("Arial", 8, "underline"), cursor="hand2")
    lien_mit.place(relx=0.0, rely=1.0, anchor="sw", x=134, y=-28)
    lien_mit.bind("<Button-1>", lambda e: ouvrir_lien_mit())

    mention_copyright = ttk.Label(
        fenetre,
        text="Copyright © Congia Vanille, Dubus Yanis",
        font=("Arial", 8),
        background="#1c1c1c",
        foreground="white"
    )
    mention_copyright.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)

    fenetre.mainloop()
