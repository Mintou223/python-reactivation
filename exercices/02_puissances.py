''' calcul de la puissance reçue par chacune des résistances, pour pratiquer la manipulation de dictionnaires en Python'''

import math
    
u=12
res={"R1": 100, "R2": 220, "R3": 470}
r_eq=sum(res.values())#circuit en série
I=u/r_eq #circuit en série
power={P: R*I**2 for P,R in res.items()}#calcul de la puissance reçue par chaque résistance en W

for k, v in power.items():
    n = res.get(k, "résistance inconnue")
    print(f"{k}: {n} \u03A9 --> {v*10**3:.2f} mW") #passage en mW

print(f"La résistance qui reçoit le plus de puissance est: {max(power, key=power.get)}")

if math.isclose(u*I,sum(power.values())):
    print("La loi de conservation de l'énergie est vérifiée")
