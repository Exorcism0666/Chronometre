import tkinter as tk
from tkinter import ttk
import time
from styles import appliquer_theme, configurer_styles
from ultrason_reader import UltrasonWatcher


class ChronometreFenetre:
    def __init__(self, pseudo, uid):
        self.fenetre = tk.Toplevel()
        self.fenetre.title("Chronomètre")
        self.fenetre.geometry("300x200")
        self.fenetre.configure(bg="#1c1c1c")
        self.fenetre.resizable(False, False)

        appliquer_theme()
        configurer_styles()

        self.pseudo = pseudo
        self.uid = uid
        self.start_time = None
        self.running = False

        self.label_info = ttk.Label(self.fenetre, text=f"Joueur : {pseudo}", font=("Arial", 12), background="#1c1c1c", foreground="white")
        self.label_info.pack(pady=10)

        self.label_chrono = ttk.Label(self.fenetre, text="00:00:000", font=("Arial", 28, "bold"), background="#1c1c1c", foreground="white")
        self.label_chrono.pack(pady=20)

        self.ultrason = UltrasonWatcher(port='COM5')  # Port ESP32
        self.ultrason.start(self.arreter_chrono)


        self.label_resultat = ttk.Label(self.fenetre, text="", background="#1c1c1c", foreground="white", font=("Arial", 10))
        self.label_resultat.pack()

        self.lancer_chrono()

    def lancer_chrono(self):
        self.start_time = time.time()
        self.running = True
        self.mettre_a_jour()

    def mettre_a_jour(self):
        if self.running:
            elapsed = time.time() - self.start_time
            minutes = int(elapsed // 60)
            secondes = int(elapsed % 60)
            millis = int((elapsed - int(elapsed)) * 1000)
            self.label_chrono.config(text=f"{minutes:02}:{secondes:02}:{millis:03}")
            self.fenetre.after(10, self.mettre_a_jour)

    def arreter_chrono(self):
        if self.running:
            self.running = False
            final_time = self.label_chrono.cget("text")
            self.label_resultat.config(text=f"Temps final : {final_time}")
            print(f"[Chrono] {self.pseudo} ({self.uid}) a terminé en {final_time}")

            self.fenetre.geometry("400x300")  # Agrandit la fenêtre
            self.jouer_son()
            self.afficher_boutons_fin()

    def afficher_boutons_fin(self):
        cadre_boutons = ttk.Frame(self.fenetre)
        cadre_boutons.pack(pady=20)

        def recommencer():
            self.fenetre.destroy()
            ChronometreFenetre(self.pseudo, self.uid)

        def autre_joueur():
            from player_setup import afficher_fenetre_joueurs
            self.fenetre.destroy()
            afficher_fenetre_joueurs(self.fenetre.master)

        btn_recommencer = ttk.Button(cadre_boutons, text="🔁 Recommencer", command=recommencer, style="Accent.TButton")
        btn_autre = ttk.Button(cadre_boutons, text="👤 Autre joueur", command=autre_joueur)
        btn_quitter = ttk.Button(cadre_boutons, text="❌ Quitter", command=self.fenetre.master.destroy)

        btn_recommencer.pack(side="left", padx=10)
        btn_autre.pack(side="left", padx=10)
        btn_quitter.pack(side="left", padx=10)

    def jouer_son(self):
        try:
            import platform
            import os
            if platform.system() == "Windows":
                import winsound
                winsound.MessageBeep()
            else:
                os.system("paplay /usr/share/sounds/freedesktop/stereo/complete.oga 2>/dev/null &")
        except Exception as e:
            print(f"[Son] Impossible de jouer le son : {e}")