import socket
import threading
import base64
import random
import string
import time

# ================================================================
#  CONFIGURATION
# ================================================================
FLAG    = "S7{X0R_1s_N0t_S3cur3}"
CLE_XOR = b"spectre"       # Clé utilisée pour chiffrer le code
TIMEOUT = 5                # Secondes accordées au joueur pour répondre
HOST    = '0.0.0.0'
PORT    = 57778


# ================================================================
#  FONCTIONS UTILITAIRES
# ================================================================

def generer_code(longueur=12):
    """
    Génère un code aléatoire de lettres et chiffres.
    Ce code sera différent à chaque connexion.
    Exemple : "aB3kR7mXpQ2z"
    """
    caracteres_possibles = string.ascii_letters + string.digits
    code = ""
    for _ in range(longueur):
        code += random.choice(caracteres_possibles)
    return code


def chiffrer_xor(texte_bytes, cle_bytes):
    """
    Chiffre des données avec l'algorithme XOR.

    Le XOR (ou exclusif) compare chaque bit : si les deux bits sont différents
    le résultat est 1, sinon 0. C'est réversible : XOR deux fois = texte original.

    On répète la clé si elle est plus courte que le texte.
    Exemple avec clé "AB" et texte "HELLO" :
        H ^ A, E ^ B, L ^ A, L ^ B, O ^ A
    """
    resultat = []

    for i in range(len(texte_bytes)):
        # On prend le caractère du texte
        octet_texte = texte_bytes[i]

        # On prend le caractère de la clé (on recommence au début si nécessaire)
        position_dans_cle = i % len(cle_bytes)
        octet_cle = cle_bytes[position_dans_cle]

        # On applique le XOR entre les deux
        octet_chiffre = octet_texte ^ octet_cle

        resultat.append(octet_chiffre)

    return bytes(resultat)


def construire_message_challenge(code):
    """
    Prépare le message envoyé au joueur :
      - Chiffre le code avec XOR
      - Encode la clé et le code chiffré en Base64 (pour pouvoir les envoyer en texte)
      - Formate le tout dans un message lisible
    """
    # Chiffrement XOR du code
    code_en_bytes   = code.encode('utf-8')
    code_chiffre    = chiffrer_xor(code_en_bytes, CLE_XOR)

    # Encodage en Base64 pour pouvoir transmettre en texte
    cle_en_base64          = base64.b64encode(CLE_XOR).decode('utf-8')
    code_chiffre_en_base64 = base64.b64encode(code_chiffre).decode('utf-8')

    message = (
        "=== Spectre 7 – Authentification chiffrée ===\n"
        "Un code d’accès temporaire a été généré.\n"
        "Déchiffrez-le et renvoyez-le en clair AVANT expiration.\n\n"
        f"CLE    : {cle_en_base64}\n"
        f"CIPHER : {code_chiffre_en_base64}\n\n"
        f"Vous avez {TIMEOUT} secondes. Bonne chance.\n"
    )
    return message


# ================================================================
#  GESTION DES CONNEXIONS
# ================================================================

class Serveur:
    def __init__(self):
        self.socket_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def gerer_client(self, connexion, adresse):
        """Gère un client connecté : envoie le challenge et vérifie la réponse."""
        try:
            print(f"\n[+] Connexion de {adresse}")

            # Génération d'un code secret unique pour cette connexion
            code_secret = generer_code()
            print(f"[DEBUG] Code généré : {code_secret}")

            # Envoi du challenge au joueur
            message = construire_message_challenge(code_secret)
            connexion.send(message.encode('utf-8'))

            # On donne TIMEOUT secondes au joueur pour répondre
            connexion.settimeout(TIMEOUT)
            debut = time.time()

            try:
                # Réception de la réponse du joueur
                reponse = connexion.recv(1024).decode('utf-8').strip()
                temps_ecoule = time.time() - debut

                if reponse == code_secret:
                    # Bonne réponse dans les temps !
                    print(f"[OK] {adresse} a reussi en {temps_ecoule:.2f}s")
                    connexion.send(f"\nAccès autorisé ! Voici le flag : {FLAG}\n".encode('utf-8'))
                else:
                    # Mauvaise réponse
                    print(f"[FAIL] {adresse} a envoye : '{reponse}' (attendu : '{code_secret}')")
                    connexion.send(f"\nCode incorrect. Connexion fermée.\n".encode('utf-8'))

            except socket.timeout:
                # Le joueur n'a pas répondu à temps
                print(f"[TIMEOUT] {adresse} n'a pas répondu dans les {TIMEOUT}s")
                connexion.send(f"\nTemps écoulé. Connexion fermée.\n".encode('utf-8'))

        except Exception as e:
            print(f"[ERREUR] Problème avec {adresse} : {e}")
        finally:
            connexion.close()

    def demarrer(self):
        """Lance le serveur et attend les connexions en boucle."""
        try:
            self.socket_serveur.bind((HOST, PORT))
            self.socket_serveur.listen(5)
            print(f"\nServeur en écoute sur {HOST}:{PORT}...")
            print(f"Timeout configuré : {TIMEOUT} secondes\n")

            while True:
                try:
                    connexion, adresse = self.socket_serveur.accept()
                    # Chaque client est géré dans un thread séparé
                    thread = threading.Thread(target=self.gerer_client, args=(connexion, adresse))
                    thread.daemon = True
                    thread.start()
                except KeyboardInterrupt:
                    print("\n[ARRET] Serveur arrêté par l'utilisateur.")
                    break
        except Exception as e:
            print(f"[ERREUR] Impossible de démarrer le serveur : {e}")
        finally:
            self.socket_serveur.close()


# ================================================================
#  POINT D'ENTREE
# ================================================================

if __name__ == "__main__":
    serveur = Serveur()
    serveur.demarrer()