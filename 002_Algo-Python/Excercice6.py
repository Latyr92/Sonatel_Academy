matrice=[]
k=""
list=[]
position=["ADDP,EDDP,SDP,ADDS,EDDS,SDS"]
# position=input("choix diagonale")
# option=int(input("entrer un entier pour position couleurs"))
ordre_matrice=int(input("entrer l'ordre de la matrice superieur a 4\n"))
position=input("donner la position \n")
choix_couleur=input("donner une couleur\n")

if ordre_matrice<4:
    print("Erreur")

if ordre_matrice>4:
    
    for i in range(ordre_matrice):
        list=[]
        for j in range(ordre_matrice):
           
           
            if i==j:
                k="+"
        
                #list.append(k)
            elif i<j:
                k="-"
                
                #list.append(k)
            else:
                i>j 
                k="*"
            list.append(k) 
            
        matrice.append(list)
if(position=='SDP'and choix_couleur=='bleu'):
    for i in range(ordre_matrice):
        for j in range(ordre_matrice):
            matrice=""
            if i==j:
                matrice="SDP"
                matrice="\033[0;34m B \033[0m"
            print(matrice,end=' ')
        print("\n")

elif(position=="ADDP"and choix_couleur=='rouge'):
        for i in range(ordre_matrice):
            for j in range(ordre_matrice):
                matrice=""
                if i<j:
                    matrice="ADDP"
                    matrice="\033[0;34m R \033[0m"
                print(matrice,end=' ')
            print("\n")

elif(position=="EDDP"and choix_couleur=='vert'):
        for i in range(ordre_matrice):
            for j in range(ordre_matrice):
                matrice=""
                if i>j:
                    matrice="EDDP"
                    matrice="\033[0;34m V \033[0m"
                print(matrice,end=' ')
            print("\n")

if(position=='SDS'and choix_couleur=='jaune'):
    for i in range((ordre_matrice)):
        for j in range(ordre_matrice):
            matrice=""
            if(i+j==ordre_matrice):
                matrice="SDS"
                matrice="\033[0;34m J \033[0m"
            print(matrice,end=' ')
        print("\n")

elif(position=="ADDS"and choix_couleur=='grise'):
        for i in range(ordre_matrice):
            for j in range(ordre_matrice):
                matrice=""
                if i+j<(ordre_matrice):
                    matrice="ADDs"
                    matrice="\033[0;34m G \033[0m"
                print(matrice,end=' ')
            print("\n")

elif(position=="EDDS"and choix_couleur=='orange'):
        for i in range(ordre_matrice):
            for j in range(ordre_matrice):
                matrice=""
                if i+j>(ordre_matrice):
                    matrice="EDDS"
                    matrice="\033[0;34m O \033[0m"
                print(matrice,end=' ')
            print("\n")
else:

    for i in matrice:
        print(matrice)
        

    # def diag_principale(h):
    #     matrice=[]
    #     vars=[]
    #     k=""
    
    #     # for t in position:
    #     #     for n in option:
    #     for i in range(1,ordre_matrice):
    #         for j in range(1,ordre_matrice):
    #             if i==j:
    #                 k="SDP"
    #                 vars+=k
    #                 matrice.append(k)
    #             elif i<j:
    #                 k="ADDP"
    #                 vars+=k
    #                 matrice.append(k)
    #             elif i>j:
    #                 k="EDDP"
    #                 vars+=k
    #                 matrice.append(k)
    #     return matrice
    #print(matrice)
                    
#                     else:
#                         i>j
#                     vars+=k
#                     matrice.append(k)

#         return matrice
# l=diag_principale(ordre_matrice)
# def choix_couleur(p):
#     for t in position:
        # for n in option:
        #     if 
            
                       



            
