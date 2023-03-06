import csv
from MyFonctions import *


class Etudiant:
    def __init__(self, code, numero,nom, prenom, date_naissance, classe, notes):
        self.code = code
        self.numero = numero
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.classe = classe
        self.notes = notes.split("#")
    def est_valide(self):
        # Vérification de la validité de chaque attribut de l'objet Eleve
        if not isinstance(self.numero, str) or not self.numero.isalnum() or len(self.numero) != 7:
            return False
        else:
            True
        if not isinstance(self.nom, str) or not self.nom.isalpha() or len(self.nom) < 2:
            return False
        else:
            True
        if not isinstance(self.prenom, str) or not self.prenom.isalpha() or len(self.prenom) < 3:
            return False
        else:
            True
        if not isinstance(self.date_naissance, str):
            return False
        else:
            True
        if not isinstance(self.classe, str):
            return False
        else:
          True
        if not isinstance(self.notes, str):
            return False
        else:
          True
        # Vérification de la validité de chaque note de devoir et de la note d'examen
        for note in self.notes.split('#'):
            if len(note.split('|')) != 2 or ':' not in note.split('|')[1]:
                return False
            for n in note.split('|'):
                if not n.replace(':', '', 1).isdigit():
                    return False
        # Extraction des notes de devoir et de la note d'examen
        for note in self.notes.split('#').split("["):
            
            self.devoirs.append(float(note.split('|')[0]))
            if self.examen is None:
                self.examen = float(note.split('|')[1].split(':')[1])
            else:
                self.examen += float(note.split('|')[1].split(':')[1])
        # Calcul de la moyenne des devoirs et de la moyenne générale
        self.moyenne_devoir = sum(self.devoirs) / len(self.devoirs)
        self.moyenne_generale = (self.moyenne_devoir + 2 * self.examen) / 3
        return True

    
    def afficher(self):
        print(f"{self.numero} - {self.nom} {self.prenom} ({self.date_naissance}) {self.classe} {self.notes}:")
#         print(f"\tNote devoir: {self.note_devoir}")
#         print(f"\tNote examen: {self.note_examen}")


fichier = "/home/faye/Sonatel_Academy/donnée_projet.csv" 

def lire_fichier_csv(nom_fichier):
    etudiants = []
    with open(fichier, newline='') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv, delimiter=',')
        for ligne in lecteur_csv:
            code = ligne[0]
            numero = ligne[1]
            nom= ligne[2]
            prenom = ligne[3]
            date_naissance = ligne[4]
            classe = ligne[5]
            notes = ligne[6]
            etudiant = Etudiant(code, numero, nom, prenom, date_naissance, classe, notes)
            etudiants.append(etudiant)
    return etudiants

if __name__ == "__main__":
    etudiants = lire_fichier_csv("etudiants.csv")
    for etudiant in etudiants:
        etudiant.afficher()
