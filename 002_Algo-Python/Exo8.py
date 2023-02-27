tab=input("donner  nom de l'etudiant,prenom")
numero=int(input("donner numero téléphone"))
niveau=input("donner son niveau")
note=(input("donner note devoir"))
note=(input("donner note projet"))
note=(input("donner note examen"))
choix_affichage=int(input("taper un entier pour afficher tous le tableau "))
choix= "2"
    #average=input("entrer la moyenne")                 
#print("\n")
#for i in tab:
print("_________________________________________________________________")
for i in range(len(tab)):
    print("|"+"prenom"+"|","nom"+"|","telephone"+"|","classe"+"|","devoir"+"|","projet"+"|","examen"+"|","moyenne"+"|")
    print("_________________________________________________________________")

def det_note(i):
    # note[0]="note devoir"
    # note[1]="note du projet"
    # note[2]="note de l'examen"
    #sum=""
    note=[]
    #tab=[]
    for i in range(3):
        if(0<=note<=20): 
                  note.append(note)
                  #sum=sum+note[0]+note[1]+note[2]
                  #average=sum/len(note[i])
        return note 
    #print(etudiant)

def calculmoyenne(note):
      tab=[]
      sum=""
      note=[]
      average
      for i in note:
        if note[i]:
            tab.append(note[i])
            sum=sum+note[0]+note[1]+note[2]
            average=sum/len(tab[note])
            print()
        return average
        
def numero(t):
    k=""
    numero=[]
    tab=[]
    for i in t:
         if i=="":
              k+=i
         else:
              numero.append(k)
    return numero

def verification(numero):
     ch=["78","76","70","77","75"],
     for i in numero:
          if len(numero)==9 and numero[:2] in  ch:
            return numero
    
def validation(numero):
     tab=[]
     for i in numero:
          if numero:
               tab.append(numero)

#def trier(moyenne):
        #for i in moyenne:
                   

# l=note(note)
# print(l)
      