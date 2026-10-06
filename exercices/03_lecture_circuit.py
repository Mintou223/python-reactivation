'''manipulation de fichiers .txt'''

with open('data/circuit.txt', 'r') as f:
    contenu=f.read().splitlines()
    #res={cle: valeur for item in contenu for cle, valeur in [item.split("=")]}
    a= [item.split("=") for item in contenu]
print(contenu)
print(a)
