import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# IMPORTATION DE LA BASE DE DONNEES
Athletes = pd.read_csv("C:\Users\gaidi\OneDrive\Documents\ESILV quentin\Espagne\GINDRE GAIDIER GOURJAULT FALEMPIN STATISTIQUES\GINDRE GAIDIER GOURJAULT FALEMPIN STATISTIQUES\athlete_events.csv", sep=';')

# Nettoyage des données
Athletes = Athletes.dropna(subset=['Age', 'Height', 'Weight'])

# PREMIERE ANALYSE DES DONNEES

# Répartition homme femme moyene
sexe_counts = Athletes['Sex'].value_counts()
plt.pie(sexe_counts, labels=sexe_counts.index, colors=['pink', 'blue'], autopct='%1.1f%%')
plt.title('Répartition homme femme moyenne')
plt.show()

# Répartition homme femme au fur et à mesure des années
gender_counts = Athletes.groupby(['Year', 'Sex']).size().unstack(fill_value=0)
gender_proportions = gender_counts.div(gender_counts.sum(axis=1), axis=0)
plt.plot(gender_proportions.index, gender_proportions['F'], color='pink', label='Femmes')
plt.plot(gender_proportions.index, gender_proportions['M'], color='blue', label='Hommes')
plt.xlabel('Année')
plt.ylabel('Proportion')
plt.title('Répartition homme femme au fil des années')
plt.legend()
plt.show()

# Verification des moyennes d'âge
mean_age_femmes = Athletes[Athletes['Sex'] == 'F']['Age'].mean()
mean_age_hommes = Athletes[Athletes['Sex'] == 'M']['Age'].mean()
mean_age_total = Athletes['Age'].mean()

# Première analyse de l'âge des athlètes
age_summary = Athletes['Age'].describe()
plt.hist(Athletes['Age'], bins=range(10, 101, 5), edgecolor='black')
plt.xlabel('Âge')
plt.ylabel('Nombre total selon catégorie')
plt.show()

# Moyenne d'âge par année
mean_age_by_year = Athletes.groupby('Year')['Age'].mean()
plt.plot(mean_age_by_year.index, mean_age_by_year.values, color='blue', label='Âge moyen')
plt.axhline(mean_age_total, color='red', linestyle='dashed', label='Âge moyen total')
plt.xlabel('Année')
plt.ylabel('Âge moyen')
plt.title('Moyenne d\'âge des athlètes aux JO par année')
plt.legend()
plt.show()

# Moyenne d'âge par sport
mean_age_by_sport = Athletes.groupby('Sport')['Age'].mean().sort_values()
plt.plot(mean_age_by_sport.index, mean_age_by_sport.values, color='blue', label='Âge moyen')
plt.axhline(mean_age_total, color='red', linestyle='dashed', label='Âge moyen total')
plt.xlabel('Sport')
plt.ylabel('Âge moyen')
plt.title('Moyenne d\'âge des athlètes aux JO par sport')
plt.xticks(rotation=90)
plt.legend()
plt.show()

# Proportion d'athlètes dans les sports où l'âge moyen est plus élevé
selected_sports = ["Alpinism", "Art Competitions", "Roque", "Croquet", "Motorboating",
                   "Polo", "Shooting", "Jeu De Paume", "Equestrianism", "Curling"]

proportion_high_age_sports = Athletes[Athletes['Sport'].isin(selected_sports)]['Sport'].value_counts(normalize=True).sum()

# Moyenne d'âge des médaillés d'or
gold_medals = Athletes[Athletes['Medal'] == 'Gold']
mean_age_gold_medals_by_year = gold_medals.groupby('Year')['Age'].mean()
plt.plot(mean_age_gold_medals_by_year.index, mean_age_gold_medals_by_year.values, color='blue')
plt.xlabel('Année')
plt.ylabel('Âge moyen des médaillés d\'or')
plt.title('Moyenne d\'âge des médaillés d\'or aux JO par année')
plt.show()

# Moyenne de taille et de poids
mean_height_by_year = Athletes.groupby('Year')['Height'].mean()
mean_weight_by_year = Athletes.groupby('Year')['Weight'].mean()

plt.plot(mean_height_by_year.index, mean_height_by_year.values, color='blue', label='Taille moyenne')
plt.axhline(Athletes['Height'].mean(), color='red', linestyle='dashed', label='Taille moyenne totale')
plt.xlabel('Année')
plt.ylabel('Taille moyenne')
plt.title('Moyenne de taille des athlètes aux JO par année')
plt.legend()
plt.show()

plt.plot(mean_weight_by_year.index, mean_weight_by_year.values, color='blue', label='Poids moyen')
plt.axhline(Athletes['Weight'].mean(), color='red', linestyle='dashed', label='Poids moyen total')
plt.xlabel('Année')
plt.ylabel('Poids moyen')
plt.title('Moyenne de poids des athlètes aux JO par année')
plt.legend()
plt.show()


