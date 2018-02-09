def MinToMax(a, res):
    #Algorithme pour calculer le plus petit chifre 
    for j in range(0,len(a)):
        mini = a[0]
        k = 0
        for i in range(1,len(a)):
            if mini > a[i]:
                mini = a[i]  
                k = i          
        #je le met dans le tableau res        
        res[j] = mini
        #je detruie le plus petit
        a[k] = 100000 
    
def MaxToMin(a, res):
    #Algorithme pour calculer le plus grand chifre 
    for j in range(0,len(a)):
        mini = a[0]
        k = 0
        for i in range(1,len(a)):
            if mini < a[i]:
                mini = a[i]  
                k = i          
        #je le met dans le tableau res        
        res[j] = mini
        #je detruie le plus grand
        a[k] = 0 

            

