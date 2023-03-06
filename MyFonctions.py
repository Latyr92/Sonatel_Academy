import csv
import re
fichier="/home/faye/Sonatel_Academy/Donnees_Projet_Python_DataC5.csv"
#Afficher les donnees depuis le fichier csv
with open(fichier, 'r') as monlecteur:
    monlecteur_csv = csv.reader(monlecteur, delimiter= ",")
    fichier=[ligne for ligne in monlecteur_csv]
    def valider_numero(numero):
        #verifier que le numero a une taille 7 caractères
        if len(numero) != 7:
            return False
        #verifier que le numero contient seulement des chiffres  et- des lettres
        if not numero.isalnum():
            return False
        else:
            return True
#fonctiojn pour valider le nom et le prenom de l'élève
    def valider_nom(nom):
    #verifierv que le nom ou le prenom commence par une lettre
        if not nom[0].isalpha():
            return False
        #verifier que le nom ou le prenom contient au moins 2 ou 3 lettres respectivement
        if len(nom) < 2 :
            return False
        else:
            return True
    def valider_prenom(prenom):
        if not prenom[0].isalpha():
            return False
        if not len(prenom) < 3:
            return False
        else:
            return True 
    #fonction pour valider la date de naissance l'élève
    def valider_date_de_naissance(date_naissance):
        #verifier que la date est au format JJ/MM/AAAA
        try:
            jour, mois, annee = date_naissance.split('/')
            jour, mois, annee = int(jour), int(mois), int(annee)
        except ValueError:
            return False
        #verifier que la date est valide(par exemple,pas de 30fevrier)
        if jour < 1 or jour > 31 or mois < 1 or mois > 12 or annee < 1900 or annee >2099:
            return False
        else:
            return True
    #fonction pour valider la classe de l'éléève
    def valider_classe(classe):
        #remplacer les espace et les ieme,ème,ième,iem etc  par eme
        classe = classe.replace(' ','')
    #verifions les classe valides
        if classe[0] in ["3","4","5","6"] and classe[-1] in ["A","B"]:
            classe = classe[0]+"eme"+classe[-1]
            return classe,True
        else:
            return classe,False
    #fonction pour valider note
    def valide_notes(notes):
    #verifier que le chaque notes est au forme matier[devoir1|devoir2 : examen]
        for note in notes.splite("#"):
            if not re.match(r'^[A-Za-z]+\[\d+\|\d+:\d+\]$', note):
                return False
        return True


# fichier="/home/faye/Sonatel_Academy/Donnees_Projet_Python_DataC5.csv"
# #Afficher les donnees depuis le fichier csv
# with open(fichier, 'r') as monlecteur:
#     monlecteur_csv = csv.reader(monlecteur, delimiter= ",")
#     fichier=[ligne for ligne in monlecteur_csv]
    for ligne in monlecteur_csv:
      f=valider_classe(ligne[5])
      print(f)
 


#    #============================================================================== 
# #fonction pour valider les notes de l'élève
# fichier="/home/faye/Sonatel_Academy/Donnees_Projet_Python_DataC5.csv"
# notes_eleves= 'SVT[12|20:19] #PC[13|14:10] #Francais[14|18:19] #Anglais[14|15:18] #HG[10|07:20] #Math[19|17:18]'.split('#')
# eleve = ['AMG015', 'SONA003', 'DIOP', 'YOUSSOU', '12/06/94', '5emA', 'Math[04|03:05] #Francais[15|16:14] #Anglais[15|16:17] #PC[04|03:07] #SVT[12|09:10] #HG[16|15:17]']
# #def transformer_csv_en_liste_de_liste(eleves):
# def valider_notes(notes_eleves):
    
#     #verifier que chaque note est format[devoir1|devoir2:examen]
#     with open(fichier,"r") as monlecteur:
#         monlecteur_csv = reader(monlecteur, delimiter= ",")
#         liste_eleve = []
      
#         for ligne in monlecteur_csv:
#             #liste_eleve = []
#             #print(ligne)
#             liste_eleve.append(ligne)
#         return liste_eleve
#         #print(liste_eleve)

# #valider_notes(fichier)
#        #list_eleve.append(ligne)
#     #return list_eleve
#   # Retourne une liste de liste d'èleves

# def DictMatiere(notes_eleves):
#   try:
#     tmp = notes_eleves.replace("[","-").replace("|","-").replace(":","-").replace("]","-").split("-")
#     del tmp[-1]
#     return {tmp[0]:{
#         "devoir": [float(x) for x in tmp[1:-1]],
#         "examen": float(tmp[-1])
#     }}
#   except ValueError:
#      return 

# def TransformerNoteEnDictionnaire(notes):
#   matieres = {}
#   for n in notes:
#     m = DictMatiere(n)
#     matieres.update(m)
#   return matieres


# dict_note = TransformerNoteEnDictionnaire("Math[04|03:05] #Francais[15|16:14] #Anglais[15|16:17] #PC[04|03:07] #SVT[12|09:10] #HG[16|15:17]".split("#"))
# def TransformerEleveEnDictionnaire(eleve):
#   try:
#     return {
#         "code": eleve[0],
#         "numero": eleve[1],
#         "nom":eleve[2],
#         "prenom": eleve[3],
#         "date_de_naissance": eleve[4],
#         "classe": eleve[5],
#         "notes": TransformerNoteEnDictionnaire(eleve[6].split("#"))
#     }
#   except ValueError:
#      return False
# def calcul_de_la_moyenne(eleve):
#     somme_des_devoir = 0.0
#     for n in eleve["notes"]:
#         devoir = eleve["notes"][n]["devoir"]
#         nombre_de_devoir = len(devoir)
#         for i in range(len(devoir)):
#             somme_des_devoirs += i
#         # La moyenne des devoirs d'une seule matière
#         moyenne_des_devoir=somme_des_devoirs / nombre_de_devoir
#         # La moyenne générale d'une seule matière
#         moyenne_general = (moyenne_des_devoir+(2*eleve["notes"][n]["examen"])) / 3
#         somme_des_moyennes += moyenne_general
#         print("La moyenne générale en {} est {:.2f}".format(n,moyenne_general))
#     moyenne = somme_des_moyennes/len(eleve["notes"])
#     return devoir,moyenne_general
#     #print("La moyenne de {} {} {} {} {} {} {} est {:.2f}".format(eleve["nom"], eleve["prenom"], eleve["numero"], eleve["code"], eleve["classe"], eleve["date_de_naissance"], moyenne, moyenne_general))

     
# #Eleve= TransformerEleveEnDictionnaire("eleve")
# all = valider_notes("eleve")
# # print(type(all[-1][6]))
# tab_eleves = []
# for i in all:
#   Eleve = TransformerEleveEnDictionnaire(i)
#   tab_eleves.append(Eleve)

# good_eleves = []
# bad_eleves = []
# def lesnotes(note_des_eleve):
#      #for i in e["note"]:
#      for i in note_des_eleve:
#       try:
#         good_eleves.append(i)
#         #print(good_eleves)
#       except Exception as e:
#         bad_eleves.append(i)

# def Ouvrir(fichier):
#    tab_invalide = []
#    tab_valide = []
#    with open(fichier,"r") as monlecteur:
#     monlecteur_csv = reader(monlecteur, delimiter= ",")
#     for ligne in monlecteur_csv:
#         if valider_numero == True:
#            tab_valide.append(i)
#         else:
#            tab_invalide
#     return tab_valide,tab_invalide

# valide,invalide = Ouvrir(fichier)
# print(valide)
    
    

        
        
# # lesnotes(good_eleves)

# # good_eleves = []
# # bad_eleves = []
# # for el in tab_eleves:
# #   print(el)
# #     for note in notes.split('#'):
# #         if not re.match(r'^[A-Za-z]+\[\d+\|\d+:\d+\]$', note):
# #             return False
# #     else:
# #         return True
# #fonction calcul moyenne de l'élève
# def calcul_moyenne(notes):
#     moyenne_general=0
#     somme=0.0
#     for note in notes.split('#'):
#         matieres,notes_devoirs,note_examen = re.match(r'^([A-Za-z]+)\[(\d+)\|(\d+):(\d+)\]$', note).group()
#         notes_devoirs = re.match(r'^(\d+)\|(\d+))')
#         for i in range(len(notes_devoirs)):
#           somme += notes_devoirs[i]
#           moyenne = somme / len(notes_devoirs)
#     moyenne_general+= (moyenne+2*float(note_examen))/3
#     return notes_devoirs, note_examen, moyenne_general 
#lire les donnees depuis le fichier csv
#fichier='/home/faye/Documents/Donnees_Projet_Python_DataC5.csv'
#fichier='/home/faye/Documents/Donnees_Projet_Python_DataC5.csv'
#def ouvrir(fichier):
#definition des expression regulier pour verification
# def menu(choix):
    
# # #tableau pour les donnéés valides et invalides 
# #fichier=
# # tab_valide=[]
# # tab_invalide=[]
# # def ouvrir(fichier):
   
# # #ouverture du fichier contenant les donnees des eleves 
# #     with open('/home/faye/Documents/Donnees_Projet_Python_DataC5.csv', 'r') as monlecteur:
# #      monlecteur_csv = reader(monlecteur,delimiter = ',')
# #     # for i in monlecteur_csv:
# #     #     print(i)
     
# #      #lecture des ligne
# #      for i in monlecteur_csv:
# #      #supression d'espace en debut et fin de ligne
# #       #line=line.strip()
# #      #separation des donnees de la ligne
# #       #monlecteur_csv=line.split(',')
# #      #verification validité des donnees 
# #       numero_valide = bool(re.match(NUMERO_REGEX, i[1]))
# #       nom_valide = bool(re.match(NOM_REGEX, i[2]))
# #       prenom_valide = bool(re.match(PRENOM_REGEX, i[3]))
# #       date_valide = bool(re.match(DATE_REGEX, i[4]))
# #       classe_valide = bool(re.match(CLASSE_REGEX, i[5]))
# #      #verification de validiter des notes
# #       notes_valides = True
# #       moyenne=0.0
# #       #somme = 0.0
# #       for note in i[6:]:
# #             note.split('#')
# #             note_valide = bool(re.match(NOTE_REGEX, note))
# #             if not note_valide:
# #              notes_valides = False
# #              break
# #             else:
# #              note_devoir, note_examen = note.split('|') if '|' in note else(note, '0')
# #              note_devoir = float(note_devoir)
# #              note_examen = float(note_examen.split(':')[0])
# #              moyenne += (note_devoir+ 2 * note_examen) / 3
# # #si toutes les donnees sont valides on ajoute la ligne avec la moyenne au tableau des donnees valides
# #       if valider_numero== True and valider_nom_prenom == True and valider_date_de_naissance == True and valider_classe == True and valider_notes == True:
# #         classe=monlecteur_csv[5].replace('eme ', 'eme').replace('ieme ','eme')
# #      #print(i)
# #     tab_valide.append({'code': i[0],
# #                         'numero': i[1],
# #                         'nom': i[2],
# #                         'prenom': i[3],
# #                         'date_de_naissance':i[4],
# #                         'classe': i[5],
# #                         'notes': i[6:],
# #                         'moyenne': moyenne/len(i[6:])
# #                         })
    
# #print(tab_valide)
#     #   else:
#     #      tab_invalide.append(i)
#     #      print(tab_invalide)

# #menu pour affichage des donnees 
# fichier='/home/faye/Documents/Donnees_Projet_Python_DataC5.csv'
# def ouvrir(fichier):
#     tab_valide=[]
#     tab_invalide=[]
#     with open(fichier,'r') as monlecteur:
#         monlecteur_csv = reader(monlecteur,delimiter = ',')
#         #donnees=[ligne for ligne in monlecteur_csv]
#         for i in monlecteur_csv:
#             #print(donnees)
#             if valider_numero == True and valider_nom_prenom == True and valider_date_de_naissance == True and  valider_notes == True and valider_classe == True:
#                 tab_valide.append(i)
#             else:
#                 tab_invalide.append(i)
#         return tab_valide, tab_invalide


# valide, invalide = valider_notes(fichier)
# print(invalide)
     
# #Aficher le menu
# while True:
#         choix = input('que voulais-vous afficher ?(1: donnees valides, 2: donnees invalides, 3: quitter)') 

        
            
    
    
     
        
                                               
                                              
        
              
                                          