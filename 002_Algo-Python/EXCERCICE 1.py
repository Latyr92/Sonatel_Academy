#Excercice 1
liste=["janvier","février","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]
for i in range(12):	
    print(liste[i])

def trouvermax(t):
    t0=t[0]
    for i in range(1 ,len(t)):
        if t[i]>t0:
            t0=t[i]
    return len(t0)
    

a=trouvermax(liste)


print(a)
t=[]
for i in range(12):
    if len(liste[i])<9:
        k=9-len(liste[i])
        liste[i]=liste[i]+k*' '
    t.append(liste[i])
        
print(t)

liste=t
print("___________________________________________")
for i in range(3):
    print("|"+t[i]+"|",t[i+3]+"|",t[i+6]+"|",t[i+9]+"|")
    print("|_________|__________|__________|__________|")
input("choix option")
for i in range(12):
        if i==1:   
            print("choix 1 pour liste en français")
            break
        elif i==2:
            print("choix 2 pour liste en anglais")
            break





        


   

    

            
