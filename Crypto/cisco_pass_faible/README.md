# CTF – Spectre 7  

---

## Informations générales

| Champ              | Valeur à remplir |
|--------------------|------------------|
| **Nom du challenge** | Cisco Pass Faible |
| **Auteur**           | Flavien          |
| **Difficulté**       | Easy             |
| **Code challenge**   | crypto2_E1       |

---

## Description du challenge
La configuration d'un switch appartenant à Spectre 7 a été rendue publique ! A vous de retrouver le mot de passe Admin a partir du hash donné dans la configuration.

---

## Techniques utilisées
Décrire uniquement les mécaniques réelles exploitées par le joueur :

- Crack de hash
- Utilisation de hashcat
- Utilisation de wordlist

---

## Création du challenge
Décrire brièvement :

- Créé un switch vierge sur Packet Tracer
- Créé un user Admin avec un mot de passe faible
- Récupéré la conf avec la commande `show running-config`

---

## Problèmes rencontrés
Lister les éventuels soucis durant la création :

- Desfois le 'backend runtime' est long a start lors du crackage, faut juste attendre

---

## Structure du projet
Donner une vue rapide :

```
./
├── cisco.dmp
└── README.md
```

---

## Déploiement interne
Instructions utiles uniquement à l’équipe :

- téléchargement du fichier de conf Cisco
- installation de hashcat si pas déjà fait
- installation de rockyou.txt si pas déjà fait
- regarder [les différents examples de hash](hashcat.net/wiki/doku.php?id=example_hashes) pour connaître le mode à utiliser

---

## Flag
Format du flag : `S7{mot_de_passe}`
Flag : `S7{password!}`
Emplacement / méthode de génération : Création d'un user sur switch Cisco

---

## ✍️ Writeup interne (réservé à l’orga)
Explication claire de la résolution :

- Télécharger cisco.dmp
- Avoir hashcat et rockyou.txt
- Mettre le hash dans un fichier (ex: hash.txt)
- à l'aide [de la page des examples de hash](hashcat.net/wiki/doku.php?id=example_hashes), trouver le mode à utiliser (500)
- `hashcat -m 500 hash.txt rockyou.txt`

---
