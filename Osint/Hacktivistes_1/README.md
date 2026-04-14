# CTF – Spectre 7  
## Documentation interne du challenge

---

## Informations générales

| Champ              | Valeur à remplir |
|--------------------|------------------|
| **Nom du challenge** | Hacktivistes    |
| **Auteur**           | lenzzair       |
| **Difficulté**       | Welcome        |
| **Code challenge**   | Osint1_E1      |

---

## Description du challenge
Un faux article de presse indiquant qu’un groupe d’hacktivistes a signé une revendication après une cyberattaque ayant causé des perturbations notables sur les services municipaux d’Annecy. Le joueur doit suivre le pivot OSINT (le hashtag #AwakeTheTruth) pour retrouver le compte X/Twitter qui a relayé la revendication et en déduire le nom du groupe : ShadowHunter.

---

## Techniques utilisées
Décrire uniquement les mécaniques réelles exploitées par le joueur :  
- Recherche OSINT sur les réseaux sociaux  
- Inspection d’un contenu statique fourni (PDF / image)
- Fichiers importants : article_annecy.pdf (faux article) 


---

## Création du challenge
Décrire brièvement :  
- Rédaction d’un faux article « Journal Des Alpes — Édition Haute-Savoie » mentionnant une cyberattaque importante à Annecy.
- insertion du hashtag pivot #AwakeTheTruth

---

## Problèmes rencontrés
Lister les éventuels soucis durant la création :  
- Aucun

---

## Structure du projet
Donner une vue rapide :
```

./
├── Journal-Des-Alpes.pdf
└── README.md
```


---

## Déploiement interne
Instructions utiles uniquement à l’équipe :  
- Création d'un compte X au nom de @ShadowHunter_S7

---

## Flag
Format du flag : `S7{compte_twitter}`
Flag : `S7{ShadowHunter_S7}`

---

## Writeup interne (réservé à l’orga)
Explication claire de la résolution :  
- Lecture du journal
- Identifier le tag #
- Touver le compte twitter qui aura utilisé ce tag

---
