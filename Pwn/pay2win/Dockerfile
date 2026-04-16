FROM debian:bookworm-slim

RUN apt update && apt install -y socat

WORKDIR /app
COPY menu .
COPY flag.txt .

EXPOSE 54321

CMD socat TCP-LISTEN:54321,reuseaddr,fork EXEC:"./menu",pty,stderr

