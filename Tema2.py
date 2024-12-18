import pandas as pd
import matplotlib.pyplot as plt

# Citesc datele
try:
    data = pd.read_csv("data.csv")
except FileNotFoundError:
    print("Eroare: Fișierul 'data.csv' nu a fost găsit.")
    exit()

# Functia pt toate valorile
def plot_all_values():
    plt.figure(figsize=(10, 6))
    plt.plot(data['Durata'], label="Durata", marker='o')
    plt.plot(data['Puls'], label="Puls", marker='x')
    plt.title("Toate valorile pentru Durata și Puls")
    plt.xlabel("Index")
    plt.ylabel("Valori")
    plt.legend()
    plt.grid()
    plt.show()

# Functia pt primele X valori
def plot_first_x_values():
    x = 6
    plt.figure(figsize=(10, 6))
    plt.plot(data['Durata'][:x], label="Durata", marker='o')
    plt.plot(data['Puls'][:x], label="Puls", marker='x')
    plt.title(f"Primele {x} valori pentru Durata și Puls")
    plt.xlabel("Index")
    plt.ylabel("Valori")
    plt.legend()
    plt.grid()
    plt.show()

# Functia pt ultimele Y valori
def plot_last_y_values():
    y = 9 
    plt.figure(figsize=(10, 6))
    plt.plot(data['Durata'][-y:], label="Durata", marker='o')
    plt.plot(data['Puls'][-y:], label="Puls", marker='x')
    plt.title(f"Ultimele {y} valori pentru Durata și Puls")
    plt.xlabel("Index")
    plt.ylabel("Valori")
    plt.legend()
    plt.grid()
    plt.show()

# Meniu
while True:
    print("\nAlege opțiunea:")
    print("1. Toate valorile")
    print("2. Primele 6 valori")
    print("3. Ultimele 9 valori")
    print("4. Ieșire")

    optiune = input("Introdu o opțiune: ")

    if optiune == "1":
        plot_all_values()
    elif optiune == "2":
        plot_first_x_values()
    elif optiune == "3":
        plot_last_y_values()
    elif optiune == "4":
        print("La revedere!")
        break
    else:
        print("Opțiune invalidă. Încearcă din nou.")
