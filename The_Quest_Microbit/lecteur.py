# ================================================================
#  MICRO:BIT B — LECTEUR DE BADGE
#  Tourne sur le micro:bit lecteur (visible sur la table).
#
#  Deux niveaux d'accès :
#    AUTH:USER  → challenge-response → OK  (porte ouverte)
#    AUTH:ADMIN → challenge-response → FLAG chiffré XOR
# ================================================================

from microbit import *
import radio
import random

# ================================================================
#  CONFIGURATION
# ================================================================
radio.config(channel=7, power=7)
radio.on()

FLAG         = "S7{R4D10_PR0T0C0L}"
MOT_DE_PASSE = "SHADOW"

# Deux niveaux d'accès :
#   USER  → porte ouverte, simple OK renvoyé
#   ADMIN → porte ouverte + flag chiffré renvoyé
UTILISATEURS = ["USER", "ADMIN"]


# ================================================================
#  FONCTION : Calcul de la réponse attendue (XOR)
#  ASCII(lettre) XOR challenge → encodé en hex sur 2 caractères
# ================================================================
def chiffrer_xor(mot_de_passe, nombre_challenge):
    resultat = ""

    for lettre in mot_de_passe:
        valeur_lettre = ord(lettre)
        valeur_xor    = valeur_lettre ^ nombre_challenge
        resultat     += "{:02x}".format(valeur_xor)

    return resultat


# ================================================================
#  FONCTION : Chiffrement du flag
#  FLAG[i] XOR MOT_DE_PASSE[i % len] → encodé en hex
# ================================================================
def chiffrer_flag(flag, mot_de_passe):
    resultat = ""

    for i in range(len(flag)):
        valeur_flag = ord(flag[i])
        valeur_cle  = ord(mot_de_passe[i % len(mot_de_passe)])
        valeur_xor  = valeur_flag ^ valeur_cle
        resultat   += "{:02x}".format(valeur_xor)

    return resultat


# ================================================================
#  BOUCLE PRINCIPALE
# ================================================================
display.show(Image.SQUARE)

challenge_en_cours   = None
utilisateur_en_cours = None

while True:

    message = radio.receive()

    if message is not None:

        # --------------------------------------------------
        # PHASE 1 : Réception du AUTH
        # --------------------------------------------------
        if message.startswith("AUTH:"):
            utilisateur = message.split(":")[1]

            if utilisateur in UTILISATEURS:
                # Utilisateur connu → génération du challenge
                utilisateur_en_cours = utilisateur
                challenge_en_cours   = random.randint(0, 255)

                radio.send("CHALLENGE:" + str(challenge_en_cours))
                display.show(Image.CLOCK12)

            else:
                # Utilisateur inconnu → refus immédiat
                radio.send("DENIED")
                display.show(Image.NO)
                sleep(2000)
                display.show(Image.SQUARE)

        # --------------------------------------------------
        # PHASE 3 : Réception du RESP
        # --------------------------------------------------
        elif message.startswith("RESP:") and challenge_en_cours is not None:
            reponse_recue    = message.split(":")[1]
            reponse_attendue = chiffrer_xor(MOT_DE_PASSE, challenge_en_cours)

            if reponse_recue == reponse_attendue:

                if utilisateur_en_cours == "USER":
                    # Accès USER → simple OK, porte ouverte
                    radio.send("OK")

                elif utilisateur_en_cours == "ADMIN":
                    # Accès ADMIN → flag chiffré renvoyé
                    flag_chiffre = chiffrer_flag(FLAG, MOT_DE_PASSE)
                    radio.send("FLAG:" + flag_chiffre)

                display.show(Image.YES)
                sleep(3000)

            else:
                # Mauvaise réponse → refus
                radio.send("DENIED")
                display.show(Image.NO)
                sleep(2000)

            # Reset pour la prochaine session
            challenge_en_cours   = None
            utilisateur_en_cours = None
            display.show(Image.SQUARE)

    sleep(50)