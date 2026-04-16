# CTF – Spectre 7  

---

## Informations générales

| Champ              | Valeur à remplir |
|--------------------|------------------|
| **Nom du challenge** | SOC Apache Logs |
| **Auteur**           | Flavien        |
| **Difficulté**       | Welcome        |
| **Code challenge**   | SOC1_E1      |

---

## Description du challenge
Voici les logs Apache d'un site interne à l'IUT. Nous avons reçu le fait qu'une IP externe avait réussi à accéder au site ! Retrouvez l'utilisateur ainsi que son adresse IP.

---

## Techniques utilisées
Décrire uniquement les mécaniques réelles exploitées par le joueur :
- Lecture de logs
- Grep / CTRL + F


---

## Création du challenge
Décrire brièvement :
- Utilisation d'un tool en ligne [log-generator](https://github.com/WuerthPhoenix/log-generator/tree/develop)
- Mise en place d'une template de logs
- Insertion manuelle de l'utilisateur externe

---

## Problèmes rencontrés
Lister les éventuels soucis durant la création :  
- Versioning Python pour utiliser le tool (Python 3.9 max)

---

## Structure du projet
Donner une vue rapide :
```

./
├── apache.log
└── README.md
```


---

## Déploiement interne
Instructions utiles uniquement à l’équipe :  
- Télécharger le fichier de log `apache.log`

---

## Flag
Format du flag : `S7{IP:username}`
Flag : `S7{78.132.99.11:nightfalcon}`

---

## Writeup interne (réservé à l’orga)
Explication claire de la résolution :  
- Téléchargement du fichier
- `grep -v` sur les 10.102 (par exemple)
- trouver nightfalcon et son IP

---
