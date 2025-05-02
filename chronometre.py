import tkinter as tk
from tkinter import ttk
import time
from styles import appliquer_theme, configurer_styles

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

        self.btn_stop = ttk.Button(self.fenetre, text="Stop", command=self.arreter_chrono)
        self.btn_stop.pack(pady=10)

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
