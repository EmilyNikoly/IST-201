def Sochetanya(n,m):
    Sochetan(m,0)

def Sochetan(k,nach):
        if k==0:
            for i in range(0,m):
                print(ind[i], end=" ")
            print()
        else:
            for i in range (nach,n-k+1):
                ind[m-k]=el[i]
                Sochetan(k-1,i+1)
n=4
m=2
#Объявление имён
el=["Олег", "Владислав","Степан ","Владимир","Руслан","Евгений"]
ind=[0]*(n)
for i in range (0,n):
    ind[i]=el[i]
Sochetanya(n,m)
