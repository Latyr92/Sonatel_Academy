import json

# Charger le fichier JSON
with open('data.json', 'r') as f:
    data = json.load(f)

valid_data = []
invalid_data = []

# Vérifier chaque objet dans le fichier JSON
for obj in data:
    # Vérifier si toutes les clés requises sont présentes dans l'objet JSON
    if all(key in obj for key in ('id', 'name', 'age', 'email')):
        valid_data.append(obj)
    else:
        invalid_data.append(obj)

# Recycler les données valides dans un nouveau fichier JSON
with open('/home/faye/Sonatel_Academy/donnée_projet.csv".json', 'w') as f:
    json.dump(valid_data, f)

# Recycler les données invalides dans un nouveau fichier JSON
with open('invalid_data.json', 'w') as f:
    json.dump(invalid_data, f)