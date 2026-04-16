# CTF – Spectre 7

---

## Informations générales

| Champ            | Valeur                         |
|------------------|-------------------------------|
| Nom du challenge | Écoute chiffrée               |
| Auteur           | lenzzair                      |
| Difficulté       | Medium                        |
| Code challenge   | Prog2_EM                      |

---

## Description du challenge

> Spectre 7 protège ses communications avec un système d'authentification chiffrée.
> Un code d'accès temporaire est généré à chaque connexion, chiffré et transmis.
> Vous devez le déchiffrer et le renvoyer au serveur avant qu'il n'expire.
> Les humains sont trop lents. Scriptez.

---

## Techniques utilisées

- Scripting Python
- Sockets TCP (réutilisation de prog1)
- Encodage **Base64**
- Chiffrement **XOR**
- Challenge-response avec **timer**

---

## Principe du challenge

1. Le joueur se connecte au serveur TCP (port 57778)
2. Le serveur envoie un challenge :
   - `CLE` : la clé XOR encodée en base64
   - `CIPHER` : un code aléatoire chiffré XOR, encodé en base64
3. Le joueur a **5 secondes** pour :
   - Décoder les deux valeurs depuis base64
   - XOR déchiffrer le code
   - Renvoyer le code en clair au serveur
4. Si correct et dans les temps → le serveur envoie le flag
5. Sinon → connexion fermée (timeout ou mauvaise réponse)

> Le code change à chaque connexion : impossible de tricher avec netcat.

---


## Structure du projet

```
./
├── server.py
├── client_exemple.py
└── README.md
```

---

## Déploiement interne

- Aucune lib externe (stdlib uniquement : `socket`, `threading`, `base64`, `random`, `time`)
- Lancer le serveur : `python3 server.py`
- Port par défaut : **57778**
- Timer configurable via la constante `TIMEOUT` dans `server.py` (défaut : 5s)

---

## Flag

| Champ       | Valeur                     |
|-------------|---------------------------|
| Format      | `S7{...}`                  |
| Flag        | `S7{X0R_1s_N0t_S3cur3}`   |
| Emplacement | Envoyé par le serveur après validation du code |

---

## Writeup interne (réservé à l'orga)

```python
import socket, base64

HOST = 'IP_DU_SERVEUR'
PORT = 57778

def xor_decrypt(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(4096).decode()

    for line in data.split('\n'):
        if line.startswith("CLE    :"): key_b64    = line.split(":",1)[1].strip()
        if line.startswith("CIPHER :"): cipher_b64 = line.split(":",1)[1].strip()

    key    = base64.b64decode(key_b64)
    cipher = base64.b64decode(cipher_b64)
    code   = xor_decrypt(cipher, key).decode()

    s.send((code + '\n').encode())
    print(s.recv(1024).decode())  # S7{X0R_1s_N0t_S3cur3}
```

### Pourquoi nc ne suffit pas
Le code généré est **aléatoire à chaque connexion** et expire après 5 secondes.
Un humain avec netcat ne peut pas décoder du base64 + XOR et retaper la réponse dans ce délai.
Le joueur est **forcé d'écrire un script** qui maintient la connexion ouverte entre la réception et l'envoi.

### Points de blocage fréquents
- Ouvrir une nouvelle socket pour envoyer → le code a expiré ou n'est plus valide
- Oublier le `\n` à la fin de l'envoi → le `recv` serveur ne flush pas
- Décoder base64 mais oublier le XOR (ou l'inverse)
