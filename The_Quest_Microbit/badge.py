# ================================================================
#  MICRO:BIT — BADGE
#  Étape 3 du challenge
#
#  Ce script est à flasher sur votre micro:bit.
#  Il rejoue le protocole d'authentification en radio.
#
#  Bouton A → authentification USER  (teste que le protocole fonctionne)
#  Bouton B → authentification ADMIN (récupère le flag chiffré)
#
#  RAPPEL DU PROTOCOLE :
#    AUTH:USER ou AUTH:ADMIN  →  lecteur
#    CHALLENGE:xx             ←  lecteur
#    RESP:xxxxxxxx            →  lecteur
#    OK       (si USER)       ←  lecteur
#    FLAG:xxx (si ADMIN)      ←  lecteur
# ================================================================

from microbit import *
import radio

# ================================================================
#  CONFIGURATION RADIO
# ================================================================
radio.config(channel=7, power=7)
radio.on()

# ================================================================
#  À COMPLÉTER : mot de passe trouvé à l'étape 2
# ================================================================
MOT_DE_PASSE = "SHADOW"   


# ================================================================
#  FONCTION : Chiffrement XOR
# ================================================================
def chiffrer_xor(mot_de_passe, nombre_challenge):
    resultat = ""

    for lettre in mot_de_passe:
        valeur_lettre = ord(lettre)
        valeur_xor    = valeur_lettre ^ nombre_challenge
        resultat     += "{:02x}".format(valeur_xor)

    return resultat


# ================================================================
#  FONCTION : Lancer un échange complet avec le lecteur
# ================================================================
def authentifier(nom_utilisateur):

    display.show(Image.ARROW_E)

    # --------------------------------------------------
    # PHASE 1 : Envoi du AUTH
    # --------------------------------------------------
    radio.send("AUTH:" + nom_utilisateur)
    sleep(500)

    # --------------------------------------------------
    # PHASE 2 : Attente du CHALLENGE
    # --------------------------------------------------
    display.show(Image.CLOCK12)
    nombre_challenge = None
    attente          = 0

    while nombre_challenge is None and attente < 5000:
        message = radio.receive()

        if message is not None:
            if message.startswith("CHALLENGE:"):
                nombre_challenge = int(message.split(":")[1])

        sleep(100)
        attente += 100

    if nombre_challenge is None:
        # Pas de réponse du lecteur
        display.show(Image.NO)
        sleep(2000)
        return

    # --------------------------------------------------
    # PHASE 3 : Calcul et envoi de la réponse XOR
    # --------------------------------------------------
    reponse = chiffrer_xor(MOT_DE_PASSE, nombre_challenge)
    radio.send("RESP:" + reponse)
    display.show(Image.CLOCK3)

    # --------------------------------------------------
    # PHASE 4 : Attente de la réponse du lecteur
    # --------------------------------------------------
    attente = 0

    while attente < 5000:
        message = radio.receive()

        if message is not None:

            if message == "OK":
                # Accès USER accordé
                display.show(Image.YES)
                sleep(3000)
                return

            elif message.startswith("FLAG:"):
                # Accès ADMIN → flag chiffré reçu
                flag_chiffre = message.split(":")[1]

                # Envoi sur le port série pour déchiffrement sur PC
                print("FLAG_CHIFFRE:" + flag_chiffre)

                display.show(Image.YES)
                sleep(3000)
                return

            elif message == "DENIED":
                display.show(Image.NO)
                sleep(2000)
                return

        sleep(100)
        attente += 100

    # Timeout
    display.show(Image.NO)
    sleep(2000)


# ================================================================
#  BOUCLE PRINCIPALE
#  Bouton A → USER  |  Bouton B → ADMIN
# ================================================================
display.show(Image.HAPPY)

while True:

    if button_a.was_pressed():
        # Test simple : est-ce que le protocole fonctionne ?
        authentifier("USER")
        display.show(Image.HAPPY)

    if button_b.was_pressed():
        # Récupération du flag chiffré
        authentifier("ADMIN")
        display.show(Image.HAPPY)

    sleep(50)
