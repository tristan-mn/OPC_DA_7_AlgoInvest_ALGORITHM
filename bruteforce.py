import csv
from itertools import combinations
import time

lien_csv = 'actions.csv'

ligne_action = 0
BUDGET = 500

def calculer_actions():
    """
    notre fichier csv est lu 
    on calcule le profit potentiel par action
    on retourne ça dans un tableau

    Returns:
        array: toutes les actions sont conservées dans un tableau
    """
    actions = []
    with open (lien_csv) as f:
        fichier_csv = csv.DictReader(f)
        for row in fichier_csv:
            action = (row['name'], int(row['price']), (int(row['profit']) * 0.01) * int(row['price']))
            actions.append(action)
    return actions


def calculer_toutes_combinaisons(actions):
    """
    on calcule toutes les combinaisons possibles

    Args:
        actions (array): toutes les actions

    Returns:
        array: retourne un tableau avec toutes les combinaisons possibles
    """
    total_combinations = []
    for i in range(len(actions)):
        combi = combinations(actions, i)
        for comb in combi:
            total_combinations.append(comb)
    return total_combinations


def selectionner_combinaisons_valides(total_combinaisons, budget):
    """
    on garde toutes les combinaisons qui ne dépassent pas notre budget

    Args:
        total_combinaisons (array): le tableau stockant toutes les combinaisons possibles
        budget (int): notre budget est une constante de 500 euros

    Returns:
        array: on retourne un tableau avec toutes les combinaisons avec un budget
               inférieur au notre
    """
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
    """
    on calcule la combinaison la plus rentable

    Args:
        valides_combinaisons (array): toutes les combinaisons avec un prix inférieur au budget

    """
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
          f"\n{[ action[0] for action in optimale_solution ]}")
    print(f"\nLe profit maximum est de {round(max_benefice,2)}€ \nPour un investissement est de {max_prix}€\n")

debut = time.time()
combinaisons = calculer_toutes_combinaisons(calculer_actions())
selectionner_meilleure_combinaison(selectionner_combinaisons_valides(combinaisons, BUDGET))
fin = time.time()
print(f"temps d'éxécution : {fin - debut} seconds")
