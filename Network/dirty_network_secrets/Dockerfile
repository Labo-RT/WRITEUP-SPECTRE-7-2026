FROM ubuntu/bind9:latest

RUN mkdir -p /etc/bind/zones

COPY named.conf /etc/bind/named.conf
COPY db.ghostshark.local /etc/bind/zones/db.ghostshark.local
COPY db.10.102.74 /etc/bind/zones/db.10.102.74
EXPOSE 53/udp 53/tcp
