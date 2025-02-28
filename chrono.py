import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import time
import os

class CourseApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestionnaire de Course - Vanille")
        self.geometry("800x600")
        
        # Gestionnaire de données
        self.equipes = {}
        self.resultats = []
        self.archive_dir = "archives"
        
        # Création de l'interface
        self.create_widgets()
        
    def create_widgets(self):
        # Frame principale
        main_frame = ttk.Frame(self)
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Titre en haut
        title_label = ttk.Label(main_frame, 
                              text="Gestionnaire de Course Char à Voile", 
                              font=('Helvetica', 16, 'bold'))
        title_label.pack(pady=20)
        
        # Boutons centraux
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(expand=True)
        
        buttons = [
            ("Démarrer une course", self.demarrer_course),
            ("Contre-la-montre", self.contre_la_montre),
            ("Afficher le classement", self.afficher_classement),
            ("Archiver les résultats", self.archiver_results),
            ("Quitter", self.quit)
        ]
        
        for text, command in buttons:
            btn = ttk.Button(button_frame, 
                           text=text, 
                           command=command,
                           width=25)
            btn.pack(pady=5)
        
        # Zone de logs
        self.log_text = tk.Text(main_frame, height=10, state='disabled')
        self.log_text.pack(pady=20, fill='x')
    
    def log_message(self, message):
        self.log_text.config(state='normal')
        self.log_text.insert('end', message + '\n')
        self.log_text.see('end')
        self.log_text.config(state='disabled')
    
    def detecter_rfid(self):
        self.log_message("En attente de détection RFID...")
        popup = tk.Toplevel()
        popup.title("Simulation RFID")
        
        ttk.Label(popup, text="Entrez l'UID simulé:").pack(padx=10, pady=5)
        uid_entry = ttk.Entry(popup)
        uid_entry.pack(padx=10, pady=5)
        
        def confirm():
            uid = uid_entry.get()
            popup.destroy()
            self.enregistrer_equipe(uid)
        
        ttk.Button(popup, text="Valider", command=confirm).pack(pady=5)
    
    def enregistrer_equipe(self, uid):
        if uid not in self.equipes:
            nom = simpledialog.askstring("Enregistrement", "Nom de l'équipe:")
            if nom:
                self.equipes[uid] = nom
                self.log_message(f"Équipe '{nom}' enregistrée (UID: {uid})")
        else:
            messagebox.showwarning("Erreur", "Carte déjà enregistrée")
    
    def demarrer_course(self):
        self.detecter_rfid()
        # Ajouter ici la logique de chronométrage
    
    def contre_la_montre(self):
        self.detecter_rfid()
        # Ajouter ici la logique spécifique
    
    def afficher_classement(self):
        classement_window = tk.Toplevel()
        classement_window.title("Classement")
        
        lb = tk.Listbox(classement_window, width=50)
        lb.pack(padx=10, pady=10)
        
        for i, result in enumerate(sorted(self.resultats), 1):
            lb.insert('end', f"{i}ème - {result}s")
    
    def archiver_results(self):
        path = filedialog.asksaveasfilename(
            initialdir=self.archive_dir,
            filetypes=[("Fichiers texte", "*.txt")]
        )
        if path:
            try:
                with open(path, 'w') as f:
                    f.write("Résultats des courses:\n")
                    for t in self.resultats:
                        f.write(f"{t}\n")
                self.log_message(f"Archive sauvegardée: {path}")
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

if __name__ == "__main__":
    app = CourseApp()
    app.mainloop()
