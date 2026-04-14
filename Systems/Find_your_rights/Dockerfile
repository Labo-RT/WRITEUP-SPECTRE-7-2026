FROM ubuntu:26.04

# ---------------------------
# Installation des paquets nécessaires
# ---------------------------
RUN apt-get update \
    && apt-get purge -y sudo-rs || true \
    && apt-get install -y \
    sudo=1.9.* \
    openssh-server \
    vim \
    bash \
    coreutils \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------
# Création des users
# ---------------------------
RUN useradd -m -s /bin/bash nightfalcon \
    && echo "nightfalcon:nightfalcon" | chpasswd \
    && usermod -aG nightfalcon nightfalcon

RUN useradd -m -s /bin/bash orion \
    && echo "orion:S3cr3t_P4ss0rd_4s_Fuck3d" | chpasswd \
    && usermod -aG orion orion
# ----------------- ----------
# Création des fichiers et du flag
# ---------------------------

COPY --chown=nightfalcon:nightfalcon files/investigation-notes.txt /home/nightfalcon/investigation-notes.txt
RUN chmod 644 /home/nightfalcon/investigation-notes.txt

COPY --chown=nightfalcon:nightfalcon files/network-logs.txt /home/nightfalcon/network-logs.txt
RUN chmod 644 /home/nightfalcon/network-logs.txt

COPY --chown=orion:orion files/spectre-trace.txt /home/orion/spectre-trace.txt
RUN chmod 600 /home/orion/spectre-trace.txt

COPY files/spectre-welcome.sh /etc/profile.d/
RUN chmod +x /etc/profile.d/spectre-welcome.sh

# ---------------------------
# Configuration sudo
# ---------------------------

RUN echo 'nightfalcon ALL=(orion) NOPASSWD: /usr/bin/find' >> /etc/sudoers


# ---------------------------
# Activation du SSH
# ---------------------------
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config \
    && sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
