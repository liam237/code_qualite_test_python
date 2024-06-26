import pandas as pd

# Liste d'exemple avec quelques équipes (les données doivent être mises à jour avec des sources fiables)
equipes = [
    {"nom_equipe": "Paris Saint-Germain", "age_moyen": 26.5, "poids_moyen": 75.3, "valeur_marchande": 950.0, "nombre_victoires": 28, "nombre_trophées": 45},
    {"nom_equipe": "Olympique de Marseille", "age_moyen": 27.2, "poids_moyen": 76.1, "valeur_marchande": 320.0, "nombre_victoires": 21, "nombre_trophées": 26},
    {"nom_equipe": "AS Monaco", "age_moyen": 25.9, "poids_moyen": 74.5, "valeur_marchande": 350.0, "nombre_victoires": 22, "nombre_trophées": 10},
    {"nom_equipe": "Olympique Lyonnais", "age_moyen": 25.7, "poids_moyen": 73.8, "valeur_marchande": 290.0, "nombre_victoires": 18, "nombre_trophées": 18},
    # Ajouter les autres équipes...
]

# Conversion des données en DataFrame pandas
df = pd.DataFrame(equipes)

# Sauvegarde du DataFrame en fichier Excel
df.to_excel("ligue1_2023_2024.xlsx", index=False)

print("Le fichier Excel a été créé avec succès.")
