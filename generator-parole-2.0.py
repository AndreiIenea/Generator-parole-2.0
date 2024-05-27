import random
import string

# Definirea funcției care generează o singură parolă
def generare_parola(lungime=16):
    caractere = string.ascii_letters + string.digits + string.punctuation
    parola = ''.join(random.choice(caractere) for _ in range(lungime))
    return parola

# Definirea funcției care generează mai multe parole
def generare_parole(numar_parole, lungime_parola):
    parole = []
    for _ in range(numar_parole):
        parola = generare_parola(lungime_parola)
        parole.append(parola)
    return parole

while True:
    try:
        # Citirea parametrilor specificați de utilizator
        numar_parole = int(input("Introdu numărul de parole pe care dorești să le generezi: "))
        lungime_parola = int(input("Introdu lungimea parolelor: "))
        
        # Generarea parolelor
        parole_generate = generare_parole(numar_parole, lungime_parola)
        
        # Afișarea parolelor generate
        for idx, parola in enumerate(parole_generate, 1):
            print(f"Parola {idx}: {parola}")
        
        # Întreabă utilizatorul dacă dorește să continue
        continua = input("Dorești să generezi alte parole? (y/n): ").lower()
        if continua != 'y':
            break
    except ValueError:
        print("Te rog introdu numere valide pentru numărul și lungimea parolelor.")

print("Programul s-a încheiat.")
