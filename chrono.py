import tkinter as tk
import time

class Chronometre:
    def __init__(self, root):
        self.root = root
        self.root.title("Chronomètre")
        
        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        
        # Affichage du temps en très très gros
        self.time_label = tk.Label(root, text="00:00:000", font=("Arial", 120))
        self.time_label.pack(pady=20)
        
        # Bouton Start
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        # Bouton Stop
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10)
        
        # Bouton Reset
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        self.update_time()

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time

    def reset(self):
        # Réinitialiser le temps et mettre à jour l'affichage
        self.running = False
        self.elapsed_time = 0
        self.start_time = None
        self.time_label.config(text="00:00:000")

    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            minutes, seconds = divmod(int(self.elapsed_time), 60)
            milliseconds = int((self.elapsed_time - int(self.elapsed_time)) * 1000)
            time_str = f"{minutes:02}:{seconds:02}:{milliseconds:03}"
            self.time_label.config(text=time_str)
            self.root.after(10, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    chrono = Chronometre(root)
    root.mainloop()
