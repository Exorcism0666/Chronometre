import webbrowser

def ouvrir_lien_mit():
    webbrowser.open("https://github.com/Exorcism0666/Chronometre/")

def effet_fondu(widget, fenetre, opacity=0):
    if opacity <= 1.0:
        couleur = f"#{int(opacity * 255):02x}{int(opacity * 255):02x}{int(opacity * 255):02x}"
        widget.config(foreground=couleur)
        fenetre.after(50, effet_fondu, widget, fenetre, opacity + 0.05)

def afficher_texte(widget, fenetre, texte, index=0):
    if index < len(texte):
        widget.config(text=texte[:index+1])
        fenetre.after(50, afficher_texte, widget, fenetre, texte, index + 1)
