import csv
from itertools import combinations

lien_csv = 'actions.csv'

ligne_action = 0
budget = 500

def calculer_actions():
    actions = []
    with open (lien_csv) as f:
        fichier_csv = csv.DictReader(f)
        for row in fichier_csv:
            action = (row['nom'], int(row['prix']), (int(row['benefice']) * 0.01) * int(row['prix']))
            actions.append(action)
    return actions


def calculer_toutes_combinaisons(actions):
    total_combinations = []
    for i in range(len(actions)):
        combi = combinations(actions, i)
        for comb in combi:
            total_combinations.append(comb)
    print(len(total_combinations))
    return total_combinations


def selectionner_combinaisons_valides(total_combinaisons, budget):
    combinaisons_valides = []
    for combinaison in total_combinaisons:
        combinaison_prix = 0
        combinaison_benefice = 0
        for i in range(len(combinaison)):
            combinaison_prix += combinaison[i][1]
            combinaison_benefice += combinaison[i][2]
        if combinaison_prix <= budget:
            combinaisons_valides.append([combinaison, combinaison_prix, combinaison_benefice])
    return combinaisons_valides


def selectionner_meilleure_combinaison(valides_combinaisons):
    optimale_solution = None
    max_prix = 0
    max_benefice = 0
    for combinaison in valides_combinaisons:
        if combinaison[2] > max_benefice:
            max_benefice = combinaison[2]
            max_prix = combinaison[1]
            optimale_solution = combinaison[0]
    print()
    print(f"#"*10 + "    Résultats:   " + "#"*10)
    print(f"La combinaison la plus rentable est :\n"
          f"\n{optimale_solution}")
    print(f"\nLe profit maximum est de {round(max_benefice,2)}€ \nPour un investissement est de {max_prix}€\n")

combinaisons = calculer_toutes_combinaisons(calculer_actions())
selectionner_meilleure_combinaison(selectionner_combinaisons_valides(combinaisons, budget))