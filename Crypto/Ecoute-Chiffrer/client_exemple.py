import socket
import base64

# ============================================================
#  CONFIGURATION
# ============================================================
HOST = '127.0.0.1'   # Remplacer par l'IP du serveur
PORT = 57778         # Remplacer par le port attribué


# ============================================================
#  ETAPE 1 : Connexion au serveur
# ============================================================
print("ETAPE 1 : Connexion au serveur...")

ma_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ma_socket.connect((HOST, PORT))

print("  -> Connecté !\n")


# ============================================================
#  ETAPE 2 : Réception du message du serveur
# ============================================================
print("ETAPE 2 : Réception du message...")

# Write your code ...

print(message)


# ============================================================
#  ETAPE 3 : Récuperation de la CLE et du CIPHER dans le message
# ============================================================
print("ETAPE 3 : Extraction de la CLE et du CIPHER...")

cle_base64    = ""
cipher_base64 = ""

for ligne in message.split('\n'):
    if ligne.startswith("CLE    :"):
        cle_base64 = ligne.split(":", 1)[1].strip()
    if ligne.startswith("CIPHER :"):
        cipher_base64 = ligne.split(":", 1)[1].strip()

print(f"  -> CLE    : {cle_base64}")
print(f"  -> CIPHER : {cipher_base64}\n")


# ============================================================
#  ETAPE 4 : Decodage Base64
#  Base64 est un encodage, pas un chiffrement.
#  Il convertit des bytes en texte lisible pour le transport.
#  On doit le décoder pour retrouver les vrais bytes.
# ============================================================
print("ETAPE 4 : Decodage Base64...")

# Write your code

print(f"  -> CLE en bytes    : {cle_bytes}")
print(f"  -> CIPHER en bytes : {cipher_bytes}\n")


# ============================================================
#  ETAPE 5 : Déchiffrement XOR
#  Le XOR compare bit a bit deux valeurs.
#  Si les bits sont différents -> 1, sinon -> 0.
#  C'est réversible : faire XOR une 2ème fois redonne l'original.
#  On applique XOR entre chaque octet du cipher et de la clé.
#  Si la clé est plus courte, on la recommence depuis le début.
# ============================================================
print("ETAPE 5 : Déchiffrement XOR...")

# write your code ...

print(f"  -> Code déchiffré : {code}\n")


# ============================================================
#  ETAPE 6 : Envoi du code au serveur
# ============================================================
print("ETAPE 6 : Envoi du code au serveur...")

# write your code ...

print("  -> Code envoyé !\n")


# ============================================================
#  ETAPE 7 : Lecture de la réponse du serveur
# ============================================================
print("ETAPE 7 : Réponse du serveur...")

# write your code ...

print(reponse)


# ============================================================
#  FIN
# ============================================================
ma_socket.close()