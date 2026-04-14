# CTF – Spectre 7  

## Documentation interne du challenge

---

## Informations générales

| Champ              | Valeur à remplir |
|--------------------|------------------|
| **Nom du challenge** | Transfert chiffrer|
| **Auteur**           | Sirconnan         |
| **Difficulté**       | hard                 |
| **Code challenge**   | network1_E2       |

---

## Description du challenge

Ce challenge a pour but de faire découvrir l'utilisation des clef PSK dans un fichier de log web pour déchiffrer des flux https et l'exportation d'un fichier par le protocole SMB depuis une trame wireshark

---

## Techniques utilisées

Mécaniques exploitées :

- Vuln: export des logs web et export de fichier d'une trame smb
- HTTPS/SMB
- Wireshark

---

## Création du challenge

Les outils utilisés :

- Un serveur web
- Un serveur SMB
- Un client Windows
- Wireshark

---

## Problèmes rencontrés

Aucun

---

## Structure du projet

Donner une vue rapide :

```
./
├── smb_partage.pcapng
├── web_connextion.pcapng
└── README.md
```

---

## Déploiement interne

Ajouter les fichiers sur CTFd

---

## Flag

Format du flag : `S7{...}`

Flag : S7{c0nn3x!0n_d€ch!ffr€€}

Emplacement / méthode de génération :

Dans le fichier web_connextion.pcapng

---

## Writeup interne

Explication claire de la résolution :

- Dans le fichier smb_partage.pcapn il faut exporter le fichier de log dans File > Export > SMB
- Après avoir enregistré le fichier de log où sont stockées les clef PSK, dans le fichier web_connextion.pcapng, il faut modifier le fichier de logs dans les paramètres TLS.
- Dans Edit > Préférences > Protocoles > TLS > (PRE)-Master-Secret log filename et il faut mettre le chemin du fichier récupéré auparavant.
- Dans les trames http, le flag est en clair
- Attention il ne faut pas faire suivre le flux car il ne montre pas les €

---
