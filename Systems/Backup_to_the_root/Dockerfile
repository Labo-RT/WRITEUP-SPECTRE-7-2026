FROM ubuntu:26.04

# ---------------------------
# Installation des packets necessaires
# ---------------------------

RUN apt-get update && apt-get install -y \
    sudo \
    openssh-server \
    cron \
    bash \
    coreutils \
    zip \
    unzip \
    vim \
    && rm -rf /var/lib/apt/lists/*


# ---------------------------
# Création des users
# ---------------------------

RUN useradd -m -s /bin/bash lambda \
    && echo "lambda:lambda" | chpasswd

RUN useradd -m -s /bin/bash nyx \
    && mkdir -p /home/nyx/.ssh/old-root-keys \
    && chown -R nyx:nyx /home/nyx


# ---------------------------
# Création de la backup
# ---------------------------

RUN usermod -aG backup lambda

COPY scripts/backup.sh /usr/local/bin/backup.sh
RUN chown root:root /usr/local/bin/backup.sh \
    && chmod 754 /usr/local/bin/backup.sh

COPY config/backup.env /etc/backup.env
RUN chown root:backup /etc/backup.env \
    && chmod 664 /etc/backup.env

RUN mkdir -p /var/backups/nightly \
    && chown root:root /var/backups/nightly \
    && chmod 755 /var/backups/nightly

COPY cron/cron-backup /etc/cron.d/backup-nightly
RUN chmod 644 /etc/cron.d/backup-nightly

# ---------------------------
# Generation des clé ssh de nyx pour root
# ---------------------------
RUN ssh-keygen -t rsa -b 4096 -f /home/nyx/.ssh/old-root-keys/id_ssh_for_root -N "" \
  && chown -R nyx:nyx /home/nyx/.ssh/old-root-keys \
  && chmod 700 /home/nyx/.ssh/old-root-keys \
  && chmod 600 /home/nyx/.ssh/old-root-keys/id_ssh_for_root

RUN mkdir -p /root/.ssh \
    && cat /home/nyx/.ssh/old-root-keys/id_ssh_for_root.pub >> /root/.ssh/authorized_keys \
    && chmod 700 /root/.ssh \
    && chmod 600 /root/.ssh/authorized_keys

# ---------------------------
# Contenue de nyx et copy du flag
# ---------------------------

COPY file/* /home/nyx/
COPY flag.txt /root/who_is_kronos.txt
RUN chown root:root /root/who_is_kronos.txt \
  && chmod 740 /root/who_is_kronos.txt
# ---------------------------
# SSH settings
# ---------------------------
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config \
    && sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

EXPOSE 22

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]

