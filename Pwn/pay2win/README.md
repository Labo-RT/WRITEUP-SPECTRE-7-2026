# CTF – Spectre 7  

---

## Informations générales

| Champ              | Valeur à remplir |
|--------------------|------------------|
| **Nom du challenge** | **pay2win** |
| **Auteur** | **Caesesia** |
| **Difficulté** | **medium** |
| **Code challenge** | **reverse2_E1** |

---

## Description du challenge
Ce challenge a pour but de démontrer les conséquences d'une mauvaise pratique de développement bas niveau (ici en C) et de la conversion et l'utilisation d'entiers signés et non-signés.

---

## Techniques utilisées
Décrire uniquement les mécaniques réelles exploitées par le joueur :
- vulnérabilités utilisées : conversion d'un entier signé en entier non-signé
- protocoles ou concepts concernés : conversion de type en C
- services lancés et ports utilisés : voir Dockerfile
- fichiers importants : `menu`
- dépendances : N/A
- particularités à connaître pour maintenir le challenge : maintenir le service en place côté serveur


---

## Création du challenge
Décrire brièvement :
- comment le challenge a été construit : Écriture d'un programme en C 
- les étapes techniques importantes :
    - écriture du programme en C avec ajout de faille de conversion
    - lecture du mot de passe depuis un `flag.txt` en local sur le serveur
    - set up du challenge côté serveur
    - compilation du programme avec `gcc <nom_programme>.c -o <nom_binaire>`
- choix techniques effectués :
    - setup volontaire d'un nombre négatif à input pour obtenir le flag (éventuellement changeable en une valeur trsè spécifique)
    - lecture du flag en local côté serveur

---

## Problèmes rencontrés
Lister les éventuels soucis durant la création :
- limitations techniques : mon skill en C/compilation/assembleur/reverse donc sans faire exprès j'ai ajouté une seconde faille d'integer overflow en plus de la faille volontaire
- edge cases à surveiller : peut-être un bypass de l'input négatif (comme quand Lenny a input un très grand nombre qui a pu passer)
- contraintes imposées (temps, services, compatibilité) : le programme doit impérativement être exécuté dans un environnement Linux (virtuel ou non)

---

## Structure du projet
Donner une vue rapide :
```
./
├── Dockerfile
├── flag.txt
├── menu.c
├── menu
└── README.md
```


---

## Déploiement interne
Instructions utiles uniquement à l’équipe : les informations suivantes permettent de recréer le processus de mise en place du challenge
- configuration nécessaire :
    - set up le service en écoute sur le serveur (voir Dockerfile)
- commandes Docker :
    - Build l'image depuis la Dockerfile : `docker image build -t pay2win .`
- scripts de lancement : jsp sah
- variables d’environnement : N/A
- vérification du bon fonctionnement :
    - netcat sur le port serveur et check si le programme tourne bien

---

## Flag
Format du flag : `S7{...}`
Flag : `S7{}`
Emplacement / méthode de génération : le binaire print le flag lorsqu'une quantité suffisante de tokens est obtenue pour passer admin.

---

## Writeup interne (réservé à l’orga)
Explication claire de la résolution :
- cheminement attendu : exécuter le script, check les options d'input, voir qu'il faut suffisamment de tokens admin, bypass la limite via input négatif.
- vraies failles exploitées : conversion entier signé en non-signé -> integer overflow
- commandes clés : N/A
- détails nécessaires pour vérifier le challenge : entrer un input négatif pour chopper le flag.
- pièges et comportements possibles des joueurs : générer les tokens manuellement et un par un, ou essayer d'entrer un très grand nombre, etc...

---
