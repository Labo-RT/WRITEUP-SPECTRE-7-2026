# 🎯 CTF – Spectre 7  
## Documentation interne du challenge

---

## 📋 Informations générales

| Champ              | Valeur à remplir |
|--------------------|------------------|
| **Nom du challenge** | Socket Intro     |
| **Auteur**           | Flavien          |
| **Difficulté**       | Welcome          |
| **Code challenge**   | Prog1_E0         |

---

## 📝 Description du challenge

Spectre 7 possède un service TCP qui serait utilisé pour obtenir diverses informations. La personne devra donc se connecter avec un script afin de communiquer avec la socket et obtenir le flag.

---

## 🛠️ Techniques utilisées
Décrire uniquement les mécaniques réelles exploitées par le joueur :
- Scripting
- Utilisation de sockets
- Connexion avec une machine distante


---

## 🧪 Création du challenge
Décrire brièvement :
- Création d'un script `server.py` qui sera exécuté sur une machine distante et invisible aux yeux des joueurs
- Création d'un script client d'exemple très simpliste afin de pouvoir tester le challenge

---

## ⚠️ Problèmes rencontrés
Lister les éventuels soucis durant la création :
- Aucun

---

## 🗂️ Structure du projet
Donner une vue rapide :
```
./
├── server.py
├── client_exemple.py
└── README.md
```


---

## 🧩 Déploiement interne
Instructions utiles uniquement à l’équipe :
- Aucune lib à installer
- Lancer server.py sur la machine distante (`python3 server.py`)
- Attention à bien ouvrir le port nécessaire sur la machine

---

## 🏁 Flag
Format du flag : `S7{...}`
Flag : `S7{App_Ech0_S3rv}`
Emplacement / méthode de génération : Dans le script `server.py`, à récupérer depuis la connexion TCP

---

## ✍️ Writeup interne (réservé à l’orga)
Explication claire de la résolution :
- Création d'un script (Python dans mon example)
- Importer la librairie socket
- Instancer une socket
- Se connecter avec la socket sur l'IP et le port
- Recevoir la réponse du serveur et la print pour lire le flag

---
