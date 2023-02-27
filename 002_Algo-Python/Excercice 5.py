choix=(input("choisir une couleur: \n"))
matrice=[]
k=""
position=["HAUT","BAS"]
option_1="Rouge"
option_2="Bleu"
# class color:
#     class color:
#         g ="\033[92m" # vert
#         y ="\033[93m" # jaune
#         r ="\033[91m" # rouge
#         n ="\033[0m" #gris, couleur normale
# def colorise(text):
#     couleurs = [ color.g , color.y , color.r ]
#     r = ''
#     i = 0
#     for c in text:
#         if c.upper() == c:
#             r += couleurs[i] + c + color.n
#             i = (i+1) % 3
#         else:
#             r += c
            
#     return r
            
#print( colorise(matrice) )
# #position=int(input("Entrer une option"))
# def position(t):
#     position=""
    

#     for t in position:
#         if t=="1":
#             position="HAUT"
#         elif t=="2":
#             position="BAS"
#         else:
#             position=""
#     return position
# print(position)


ordre_matrice=int(input("donner un ordre_matrice qui est supérieur à 5\n"))
if ordre_matrice<5:
    print("Erreur")
if ordre_matrice>5:
    
    for i in range(ordre_matrice):
        list=[]
        for j in range(ordre_matrice):
           
           
            if i==j:
                k="*"
        
                #list.append(k)
            elif i<j:
                k="-"
                
                #list.append(k)
            else:
                i>j 
                k="*"
            list.append(k) 
            
        matrice.append(list)

if choix=='bleu':
     
    for i in range(ordre_matrice):
        for j in range(ordre_matrice):
            matrice="\033[0;34m B \033[0m"
            if i<j:
                matrice=""
            print(matrice,end=' ')
        print("\n")
elif choix=='rouge':
     
    for i in range(ordre_matrice):
        for j in range(ordre_matrice):
            matrice="\033[0;34m R \033[0m"
            if i>j:
                matrice=""
            print(matrice,end=' ' )
        print("\n")
#for i in option:

    #     print(option)

# for i in matrice:
#     for j in matrice:
print(matrice)
# print("\n")
# def colorise(matrice):
#from colorama import Back ,Fore ,Style ,deinit, init
# c=[Back,for,style]
# for i in range(ordre_matrice):
     
#     if i<j:
# #         list+=k
#      print(Fore.RED+ "")
#     print(Fore.GREEN+ "-")

    
# console = Console()
# console.print("diagonale haut", style="bold yellow")
# console.print("diagonale bas" ,style="bold cyan")
        

#for i in matrice:
#     # list=[]
#     # for j in matrice:
#     #    if j!=",":
#     #         k="*"  
#     #         var+=k
    #print(i)