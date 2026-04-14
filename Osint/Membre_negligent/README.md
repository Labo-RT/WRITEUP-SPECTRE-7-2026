# CTF – Spectre 7  

---

## Informations générales

| Champ              | Valeur à remplir |
|--------------------|------------------|
| **Nom du challenge** | Membre Négligent|
| **Auteur**           | lenzzair       |
| **Difficulté**       | Welcome        |
| **Code challenge**   | Osint1_E1      |

---

## Description du challenge
Après avoir identifié le groupe ShadowHunter dans le challenge précédent, le joueur doit maintenant identifier un membre négligent de l’équipe. Le support consiste en le compte X/Twitter du groupe où l’un des membres utilise le même avatar et le même style d’écriture sur un autre réseau social (Mastodon). Le joueur doit faire le pivot pour retrouver la description du compte Mastodon et y découvrir le flag.

Le compte Mastodon à retrouver : NightFalcon_S7@mastodon
Indice scénaristique : ShadowHunter est un petit groupe de 3 membres seulement, et NightFalcon est l’un d’eux.

---

## Techniques utilisées
Décrire uniquement les mécaniques réelles exploitées par le joueur :  
- Recherche OSINT sur les réseaux sociaux

- Analyse des interactions d’un compte X (likes / abonnements / réponses)

- Pivot vers un second réseau social


---

## Création du challenge
Décrire brièvement :  
- Mise en place d’un profil tiers réutilisant le même avatar et la même identité visuelle

---

## Problèmes rencontrés
- Aucun

---

## Structure du projet
Donner une vue rapide :
```

./
├── Compte_Screen.png
└── README.md
```


---

## Déploiement interne
Instructions utiles uniquement à l’équipe :  
- Création d'un compte X au nom de @NightFalco51139
- Compte secondaire à créer : NightFalco51139 (plateforme tierce : Mastodon)

---

## Flag
Format du flag : `S7{...}`
Flag : `S7{ECHOES_IN_THE_DARK}`

---

## Writeup interne (réservé à l’orga)
Explication claire de la résolution :  
- Il inspecte les likes, abonnements ou réponses
- Un avatar identique apparaît sur un autre réseau social
- Le pseudo associé : NightFalcon

---
