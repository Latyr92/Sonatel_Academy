list_num=input("donner des numero séparer par des virgule")
#for i in list_num:
#print(list_num)
#numero[-1]!=";":
def composition(numero):
    k=""
    numero=[]
    for i in numero:
        if i!=";":
            k+=i
        else:
            numero.append(k)
            k=""
    return numero
        
a=composition(list_num)
#print(l)


def validation(numero):
    
    ch="77","78","76","70","75"
    print("choisir numero valide")
    for i in range(len(numero)):
        numero=[]
    if numero(a[i]) :
    
        if i=="":
                k+=i
                numero.append(k)
        if(len(numero)==9 and (numero[:2] in ch)):
                
                numero.append(numero(a[i]))
                print(numero(a[i]), " ",end= ' ')
                
        else:
            #continue
        
            sprint("\n")
    print(  "***************************************************")
    print("numero invalide")
    for i in range(len(numero)):
                numero=[]
                if numero(a[i]):
                    numero.append(numero(a[i]))
                    print(numero(a[i])," ", end= '')

                #print("les nums valides sont :")
            # print(numero)
                #numero_valide.append(numero_valide)
            
#l=validation(list_num)
#print(l)