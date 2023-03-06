import re, csv
from MyFonctions import *
def Calcul_moyenne(notes):
    moyenne = 0.0
    for note in notes.split("#"):
        matiere, note_devoir, note_examen = re.match(r"^([A-Za-z]+)\[(\d+)\|(\d+):(\d+)\]$", note).group()
        moyenne += (float(note_devoir) + 2*float(note_examen))
        return note_devoir, note_examen, moyenne
fichier="/home/faye/Sonatel_Academy/Donnees_Projet_Python_DataC5.csv"
#Afficher les donnees depuis le fichier csv
with open(fichier, 'r') as monlecteur:
    monlecteur_csv = csv.reader(monlecteur, delimiter= ",")
    fichier=[ligne for ligne in monlecteur_csv]
    print(fichier)

# def valider_notes(note):
#     note= note.split("#")
#     #verifier que chaque note est format[devoir1|devoir2:examen]
#     # for i in note.split('#'):
#     #     if not re.match(r'^[A-Za-z]+\[\d+\|\d+:\d+\]$', note):
#     #         return False
#     return note

# # Définition des expressions régulières pour les vérifications des
# NUMERO_REGEX = r'^[A-Z0-9]{7}$'
# NOM_REGEX = r'^[a-zA-Z]{2,}$'
# PRENOM_REGEX = r'^[a-zA-Z]{3,}$'
# DATE_REGEX = r'^\d{2}/\d{2}/\d{4}$'
# CLASSE_REGEX = r'^[3456]eme?[A-Z]$'
# NOTE_REGEX = r'^\d{1,2}(\|\d{1,2}:\d{2})?$'

# Tableaux pour les données valides et invalides
# donnees_valides = []
# donnees_invalides = []

# # Ouverture du fichier contenant les données des élèves
# with open('/home/faye/Documents/Donnees_Projet_Python_DataC5.csv', 'r') as monlecteur:
#     monlecteur_csv = csv.reader(monlecteur)

#     # Lecture des lignes du fichier
#     for i  in monlecteur_csv:
        
#         # print(i)
        
#         #Suppression des espaces en début et fin de ligne
#         #line = line.strip()
        
#         # Séparation des données de la ligne
#         #monlecteur_csv= line.split(',')
        
#         #Vérification de la validité des données de la ligne
#         numero_valide = bool(re.match(NUMERO_REGEX, i[1]))
#         nom_valide = bool(re.match(NOM_REGEX, i[2]))
#         prenom_valide = bool(re.match(PRENOM_REGEX, i[3]))
#         date_valide = bool(re.match(DATE_REGEX, i[4]))
#         classe_valide = bool(re.match(CLASSE_REGEX, i[5]))
        
#         # Vérification de la validité des notes
#         note_valide = True
#         moyenne = 0.0
#         for note in monlecteur_csv:
            
#             note_valide = bool(re.match(NOTE_REGEX, note))
#             if not note_valide:
#                 note_valide = False
#                 break
#             else:
#                 note_devoir, note_examen = note.split('|') if '|' in note else (note, '0')
#                 note_devoir = float(note_devoir)
#                 note_examen = float(note_examen.split(':')[0])
#         moyenne += (note_devoir + 2 * note_examen) / 3
        
#         # Si toutes les données sont valides, on ajoute la ligne avec la moyenne au tableau des données valides
#         if numero_valide and nom_valide and prenom_valide and date_valide and classe_valide:
#             classe = i[5].replace('eme ', 'eme').replace('ieme ', 'ieme')
#             donnees_valides.append({
#                 'code': i[0],
#                 'numero': i[1],
#                 'nom': i[2],
#                 'prenom': i[3],
#                 'date_naissance': i[4],
#                 'classe': classe,
#                 'notes': note_examen,
#                 'notes' : note_examen,
#                 'moyenne': moyenne / len(i[6:])
#             })
        
#         # Sinon, on ajoute la ligne au tableau des données invalides
#         else:
#             donnees_invalides.append(i)
        

# # Menu pour l'affichage des données
#         while True:
#             choix = input('Que voulez-vous afficher ? (1: données valides, 2: données invalides, 3: quitter) ')
#             if choix == '1':
#                 for eleve in donnees_valides:
#                     print(donnees_valides)
#             else:
#                 print(donnees_valides)
#     for i in monlecteur_csv:
#         f=valider_notes(i[6])
#         print(f)