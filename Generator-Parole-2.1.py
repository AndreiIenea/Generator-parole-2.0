import tkinter as tk
from tkinter import messagebox
import random
import string

# Funcția care evaluează tăria parolei
def evaluate_password_strength(password):
    length = len(password)
    
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digits = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    strength_score = length

    # Fiecare tip de caracter crește tăria parolei
    if has_lower:
        strength_score += 2
    if has_upper:
        strength_score += 2
    if has_digits:
        strength_score += 2
    if has_special:
        strength_score += 2

    # Evaluăm scorul
    if strength_score <= 8:
        return "Slabă"
    elif 8 < strength_score <= 12:
        return "Mediu"
    else:
        return "Puternică"

# Funcția care generează parola
def generate_password():
    try:
        length = int(entry_length.get())  # Preluăm numărul de caractere din input
        if length < 4:
            messagebox.showerror("Eroare", "Parola trebuie să aibă minim 4 caractere!")
            return
        
        # Colectăm setările utilizatorului
        use_lower = var_lower.get()
        use_upper = var_upper.get()
        use_digits = var_digits.get()
        use_special = var_special.get()

        # Verificăm dacă cel puțin o opțiune este selectată
        if not (use_lower or use_upper or use_digits or use_special):
            messagebox.showerror("Eroare", "Selectați cel puțin un tip de caracter!")
            return

        # Adunăm tipurile de caractere selectate
        available_characters = ""
        if use_lower:
            available_characters += string.ascii_lowercase
        if use_upper:
            available_characters += string.ascii_uppercase
        if use_digits:
            available_characters += string.digits
        if use_special:
            available_characters += string.punctuation

        # Generăm parola
        password = random.choices(available_characters, k=length)

        # Amestecăm caracterele pentru mai multă siguranță
        random.shuffle(password)

        # Afișăm parola generată în câmpul de text
        password_entry.config(state=tk.NORMAL)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "".join(password))
        password_entry.config(state=tk.DISABLED)

        # Evaluăm tăria parolei și o afișăm
        strength = evaluate_password_strength(password)
        label_strength.config(text=f"Tăria parolei: {strength}", fg="lime")
    
    except ValueError:
        messagebox.showerror("Eroare", "Introduceți un număr valid pentru lungimea parolei!")

# Funcția care copiază parola în clipboard
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copiat", "Parola a fost copiată în clipboard!")

# Creăm fereastra principală
root = tk.Tk()
root.title("Password Generator - Hacking Style")
root.geometry("500x500")
root.resizable(False, False)
root.config(bg="black")

# Designul de hacking pentru interfață
title_font = ("Courier", 16, "bold")
label_font = ("Courier", 12)
entry_font = ("Courier", 12)

label_title = tk.Label(root, text="Password Generator", font=title_font, fg="lime", bg="black")
label_title.pack(pady=10)

frame = tk.Frame(root, bg="black")
frame.pack(pady=10)

label_length = tk.Label(frame, text="Număr de caractere:", font=label_font, fg="white", bg="black")
label_length.grid(row=0, column=0)

entry_length = tk.Entry(frame, width=5, font=entry_font, bg="black", fg="lime", insertbackground="lime")
entry_length.grid(row=0, column=1)
entry_length.insert(0, "12")  # Setăm un număr default de caractere

# Adăugăm checkbox-uri pentru a selecta tipurile de caractere
var_lower = tk.BooleanVar(value=True)
check_lower = tk.Checkbutton(frame, text="Litere mici", variable=var_lower, font=label_font, fg="lime", bg="black", selectcolor="black", activebackground="black")
check_lower.grid(row=1, column=0, sticky='w')

var_upper = tk.BooleanVar(value=True)
check_upper = tk.Checkbutton(frame, text="Litere mari", variable=var_upper, font=label_font, fg="lime", bg="black", selectcolor="black", activebackground="black")
check_upper.grid(row=1, column=1, sticky='w')

var_digits = tk.BooleanVar(value=True)
check_digits = tk.Checkbutton(frame, text="Cifre", variable=var_digits, font=label_font, fg="lime", bg="black", selectcolor="black", activebackground="black")
check_digits.grid(row=2, column=0, sticky='w')

var_special = tk.BooleanVar(value=True)
check_special = tk.Checkbutton(frame, text="Caractere speciale", variable=var_special, font=label_font, fg="lime", bg="black", selectcolor="black", activebackground="black")
check_special.grid(row=2, column=1, sticky='w')

# Butonul pentru a genera parola
button_generate = tk.Button(frame, text="Generează", font=label_font, command=generate_password, fg="black", bg="lime", activebackground="lime")
button_generate.grid(row=3, columnspan=2, pady=10)

# Câmpul pentru a afișa parola generată
password_entry = tk.Entry(root, width=40, font=entry_font, justify="center", bg="black", fg="lime", insertbackground="lime")
password_entry.pack(pady=20)
password_entry.config(state=tk.DISABLED)

# Afișăm tăria parolei
label_strength = tk.Label(root, text="Tăria parolei: ", font=label_font, fg="white", bg="black")
label_strength.pack(pady=10)

# Butonul pentru a copia parola
button_copy = tk.Button(root, text="Copiază parola", font=label_font, command=copy_password, fg="black", bg="lime", activebackground="lime")
button_copy.pack(pady=10)

# Pornim bucla principală a interfeței grafice
root.mainloop()