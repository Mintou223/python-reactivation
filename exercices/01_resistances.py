def serie (resistances):
    r_eq = sum(resistances)
    return round(r_eq,2)

def parallele(resistances):
    invr_eq = 0
    for r in resistances:
        invr_eq = invr_eq + (1/r)
    return round(1/invr_eq,2)

print("Resistances in series:", serie([100,220,470]), "Ohms")
print("Resistances in parallele:", parallele([100,220,470]), "Ohms")

