# AlgoInvest-Trade

Lors de ce projet je devais développer un algorithme permettant de trouver les actions
dans lesquelles investir pour dégager un maximum de profit avec un budget limité.  

Le programme calcule les potentiels profits à partir de fichiers csv.


## Installation et lancement de l'application

### Installation

Étape à effectuer une seule fois :

```bash
$ git clone https://github.com/tristan-mn/OPC_DA_P7.git
$ cd OPC_DA_P7
```

### Lancement

Pour lancer le fichier bruteforce.py :

```bash
$ python3 bruteforce.py
```

Pour lancer le fichier optimized.py :

```bash
$ python3 optimized.py
```

## Usage

Le fichier bruteforce.py traite un .csv contenant 20 actions et nous retourne une liste d'actions ne    
dépassant pas un coût de 500€ pour un maximum de rentabilité.

Le fichier optimized.py traite aussi le .csv contenant 20 actions en un temps réduit,   
mais est aussi capable de traiter 2 autres .csv contenant 1000 actions.  
Le résultat sera également une liste d'actions ne dépassant pas un coût de 500€ pour 
un maximum de rentabilité.