def transform(l,n):
    corresp_c_l=[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
    corresp_l_c=['a','b','c','d','e','f','g','h','i','j']
    if(l>="2" and l<="9"):
        return corresp_c_l[int(l)-2][n]
    elif(l=="0"):
        if(n==1):
            return " "
        else:
            return ""
    elif(l>="a" and l<="j"):
        for i in range(len(corresp_l_c)):
            if(corresp_l_c[i]==l):
                return str(i)
    else:
        return l
        
def parcour_chaine(txt):
    nb=0
    p=""
    for i in range(len(txt)):
        if((i+1<len(txt))):
            if(nb<2 and txt[i]==txt[i+1] ):
                nb+=1
            else:
                p+=transform(txt[i],nb)
                nb=0
        else:
            p+=transform(txt[i],nb)
    return p
#Bonjour aly ⇔ 
txt = "22666066566688777002555999."
#- J’ai 17,5 en algo ⇔ 
txt ="5’244400bh,f0033660025554666."
p=parcour_chaine(txt)
print(p)
