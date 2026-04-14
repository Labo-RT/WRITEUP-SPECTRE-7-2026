
---

# CTF – Spectre 7

## Documentation interne du challenge

---

## Informations générales

| Champ                | Valeur                   |
| -------------------- | ------------------------ |
| **Nom du challenge** | p0st_fishing             |
| **Auteur**           | lenzzair                 |
| **Difficulté**       | Medium & Hard            |
| **Code challenge**   | forensic1_E2            |

---

## 📝 Description du challenge

Challenge de **forensic mémoire Windows**.
Un employé a exécuté un binaire malveillant suite à un clic sur un lien.
Les joueurs disposent d’un **dump mémoire Windows 10** et doivent reconstituer l’attaque : identifier l’exécutable, son comportement réseau et le moment de la compromission.

Objectifs pédagogiques :

* Identifier un OS depuis un dump mémoire
* Analyser des processus Windows
* Retrouver un reverse shell en mémoire
* Extraire des artefacts réseau et temporels

---

## Techniques utilisées

* Analyse mémoire Windows avec **Volatility 3**
* Inspection des processus (`pslist`, `pstree`)
* Analyse réseau (`netscan`)
* Reverse shell via **ncat.exe**
* Port utilisé : **1644**

---

## Création du challenge

* VM Windows 10 utilisée comme poste employé
* Exécution manuelle de `ncat.exe` depuis le profil utilisateur
* Mise en écoute sur un port TCP
* Connexion de l’attaquant simulée
* Dump mémoire réalisé après compromission
* Nettoyage volontaire de l’environnement disque

---

## Problèmes rencontrés

* Dépendance forte à l’état mémoire (timing du dump)
* Certaines commandes non visibles si la console est fermée
* Résultats variables selon les plugins Volatility
* Attention aux faux positifs réseau

---

## Structure du projet

```
./
├── memdump.zip
├── question_joueur.txt
└── README.md
```

---

## Déploiement interne

* Aucun service réseau à lancer
* Fournir uniquement le dump mémoire au joueur
* Vérifier la compatibilité Volatility 3
* OS hôte recommandé : Linux

liens de download: https://kdrive.infomaniak.com/app/share/1783311/632866d4-d9f1-470b-9ac2-94a839edb07d

---

## Flag

**Challenge en 2 Partie 
  - Partie 1 -> Medium:
    - Analyse de processus
    - Analyse de fichier
  - Partie 2 -> Hard:
    - Comprenssion d'un attaque
    - Analyse réseaux

Format : `Question`

### Partie 1

Flag 1 : Quelles est le système d'exploitation et la version du PC de l'employé ? 
  - `10`

Flag 2 : Trouvez le nom de l'executable suspect. ******.exe
  - `ncat.exe`

Flag 3 : Trouvez le numéro de processus PID associé a cette executable.
  - `3164`

Flag 4 : Quelle le chemin entier où a été installer l'executable ?
	- `\Users\b0by\AppData\ncat.exe`

### Partie 2

Flag 5 : Quelle est est le port sur lequelle écoute le .exe?
	- `1644`

Flag 6 : Donnez le timestamps (YYYY-MM-DD-HH:mm:ss) quand l'attaquant c'est connecter au PC de l'employer
  - `2026-01-22-19:51:18`

Flag 7 : Quelle commande a executer l'attaquant depuis son revese shell ?
  - `whoami`

Flag 8 : Après avoir pris le contôle du PC, l'attanquant aurait changer le mot de passe de b0by, retrouver le mot de passe qu'a utilisé l'attaquant.
  - `princess`

Méthode : déduction finale après validation des 8 questions

---

## ✍️ Writeup interne (réservé à l’orga)

Cheminement attendu :

1. Identification de l’OS via 
```bash
$ volatility3 -f memdump.raw windows.info

# NtMajorVersion  10
```
2. Liste des processus → détection du processus malveillant
```bash
$ volatility3 -f memdump.raw windows.pslist.PsList

# 3164    1448    ncat.exe        0x9182ca0ee080  2       -       1       True    2026-01-22 19:50:18.000000 UTC  N/A
`ncat.exe`
```

3. Récupération du PID associé

`3164`

4. Extraction du chemin via de l'exe
```bash
$ volatility3 -f memdump.raw windows.filescan.FileScan > scan_files.txt

$ grep ncat.exe scan_files.txt

# 0x9182c8d88180  \Users\b0by\AppData\nmap\ncat.exe
```

5. Analyse réseau, port d'écoute de ncat 
```bash
$ volatility3 -f memdump.raw windows.netscan.NetScan > network.txt

$ grep ncat.exe network.txt

# 0x9182c722bb40  TCPv4   192.168.1.18    1644    192.168.1.251   49412   ESTABLISHED     3164    ncat.exe        2026-01-22 19:51:18.000000 UTC

`1644`
```

6. Timestamp de connexion au reverseshell

Même ligne : `2026-01-22-19:51:18`

7. Commande executé sur le reverseshell 
```bash
$ volatility3 -f memdump.raw windows.consoles.Consoles

# whoami
```

8. Le mot de passe de b0by

```bash
$ volatility3 -f memdump.raw windows.hashdump.Hashdump
# b0by    1000    aad3b435b51404eeaad3b435b51404ee        fb4bf3ddf37cf6494a9905541290cf51

$ echo 'fb4bf3ddf37cf6494a9905541290cf51' > hash.txt

$ hashcat -m 1000 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
# fb4bf3ddf37cf6494a9905541290cf51:princess
```

---
