# ================================================================
#  SCRIPT PC — LECTURE DU SNIFFER
#  Ce script est donné au joueur.
#  Il lit les trames captées par le micro:bit sniffer (C)
#  et les affiche proprement dans le terminal.
#
#  INSTALLATION : pip install pyserial
#  USAGE        : python3 script_pc.py
# ================================================================

import serial
import serial.tools.list_ports


# ================================================================
#  ETAPE 1 : Détection automatique du micro:bit
#  On cherche le port série du micro:bit parmi les ports USB.
# ================================================================
print("=== SNIFFER SPECTRE 7 ===\n")
print("ETAPE 1 : Recherche du micro:bit sniffer...\n")

port_microbit = None
ports_disponibles = serial.tools.list_ports.comports()

for port in ports_disponibles:
    print("  Port detecte : " + port.device + " — " + port.description)

    # Le micro:bit apparaît généralement avec "mbed" ou "USB Serial" dans sa description
    if "mbed" in port.description.lower() or "microbit" in port.description.lower():
        port_microbit = port.device
        print("  --> Micro:bit trouve sur : " + port_microbit)

# Si pas trouvé automatiquement, le joueur doit renseigner manuellement
if port_microbit is None:
    print("\n  Micro:bit non detecte automatiquement.")
    print("  Ports disponibles :")
    for port in ports_disponibles:
        print("    " + port.device)
    print("\n  Renseigne manuellement le port ci-dessous.")
    print("  Exemple Linux : /dev/ttyACM0")
    print("  Exemple Mac   : /dev/cu.usbmodem...")
    print("  Exemple Win   : COM3\n")
    port_microbit = input("  Ton port : ").strip()


# ================================================================
#  ETAPE 2 : Connexion au micro:bit via port série
# ================================================================
print("\nETAPE 2 : Connexion sur " + port_microbit + " à 115200 baud...")

try:
    connexion_serie = serial.Serial(port_microbit, 115200, timeout=1)
    print("  --> Connecte !\n")
except Exception as erreur:
    print("  --> ERREUR : impossible de se connecter.")
    print("  Détail : " + str(erreur))
    print("\n  Conseil : lance 'sudo usermod -aG dialout $USER' puis reconnecte-toi.")
    exit()


# ================================================================
#  ETAPE 3 : Lecture des trames en temps réel
#  Le script affiche chaque trame reçue du sniffer.
#  Ctrl+C pour arrêter.
# ================================================================
print("ETAPE 3 : Ecoute des trames radio...\n")
print("-" * 45)

try:
    while True:
        # Lecture d'une ligne depuis le port série
        ligne_brute = connexion_serie.readline()

        # Décodage en texte lisible
        ligne = ligne_brute.decode('utf-8', errors='ignore').strip()

        # Affichage uniquement si la ligne n'est pas vide
        if ligne:
            print(ligne)

except KeyboardInterrupt:
    print("\n" + "-" * 45)
    print("Ecoute arretee.")
    connexion_serie.close()
