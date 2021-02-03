import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def funkcja(x,p):
    return np.sin(x)*np.cos(x*p)

min_wartosc_calki = 1000 #zmienna do przetrzymywania najmniejszej uzyskanej wartości całki
wartosc_p = 0            #zmienna do przetrzymywania wartośći p dla której uzyskaliśmy najmniejszą wartość całki

p_tablica = []     #tablica do której przekazuje wartości p
calka_tablica = [] #tablica do której wartości całki

n = 1e-5

zakres=np.arange(0,10+n,n)


for p in zakres:
    calka=quad(funkcja,0,np.pi,args=p) #wartości zmiennej p przekazuję do funkcji quad() ustawiając parametr args=p

    p_tablica.append(p)
    calka_tablica.append(calka[0])

    if calka[0]<min_wartosc_calki:
        min_wartosc_calki = calka[0]
        wartosc_p = p

    print("p = ",p," | ","Wartość całki = ",calka[0])

print("\n")
print("Minimalna wartość całki: ", min_wartosc_calki)
print("Wartość parametru p dla której występuje: ", wartosc_p)

plt.scatter(wartosc_p,min_wartosc_calki, color="red")
plt.plot(p_tablica,calka_tablica)
plt.xlabel("Wartość parametru p")
plt.ylabel("Wartość całki")
plt.legend(("Wykres całki","Wartość minimalna"))
plt.grid()
plt.show()

