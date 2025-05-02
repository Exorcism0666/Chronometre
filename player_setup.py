import tkinter as tk
from tkinter import ttk
from styles import appliquer_theme, configurer_styles
from rfid_reader import RFIDReader
from chronometre import ChronometreFenetre

def afficher_fenetre_joueurs(parent_fenetre):
    nouvelle_fenetre = tk.Toplevel(parent_fenetre)
    nouvelle_fenetre.title("Détection RFID")
    nouvelle_fenetre.geometry("400x300")
    nouvelle_fenetre.configure(bg="#1c1c1c")
    nouvelle_fenetre.resizable(False, False)

    appliquer_theme()
    configurer_styles()

    # Titre principal
    titre = ttk.Label(nouvelle_fenetre, text="Passez votre carte RFID", font=("Arial", 14, "bold"), background="#1c1c1c", foreground="white")
    titre.pack(pady=15)

    # Texte de statut
    uid_label = ttk.Label(nouvelle_fenetre, text="En attente d'une carte...", background="#1c1c1c", foreground="white", font=("Arial", 10))
    uid_label.pack(pady=10)

    # Champs de pseudo
    pseudo_var = tk.StringVar()
    uid_detecte = []

    pseudo_label = ttk.Label(nouvelle_fenetre, text="Entrez votre pseudo :", background="#1c1c1c", foreground="white", font=("Arial", 10))
    champ_pseudo = ttk.Entry(nouvelle_fenetre, textvariable=pseudo_var)

    # Fonction appelée quand la carte est détectée
    def on_uid_detected(uid):
        if not uid_detecte:
            uid_detecte.append(uid)
            uid_label.config(text=f"Carte détectée : {uid}")
            pseudo_label.pack(pady=(10, 0))
            champ_pseudo.pack()
            btn_demarer.config(state="normal")
            rfid.stop()

    # Démarrer le lecteur RFID
    rfid = RFIDReader()
    rfid.start(on_uid_detected)

    # Boutons
    cadre_boutons = ttk.Frame(nouvelle_fenetre)
    cadre_boutons.pack(pady=20)

    def demarrer_course():
        pseudo = pseudo_var.get().strip()
        if pseudo:
            print(f"Course démarrée pour {pseudo} (UID : {uid_detecte[0]})")
            ChronometreFenetre(pseudo, uid_detecte[0])
            nouvelle_fenetre.destroy()
        else:
            print("Veuillez entrer un pseudo.")

    btn_demarer = ttk.Button(cadre_boutons, text="Démarrer la course", command=demarrer_course, state="disabled", style="Accent.TButton")
    btn_demarer.grid(row=0, column=0, padx=10)

    def fermer():
        rfid.stop()
        nouvelle_fenetre.destroy()

    btn_retour = ttk.Button(cadre_boutons, text="Retour", command=fermer)
    btn_retour.grid(row=0, column=1, padx=10)

    btn_quitter = ttk.Button(cadre_boutons, text="Quitter", command=parent_fenetre.destroy)
    btn_quitter.grid(row=0, column=2, padx=10)
