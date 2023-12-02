import pandas as pd

# Chargez le fichier CSV dans un DataFrame
df = pd.read_csv('votre_fichier.csv')

# Supprimez les lignes en double
df.drop_duplicates(inplace=True)

# Supprimez les lignes avec des valeurs manquantes (NaN)
df.dropna(inplace=True)

# Enregistrez le DataFrame nettoyé dans un nouveau fichier CSV
df.to_csv('votre_fichier_nettoye.csv', index=False)

print("Base de données nettoyée et enregistrée avec succès.")
