# CTF – Spectre 7  

---

## Informations générales

| Champ              | Valeur à remplir |
|--------------------|------------------|
| **Nom du challenge** | exfiltration dns    |
| **Auteur**           | lenzzair       |
| **Difficulté**       | easy             |
| **Code challenge**   |                 |

---

## Description du challenge
exfiltration dns  

---

## 🛠️ Techniques utilisées

Lecture wireshark deduction et convertion hex


---

## 🧪 Création du challenge

script python scapy



---

## Problèmes rencontrés

aucun

---


## Flag
Format du flag : `S7{...}`
Flag : S7{dns_c4n_b3_dang3rous}


---

## Writeup interne (réservé à l’orga)
Explication claire de la résolution :

- On pouvait remarqué que le sous domaine était composé de caractère en HEX qui pointait vers un domaine de l'organisation.
- Il fallait concaténer les valeur en HEX et la convertir en text pour avoir la data exfiltré
---
