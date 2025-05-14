# generate_languages_bar.py

import matplotlib.pyplot as plt

# 1. Données à personnaliser
languages = {
    "Python": 30,
    "C": 25,
    "JavaScript": 15,
    "C++": 20,
    "Go": 10,
}

# 2. Tri (optionnel) des langages par % décroissant
languages = dict(sorted(languages.items(), key=lambda item: item[1], reverse=True))

# 3. Données pour le graphique
langs = list(languages.keys())
percentages = list(languages.values())

# 4. Création du graphique en colonnes
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(langs, percentages, color="#4CAF50")

# 5. Ajouter les pourcentages au-dessus de chaque barre
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1, f'{height}%', ha='center', va='bottom')

# 6. Titres et étiquettes
ax.set_ylabel("Temps d'attente en ms")
ax.set_title("Langages utilisés")
ax.set_ylim(0, max(percentages) + 10)  # pour laisser de l'espace au-dessus

# 7. Sauvegarde
plt.tight_layout()
plt.savefig("images/score.png")

