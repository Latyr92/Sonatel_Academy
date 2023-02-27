matrice=[]
opérateur_tél=input("donner la liste des opérateur télephonique séparer par des virgules")
information=input("donner le nom et prénom du client")
numero=input("donner le numero téléphone du client")
#for i in opérateur_tél:
    #print(opérateur_tél)

def det_op(t):
    client=[]
    nom=str
    prenom=str
    numero=[]
    ch=["77","78","76","75","70"]
    for numero in t:
        if opérateur_tél=="orange"and numero[:2]=="77":
            client.append(opérateur_tél)
        elif opérateur_tél=="tigo"and numero[:2]=="76":
            client.append(opérateur_tél)

        elif((opérateur_tél=="expresso") and (numero[:2])=="70"):
            client.append(opérateur_tél)
        elif((opérateur_tél=="promobile")and (numero[:2]=="75")):
            client.append(opérateur_tél)
        elif((opérateur_tél=="kirene")and (numero[:2]=="78")):
            client.append(opérateur_tél)
            return client

#print(l)
def client(c):
    for i in range(opérateur_tél):
        print("Afficher les clients de la matrice par opérateur")
        print("Afficher les clients d’un opérateur") 
        print("afficher les numéros téléphone d’un client")