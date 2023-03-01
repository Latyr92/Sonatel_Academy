import re

# Définition des expressions régulières pour les vérifications
NUMERO_REGEX = r'^[A-Z0-9]{7}$'
NOM_REGEX = r'^[a-zA-Z]{2,}$'
PRENOM_REGEX = r'^[a-zA-Z]{3,}$'
DATE_REGEX = r'^\d{2}/\d{2}/\d{4}$'
CLASSE_REGEX = r'^[3456]eme?[A-Z]$'
NOTE_REGEX = r'^\d{1,2}(\|\d{1,2}:\d{2})?$'

# Tableaux pour les données valides et invalides
donnees_valides = []
donnees_invalides = []

# Ouverture du fichier contenant les données des élèves
with open('/home/faye/Documents/Donnees_Projet_Python_DataC5.csv.txt', 'r') as f:

    # Lecture des lignes du fichier
    for line in f:
        
        # Suppression des espaces en début et fin de ligne
        line = line.strip()
        
        # Séparation des données de la ligne
        data = line.split(',')
        
        # Vérification de la validité des données de la ligne
        numero_valide = bool(re.match(NUMERO_REGEX, data[1]))
        nom_valide = bool(re.match(NOM_REGEX, data[2]))
        prenom_valide = bool(re.match(PRENOM_REGEX, data[3]))
        date_valide = bool(re.match(DATE_REGEX, data[4]))
        classe_valide = bool(re.match(CLASSE_REGEX, data[5]))
        
        # Vérification de la validité des notes
        notes_valides = True
        moyenne = 0
        for note in data[6:]:
            note_valide = bool(re.match(NOTE_REGEX, note))
            if not note_valide:
                notes_valides = False
                break
            else:
                note_devoir, note_examen = note.split('|') if '|' in note else (note, '0')
                note_devoir = int(note_devoir)
                note_examen = int(note_examen.split(':')[0])
                moyenne += (note_devoir + 2 * note_examen) / 3
        
        # Si toutes les données sont valides, on ajoute la ligne avec la moyenne au tableau des données valides
        if numero_valide and nom_valide and prenom_valide and date_valide and classe_valide and notes_valides:
            classe = data[5].replace('eme ', 'eme').replace('ieme ', 'ieme')
            donnees_valides.append({
                'code': data[0],
                'numero': data[1],
                'nom': data[2],
                'prenom': data[3],
                'date_naissance': data[4],
                'classe': classe,
                'notes': data[6:],
                'moyenne': moyenne / len(data[6:])
            })
        
        # Sinon, on ajoute la ligne au tableau des données invalides
        else:
            donnees_invalides.append(line)

# Menu pour l'affichage des données
while True:
    choix = input('Que voulez-vous afficher ? (1: données valides, 2: données invalides, 3: quitter) ')
#     if choix == '1':
#         for eleve in donnees_valides:
#             print(f"{eleve['prenom']}