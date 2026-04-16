# CTF – Spectre 7  

---

## Informations générales

| Champ              | Valeur à remplir |
|--------------------|------------------|
| **Nom du challenge** | SOC Apache Logs 2 |
| **Auteur**           | Flavien        |
| **Difficulté**       | Welcome        |
| **Code challenge**   | SOC2_E1      |

---

## Description du challenge
Voici les logs Apache d'un site interne à l'IUT. Nous avons reçu des alertes comme quoi l'attaquant seraît maintenant dans le réseau de l'IUT, puis qu'il aurait compromis un utilisateur, puis aurait accedé à une page cachée du site depuis ce dernier. Retrouvez l'utilisateur compromis, la page cachée accédée, et l'heure d'accès à la page.

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
Format du flag : `S7{user_compromis:page_cachée:HH:MM:SS}`
Flag : `S7{flavien:admin_index:09:41:12}`

---

## Writeup interne (réservé à l’orga)
Explication claire de la résolution :  
- Téléchargement du fichier
- Grep / ctrl + f nightfalcon
- Trouver l'utilisateur compromis (flavien)
- Grep / ctrl + f 'admin'
- Trouver à l'aide des codes http la page accédée
- Trouver l'heure de la page avec le code http '200'

---
