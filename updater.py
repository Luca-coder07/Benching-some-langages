# generate_languages_pie.py

import matplotlib.pyplot as plt

# 1. Données (à adapter selon ton dépôt GitHub)
languages = {
    "Python": 40,
    "C": 25,
    "JavaScript": 15,
    "C++": 10,
    "Go": 10,
}

# 2. Préparation
labels = [f"{lang} ({pct}%)" for lang, pct in languages.items()]
sizes = list(languages.values())
colors = plt.cm.tab20.colors[:len(languages)]  # palette de couleurs

# 3. Création du graphe
fig, ax = plt.subplots()
ax.pie(
    sizes,
    labels=labels,
    autopct=None,
    startangle=90,
    colors=colors,
    counterclock=False,
)
ax.axis("equal")  # Cercle parfait
plt.title("Langages utilisés (en %)")

# 4. Sauvegarde
plt.tight_layout()
plt.savefig("images/score.png")

