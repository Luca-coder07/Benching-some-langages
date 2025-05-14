# generate_languages_bar.py

import matplotlib.pyplot as plt

def lire_donnees_depuis_fichier(nom_fichier):
    """Lit un fichier contenant des langages et pourcentages"""
    data = {}
    with open(nom_fichier, 'r') as f:
        for ligne in f:
            if ':' in ligne:
                nom, valeur = ligne.strip().split(':')
                try:
                    data[nom.strip()] = float(valeur.strip())
                except ValueError:
                    print(f"Ignoré: ligne invalide → {ligne.strip()}")
    return data

# 1. Lecture depuis le fichier
languages = lire_donnees_depuis_fichier("data/data.txt")

# 2. Tri (optionnel) des langages par % décroissant
#languages = dict(sorted(languages.items(), key=lambda item: item[1], reverse=True))

# 3. Données pour le graphique
langs = list(languages.keys())
valeurs = list(languages.values())

# 4. Création du graphique en colonnes
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(langs, valeurs, color="#4CAF50")

# 5. Ajouter les pourcentages au-dessus de chaque barre
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1, f'{height}ms', ha='center', va='bottom')

# 6. Titres et étiquettes
ax.set_ylabel("Temps d'attente en ms")
ax.set_title("Langages utilisés")
ax.set_ylim(0, max(valeurs) + 10)  # pour laisser de l'espace au-dessus

# 7. Sauvegarde
plt.tight_layout()
plt.savefig("images/score.png")

