# CTF – Spectre 7  

---

## Informations générales

| Champ              | Valeur à remplir |
|--------------------|------------------|
| **Nom du challenge** | Chiffrement XOR  |
| **Auteur**           | Flavien          |
| **Difficulté**       | Easy             |
| **Code challenge**   | crypto1_E1       |

---

## Description du challenge
Un des membres de Spectre 7 a développé un script permettant de chiffrer les données envoyées. Montrez qu'on peut retrouver la clé de chiffrement !

---

## Techniques utilisées
Décrire uniquement les mécaniques réelles exploitées par le joueur :

- Utilisation de Netcat
- Utilisation d'un outil externe pour retrouver le flag (ex: Cyberchef?)

---

## Création du challenge
Décrire brièvement :

- Création d'un script serveur qui gère le multithreading
- Méthode XOR simplifiée pour comprendre le code source

---

## Problèmes rencontrés
Lister les éventuels soucis durant la création :

- N/A

---

## Structure du projet
Donner une vue rapide :

```
./
├── server.py
├── code_source.py
└── README.md
```


---

## Déploiement interne
Instructions utiles uniquement à l’équipe :

- Ouvrir le port nécessaire
- `python3 server.py`
- Laisser disponible `code_source.py` aux participants

---

## Flag
Format du flag : `S7{...}`  
Flag : `S7{H4ve_fUn_w1Th_X0r}`
Emplacement / méthode de génération : Ecrit dans le code

---

## Writeup interne (réservé à l’orga)
Explication claire de la résolution :

- se connecter à l'aide de netcat `nc 127.0.0.1 47777`
- envoyer une longue chaine (par ex: 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
- copier la réponse du serveur
- aller sur Cyberchef
- sélectionner XOR, puis coller la réponse dans la clé (en hex)
- copier coller la chaine envoyé dans l'input
- tadaaaaa

---
