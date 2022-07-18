import csv
import time

BUDGET = 500


def choix_fichier():
    """
    on demande à l'utilisteur quel fichier il souhaite faire analyser

    Returns:
        str: retourne le choix de l'utilisteur
    """
    print("Quel fichier voulez vous analyser ?")
    print("Tapez 1 pour le fichier actions.csv")
    print("Tapez 2 pour le fichier dataset1_Python+P7.csv")
    print("Tapez 3 pour le fichier dataset2_Python+P7.csv")
    choix = input("Votre choix : ")
    if choix == "1" or choix == "2" or choix == "3":
        return choix
    else:
        print("Vous devez choisir un nombre entre 1 et 3.")
        return choix_fichier()


def calculer_actions(choix):
    """_summary_

    Args:
        choix (str): le choix de l'utilisateur va influencer le déroulement 
                     des instructions dans la fonction

    Returns:
        array: toutes les actions sont conservées dans un tableau
    """
    actions = []
    fichier_csv = {}

    if choix == "1":
        lien_csv = 'actions.csv'
        with open (lien_csv) as f:
            fichier_csv = csv.DictReader(f)
            for ligne in fichier_csv:
                action = (ligne['name'], int(ligne['price']), (int(ligne['profit']) * 0.01) * int(ligne['price']))
                actions.append(action)
    else:
        if choix == "2":
            fichier_csv = csv.DictReader(open('dataset1_Python+P7.csv'))
        elif choix == "3":
            fichier_csv = csv.DictReader(open('dataset2_Python+P7.csv'))
        for ligne in fichier_csv:
            # on vérifie la validité des données
            if int(float(ligne['price']) * 10) > 0 and float(ligne['profit']) > 0:
                action = (ligne['name'], int(float(ligne['price']) * 10), int(float(ligne['price']) * 10) *
                          float(ligne['profit']) / 100)
                actions.append(action)
    return actions


def sacAdos_dynamique(budget, actions):
    """_summary_

    Args:
        budget (int): budget maximal à investir
        actions (array): toutes les actions

    Returns:
        float: le profit maximum
        array: toutes les actions 
    """

    # matrice permettant de parcourir le budget de 0 à 500€ pour chaque action
    matrice = [[0 for x in range(budget + 1)] for x in range(len(actions) + 1)]

    # on parcours les actions
    for i in range(1, len(actions) + 1):
        # on parcours le budget de 0 au budget max
        for j in range(1, budget + 1):
            # si le prix est inférieur au budget (je peux encore acheter une action)
            if actions[i-1][1] <= j:
                # on met dans la matrice le score le plus élevé entre l'élément trouvé juste avant et
                # l'élément courant + la solution optimisée - le prix de l'action de la ligne d'avant
                matrice[i][j] = max(actions[i-1][2] + matrice[i-1][j-actions[i-1][1]], matrice[i-1][j])
            else:
                # si je ne peux pas acheter une autre action je garde la solution
                # optimisée de la ligne précédente
                matrice[i][j] = matrice[i-1][j]

    # Retrouver les actions en fonction du coût
    w = budget
    n = len(actions)
    actions_selection = []

    while w >= 0 and n >= 0:
        action = actions[n-1]
        if matrice[n][w] == matrice[n-1][w-action[1]] + action[2]:
            actions_selection.append(action)
            w -= action[1]
        n -= 1

    cout_total = sum([action[1] for action in actions_selection])

    print("Résultat optimisé :")
    print(f"La combinaison optimale est {[action[0] for action in actions_selection]}")
    print(f"Le profit maximum est de {round(matrice[-1][-1], 2)}€ pour un investissement de {cout_total}€")

    return matrice[-1][-1], actions_selection







def sacAdos_dynamique_dixieme(budget, actions):
    """
    Cette fonction est la même que sacAdos_dynamique
    Seulement ici nous prenons en compte des actions 
    avec plusieurs chiffres après la virgule

    Args:
        budget (int): budget maximal à investir
        actions (array): toutes les actions

    Returns:
        float: le profit maximum
        array: toutes les actions
    """
    matrice = [[0 for x in range(budget + 1)] for x in range(len(actions) + 1)]

    for i in range(1, len(actions) + 1):
        for j in range(1, budget + 1):
            if actions[i-1][1] <= j:
                matrice[i][j] = max(actions[i-1][2] + matrice[i-1][j-actions[i-1][1]], matrice[i-1][j])
            else:
                matrice[i][j] = matrice[i-1][j]

    w = budget
    n = len(actions)
    actions_selection = []

    while w >= 0 and n >= 0:
        action = actions[n-1]
        if matrice[n][w] == matrice[n-1][w-action[1]] + action[2]:
            actions_selection.append(action)
            w -= action[1]
        n -= 1
    print(actions_selection)
    print([action[1] for action in actions_selection])
    print(matrice[-1][-1])
    print()
    cout_total = sum([action[1]/10 for action in actions_selection])

    print("Résultat optimisé :")
    print(f"La combinaison optimale est {[action[0] for action in actions_selection]}")
    print(f"Le profit maximum est de {round(matrice[-1][-1], 2)}€ pour un investissement de {round(cout_total, 2)}€")

    return matrice[-1][-1], actions_selection



fichier = choix_fichier()
actions = calculer_actions(fichier)
print('Analyse en cours, veuillez patienter')
start = time.time()
if fichier == "1":
    sacAdos_dynamique(BUDGET, actions)
else:
    sacAdos_dynamique_dixieme(BUDGET * 10, actions)
end = time.time()
print(f"temps d'éxécution: {round(end - start, 3)} secondes")