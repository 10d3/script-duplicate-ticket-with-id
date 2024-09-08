import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont, ImageColor
import os

# Dossier contenant les polices
FONT_DIR = "fonts"  # Remplace ceci par le chemin vers ton dossier de polices

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        entry_image_path.delete(0, tk.END)
        entry_image_path.insert(0, file_path)
        
        # Ouvrir l'image et obtenir ses dimensions
        image = Image.open(file_path)
        width, height = image.size
        
        # Afficher les dimensions dans l'interface utilisateur
        label_image_dimensions.config(text=f"Dimensions de l'image: {width} x {height}")

def choose_color():
    color_code = colorchooser.askcolor(title="Choisir la couleur du texte")[1]
    if color_code:
        entry_text_color.delete(0, tk.END)
        entry_text_color.insert(0, color_code)

def update_font_list():
    font_files = [f for f in os.listdir(FONT_DIR) if f.endswith('.ttf')]
    font_names = [os.path.splitext(f)[0] for f in font_files]
    font_names.insert(0, "Sélectionner une police")  # Ajouter une option par défaut
    font_menu['values'] = font_names

def generate_tickets():
    image_path = entry_image_path.get()
    start_number = int(entry_start_number.get())
    end_number = int(entry_end_number.get())
    position_normal = (int(entry_x_normal.get()), int(entry_y_normal.get()))
    position_reversed = (int(entry_x_reversed.get()), int(entry_y_reversed.get()))
    text_size = int(entry_text_size.get())
    text_color = entry_text_color.get() or "#FFFFFF"  # Couleur par défaut si non spécifiée
    font_name = font_var.get()
    
    # Vérifier si la couleur est en format hexadécimal valide
    try:
        text_color = ImageColor.getrgb(text_color)  # Convertir en format RGB
    except ValueError:
        messagebox.showerror("Erreur", "La couleur spécifiée n'est pas valide. Veuillez entrer une couleur hexadécimale.")
        return
    
    # Vérifier si une police est sélectionnée
    if font_name == "Sélectionner une police":
        messagebox.showerror("Erreur", "Veuillez sélectionner une police.")
        return

    # Charger l'image du ticket
    ticket = Image.open(image_path)
    
    # Charger la police sélectionnée
    font_path = os.path.join(FONT_DIR, f"{font_name}.ttf")
    try:
        font = ImageFont.truetype(font_path, text_size)
    except IOError:
        messagebox.showerror("Erreur", "La police sélectionnée est introuvable.")
        return

    for i in range(start_number, end_number + 1):
        # Créer une copie de l'image pour chaque ticket
        ticket_modifie = ticket.copy()

        # Ajouter le numéro normal sur l'image avec le préfixe
        draw = ImageDraw.Draw(ticket_modifie)
        numero = f"NO: {i:03d}"  # Format NO: 001, NO: 002, NO: 003, ...
        draw.text(position_normal, numero, text_color, font=font)  # Choisir la couleur du texte

        # Ajouter le numéro pivoté de 90 degrés sur l'image avec le préfixe
        numero_reversed = f"NO: {i:03d}"  # Utiliser le même numéro ou ajuster si nécessaire
        bbox = font.getbbox(numero_reversed)
        text_image = Image.new('RGBA', (bbox[2] - bbox[0], bbox[3] - bbox[1]), (0, 0, 0, 0))
        draw_reversed = ImageDraw.Draw(text_image)
        draw_reversed.text((-bbox[0], -bbox[1]), numero_reversed, text_color, font=font)
        
        # Faire pivoter le texte de 90 degrés
        text_image = text_image.rotate(90, expand=True)
        
        # Coller le texte pivoté sur le ticket
        ticket_modifie.paste(text_image, position_reversed, text_image)

        # Enregistrer le ticket modifié
        ticket_modifie.save(f"ticket_{i:03d}.png")
    
    messagebox.showinfo("Succès", "Les tickets ont été générés avec succès!")

# Interface utilisateur
root = tk.Tk()
root.title("Générateur de Tickets Numérotés")

tk.Label(root, text="Chemin de l'image de ticket:").grid(row=0, column=0, padx=10, pady=10)
entry_image_path = tk.Entry(root, width=50)
entry_image_path.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Sélectionner l'image", command=select_image).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Dimensions de l'image:").grid(row=1, column=0, padx=10, pady=10)
label_image_dimensions = tk.Label(root, text="Dimensions de l'image: Non sélectionnée")
label_image_dimensions.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Numéro de début:").grid(row=2, column=0, padx=10, pady=10)
entry_start_number = tk.Entry(root)
entry_start_number.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Numéro de fin:").grid(row=3, column=0, padx=10, pady=10)
entry_end_number = tk.Entry(root)
entry_end_number.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Position du numéro normal (X, Y):").grid(row=4, column=0, padx=10, pady=10)
entry_x_normal = tk.Entry(root)
entry_x_normal.grid(row=4, column=1, padx=10, pady=5)
entry_y_normal = tk.Entry(root)
entry_y_normal.grid(row=4, column=2, padx=10, pady=5)

tk.Label(root, text="Position du numéro pivoté (X, Y):").grid(row=5, column=0, padx=10, pady=10)
entry_x_reversed = tk.Entry(root)
entry_x_reversed.grid(row=5, column=1, padx=10, pady=5)
entry_y_reversed = tk.Entry(root)
entry_y_reversed.grid(row=5, column=2, padx=10, pady=5)

tk.Label(root, text="Taille du texte:").grid(row=6, column=0, padx=10, pady=10)
entry_text_size = tk.Entry(root)
entry_text_size.grid(row=6, column=1, padx=10, pady=10)
entry_text_size.insert(0, "50")  # Valeur par défaut

tk.Label(root, text="Couleur du texte (Hex):").grid(row=7, column=0, padx=10, pady=10)
entry_text_color = tk.Entry(root)
entry_text_color.grid(row=7, column=1, padx=10, pady=10)
tk.Button(root, text="Choisir la couleur", command=choose_color).grid(row=7, column=2, padx=10, pady=10)

tk.Label(root, text="Police:").grid(row=8, column=0, padx=10, pady=10)
font_var = tk.StringVar(value="Sélectionner une police")
font_menu = ttk.Combobox(root, textvariable=font_var, state="readonly")
font_menu.grid(row=8, column=1, padx=10, pady=10)
update_font_list()

tk.Button(root, text="Générer les tickets", command=generate_tickets).grid(row=9, column=1, padx=10, pady=20)

root.mainloop()
