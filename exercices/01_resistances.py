"""Calcul de la résistance équivalente (en série en parallèle) d'un circuit électrique"""

def check_resistances(resistances):
    #ValueError si la liste est vide ou contient une valeur négative
    if not resistances:
        raise ValueError("You didn't provide any resistance.")
    if any(r < 0 for r in resistances):
        raise ValueError("Your resistances cannot be negative.")

def serie (resistances):
    #calcul de la résistance équivalente en série
    check_resistances(resistances)
    r_eq = sum(resistances)
    return r_eq

def parallel(resistances):
    #calcul de la résistance équivalente en parallèle
    check_resistances(resistances)
    if 0 in resistances:
        return 0.0
    r_eq=1/sum(1/r for r in resistances)
    return r_eq

if __name__ == "__main__":
    r_circuit = [100, 220, 470]
    print(f"Resistances in series: {serie(r_circuit):.2f} \u03A9")
    print(f"Resistances in parallel: {parallel(r_circuit):.2f} \u03A9")
    print(f"Resistances in parallel with short circuit: {parallel([100,220,0]):.2f} \u03A9 \n")
#    print(f"Resistances in parallel with no resistances: {parallel([]):.2f} \u03A9")

    for bad_input in ([], [-100, 220, 470]):
        try:
            parallel(bad_input)
        except ValueError as e:
            print(f"Invalid input for parallel:{bad_input}, {e}")
        try:
            serie(bad_input)
        except ValueError as e:
            print(f"Invalid input for series:{bad_input}, {e}")
