#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv","r") as fichier:
    contenu = pd.read_csv(fichier)

# Question 5
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv","r") as fichier:
    contenu = pd.read_csv(fichier)

print(contenu)

# question 6
nb_lignes = len(contenu)
nb_colonnes = len(contenu.columns)

print("Nombre de lignes :", nb_lignes)
print("Nombre de colonnes :", nb_colonnes)

# Réponse Nombre de lignes : 107, Nombre de colonnes : 56

#Question 7
listedestypes=contenu.dtypes
print(listedestypes)

#Question 8
print(contenu.head(1))

#Question 9 : 438109 inscrits

#Question 10
liste_sommes = []

for colonne in contenu.columns:
    if contenu[colonne].dtype in ["int64", "float64"]:
        somme = contenu[colonne].sum()   
        somme = int(somme) if contenu[colonne].dtype == "int64" else float(somme)
        liste_sommes.append((colonne, somme))  
print(liste_sommes)
