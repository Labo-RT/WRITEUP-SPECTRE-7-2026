
# 🎯 CTF – Spectre 7  
## Documentation interne du challenge

---

## 📋 Informations générales

| Champ              | Valeur |
|--------------------|--------|
| **Nom du challenge** | DNS Challenge - Ghostshark |
| **Auteur**           | lenzzair|
| **Difficulté**       | Easy |
| **Code challenge**   | NET1_E1 |

---

## 📝 Description du challenge

**Thème** : Énumération DNS et Service Discovery

Le joueur doit explorer les enregistrements DNS d'un serveur Bind9 pour découvrir 4 informations progressives chaînées entre elles. 

**Objectif** : Apprendre les concepts réels de DNS :
- A Records (résolution basique)
- TXT Records (métadonnées / secrets)
- SRV Records (service discovery - Kerberos, LDAP, SSH en production)

---

## 🛠️ Techniques utilisées

**Protocoles exploités** :
- DNS
- SRV Records - Service Discovery
- TXT Records - stockage de métadonnées

**Services lancés** :
- Bind9 (ubuntu/bind9:latest)
- Port : 53 (UDP/TCP)

**Fichiers importants** :
- `db.ghostshark.local` - Zone DNS avec tous les enregistrements
- `named.conf` - Configuration Bind9
- `Dockerfile` - Image ubuntu/bind9 avec copies des configs

**Concepts clés** :
- SOA, NS, A, AAAA, MX, TXT, SRV records
- Service naming convention : `_service._protocol.domain`

**Dépendances** :
- Docker
- `dig` ou `nslookup` (côté joueur)

---

## 🧪 Création du challenge

**Étapes de construction** :

1. **Définir les réponses** : 
   - rep1 = IP ghostshark (`10.102.76.13`)
   - rep2 = TXT secret (`n3tsh4rk`)
   - rep3 = Port SSH (`2222`)
   - rep4 = TXT final (`rep4=OpenSSH_7.4`)

2. **Créer la zone DNS** (`db.ghostshark.local`) :
   - A Record pour ghostshark.local
   - TXT Records sur n3t.ghostshark.local (secret + indice)
   - SRV Record `_ssh._tcp.ghostshark.local` pointant vers sshserver
   - TXT Record final sur sshserver

3. **Configuration Bind9** (`named.conf`) :
   - Zone master pour ghostshark.local
   - Allow queries depuis n'importe où 

4. **Dockerisation** :
   - Image ubuntu/bind9 minimale
   - COPY des fichiers de zone et config
   - Expose port 53 UDP/TCP


---

## 🗂️ Structure du projet

```
dns-challenge/
├── Dockerfile                  # Image ubuntu/bind9:latest
├── named.conf                  # Configuration Bind9
├── db.ghostshark.local        # Zone DNS complète
├── CHALLENGE.md               # Énoncé pour joueurs
├── WRITEUP.md                 # Writeup admin
└── README.md                  # Cette doc (doc interne)
```

---

## 🧩 Déploiement interne

### Build & Run

```bash

docker build -t dns-challenge:latest .

# 4. Run
docker run -d --rm --name dns-server -p 53:53/udp -p 53:53/tcp dns-challenge:latest

dig @127.0.0.1 ghostshark.local
```

### Vérification de base

```bash

# Chaque étape
dig @127.0.0.1 ghostshark.local         # ÉTAPE 1
dig @127.0.0.1 n3t.ghostshark.local TXT # ÉTAPE 2
dig @127.0.0.1 _ssh._tcp.ghostshark.local SRV  # ÉTAPE 3
dig @127.0.0.1 sshserver.ghostshark.local TXT  # ÉTAPE 4
```


## ✍️ Writeup interne (réservé à l'orga)

### Cheminement attendu

**ÉTAPE 1 - A Record basique** (warm-up)
```bash
dig @127.0.0.1 ghostshark.local
# Réponse : ghostshark.local. 300 IN A 10.102.76.13
# rep1 = 10.102.76.13
```

---

**ÉTAPE 2 - TXT discovery**
```bash
dig @127.0.0.1 n3t.ghostshark.local TXT
# Réponse :
# n3t.ghostshark.local. 300 IN TXT "n3tsh4rk"
# n3t.ghostshark.local. 300 IN TXT "hint=look_for_ssh_service"
# rep2 = n3tsh4rk
```

---

**ÉTAPE 3 - SRV Record & Service Discovery**
```bash
dig @127.0.0.1 _ssh._tcp.ghostshark.local SRV
# Réponse :
# _ssh._tcp.ghostshark.local. 300 IN SRV 10 5 2222 sshserver.ghostshark.local.
# Structure SRV : priority weight PORT target
# sshserver.ghostshark.local. 300 IN A 10.102.74.42
# rep3 = 2222
```

---

**ÉTAPE 4 - Final TXT**
Avec l'addresse IP qu'on a pu récupéré du server ssh on fait une requête inverser dessus
```bash
dig @127.0.0.1 -x 10.102.74.42
# Réponse :
# 42.74.102.10.in-addr.arpa. 300 IN PTR ssh-prod-legacy-01.ghostshark.local.
# la zone inversé n'a pas été mise a jour depuis longtemps qui nous permet de découvrir l'ancien serveur
dig @127.0.0.1 ssh-prod-legacy-01.ghostshark.local TXT
# TXT "ssh-version=OpenSSH_7.4)
```

## 🏁 Flag

**Format du flag** : `S7{rep1:rep2:rep3:rep4}`

**Flag attendu** : 
```
S7{10.102.76.13:n3tsh4rk:2222:OpenSSH_7.2}
```



