from csv import reader

class Eleve():
    def _init_(self, code, numero, nom, prenom, date_naissance, classe, notes):
        self.code = code
        self.numero = numero
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.classe = classe
        self.notes = notes
        self.devoirs = "a determiner"
        self.examen = "a determiner"
        self.moyenne_devoir = "a determiner"
        self.moyenne_generale = "a determiner"
    notes='Math[14|13:05] #Francais[18|16:14] #Anglais[15|06:17] #PC[14|13:07] #SVT[18|12:16] #HG[13|15:13' 
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



class GestionEleves:
    
    def _init_(self):
        fichier= "/home/faye/sonatel_academy/Donnees_Projet_Python_datac5.csv" 
        self.fichier = fichier
        self.eleves_valides = ["A","B","C"]
        self.eleves_invalides = []

    def afficher_eleves_valides(self):
        for eleve in self.eleves_valides:
            print(f"Numéro: {eleve.numero}, Nom: {eleve.nom}, Prénom: {eleve.prenom}, date_de_naissance: {eleve.date_denaissance}, classe: {eleve.classe}, note: {eleve.notes}")
    

    def lire_fichier(self):
       
        with open(self.fichier, 'r') as f:
            reader = reader(f)

            for row in reader:
                eleve = Eleve(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                if eleve.est_valide():
                    self.eleves_valides.append(eleve)

                    #print(self.eleves_valides)
                else:
                    self.eleves_invalides.append(row)
        return self.eleves_valides,self.eleves_invalides

                  
    
#ligne_eleve= Eleve
v=GestionEleves()
a = v.lire_fichier()
print(a)
#self_eleve_= lire_fichier()
# ligne_eleve._init_()
# ligne_eleve.lire_fichier()

    #lire_fichier(fichier)