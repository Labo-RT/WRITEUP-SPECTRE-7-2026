FROM ubuntu:26.04

# ---------------------------
# Installation des packets necessaires
# ---------------------------
RUN apt-get update && apt-get install -y \
    sudo \
    openssh-server \
    bash \
    coreutils \
    vim \
    less \
    nano \
    && rm -rf /var/lib/apt/lists/*

ENV HOSTNAME=scanning_server
# ---------------------------
#  Création des users
# ---------------------------

RUN useradd -m -s /bin/bash lambda \
    && echo "lambda:lambda" | chpasswd \
    && usermod -aG lambda lambda

RUN useradd -m -s /bin/bash nightfalcon \
    && echo "nightfalcon:o56#8K#i9#%SDw" | chpasswd \
    && usermod -aG sudo nightfalcon

# ---------------------------
#  Création des fichier et des variable pour flag
# ---------------------------

COPY find_exploit.sh /home/lambda/.find_exploit.sh
RUN chown lambda /home/lambda/.find_exploit.sh
    
RUN mkdir -p /SECRET_PROJECT/shadow_user/
RUN echo "creds: nightfalcon:o56#8K#i9#%SDw" > /SECRET_PROJECT/shadow_user/secret.txt
RUN chmod 777 /SECRET_PROJECT/shadow_user/secret.txt

# ficheir pour le bruit
RUN touch /var/tmp/.cache_sync
RUN chmod 777 /var/tmp/.cache_sync

RUN touch /usr/lib/.libpthread.so.0.bak
RUN chmod 777 /usr/lib/.libpthread.so.0.bak

RUN touch /etc/.resolv.conf.save
RUN chmod 777 /etc/.resolv.conf.save

RUN touch /var/log/.syslog.swap
RUN chmod 777 /var/log/.syslog.swap

RUN echo 'export secret="S7{3nv_l34k_sp3ctr37}"' >> /home/nightfalcon/.profile \
    && chown nightfalcon:nightfalcon /home/nightfalcon/.profile

# ---------------------------
# Indice de scénario pour le prochain chall
# ---------------------------
RUN echo 'export ssh_key_i2_server="/home/nightfalcon/.ssh/id_i2_server"' >> /home/nightfalcon/.profile \
    && chown nightfalcon:nightfalcon /home/nightfalcon/.profile

COPY ssh/ /home/nightfalcon/.ssh

# ---------------------------
#  Acivation du ssh
# ---------------------------
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config \
    && sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]

