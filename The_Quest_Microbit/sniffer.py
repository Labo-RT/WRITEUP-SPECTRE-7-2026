# ================================================================
#  MICRO:BIT C — SNIFFER RADIO
#  Ce micro:bit est donné au joueur.
#  Il écoute toutes les trames radio sur le canal 7
#  et les envoie sur le port série (USB) vers le PC du joueur.
#
#  Le joueur lit ces trames depuis son PC avec script_pc.py
# ================================================================

from microbit import *
import radio

# Configuration radio (même canal que badge et lecteur)
radio.config(channel=7, power=7)
radio.on()

# Compteur de trames pour aider le joueur à suivre les échanges
compteur_trame = 0


# ================================================================
#  BOUCLE PRINCIPALE
#  Écoute en permanence et affiche chaque trame reçue
#  sur le port série → le PC du joueur les lira.
# ================================================================
display.show(Image.GHOST)

# Message de démarrage envoyé sur le port série
print("=== SNIFFER SPECTRE 7 ===")
print("Ecoute sur le canal radio 7...")
print("En attente de trames...\n")

while True:

    trame = radio.receive()

    if trame is not None:
        compteur_trame += 1

        # Envoi de la trame sur le port série (lisible depuis le PC)
        print("[TRAME " + str(compteur_trame) + "] " + trame)

        # Clignotement LED pour signaler une trame reçue
        display.show(Image.DIAMOND_SMALL)
        sleep(100)
        display.show(Image.GHOST)

    sleep(50)
