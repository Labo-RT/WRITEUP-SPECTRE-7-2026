#!/bin/bash

set -e

# chargement des variable d'environnement dans un fichier de configuration externe
source /etc/backup.env

DATE=$(date +"%Y-%m-%d_%H-%M")
ARCHIVE="infra-backup-$DATE.zip"

if [ -z "$DEST" ]; then
  exit 1
fi

# Création de la backup en cours...
zip -r "$DEST/$ARCHIVE" /home/nyx/

chown "$USER:$USER" "$DEST/$ARCHIVE"
chmod 740 "$DEST/$ARCHIVE"

