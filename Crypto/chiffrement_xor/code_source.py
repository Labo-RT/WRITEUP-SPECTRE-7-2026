import socket
import threading

FLAG = b"Le flag de ce challenge de crypto est : S7{ce_flag_est_faux}" # le vrai flag est sur le serveur!

class Server:

    def __init__(self, host='0.0.0.0', port=47777):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def gestion(self, connexion, adresse):
        try:
            print(f"\nConnecté avec {adresse}")
            connexion.send("Envoyez le texte que vous voulez chiffrer : ".encode())
            data = connexion.recv(1024)
            if not data:
                return # si la personne n'a rien envoyée, skip la suite
            chiffre = self.xor(data, FLAG) # appel de la méthode xor (il faut que l'entrée et le flag soient en octets
            response = f"Voici la réponse : {chiffre.hex()}".encode() # encodage de la réponse en hex puis renvoi en octets
            connexion.send(response)

        except Exception as e:
            print(f"[ERREUR] Erreur avec {adresse}: {e}")

        finally:
            try:
                connexion.close()
            except:
                pass

    def xor(self, data: bytes, key: bytes) -> bytes:
        if len(key) == 0:
            raise ValueError("La clé ne peut pas être vide") # dans le doute
        
        result = bytearray()
        
        for i in range(len(data)):
            data_byte = data[i]          # on prend chaque octet de la réponse
            key_byte = key[i % len(key)] # on prend chaque octet la clé en boucle
            xor_byte = data_byte ^ key_byte  # opération XOR
            result.append(xor_byte)      # on ajoute au résultat
        return bytes(result)

    def ecoute(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(10)
            print(f'\nEn écoute sur {self.host}:{self.port}...\n')
            while True:
                try:
                    connexion, adresse = self.server_socket.accept()
                    client = threading.Thread(target=self.gestion, args=(connexion, adresse))
                    client.daemon = True
                    client.start()
                except KeyboardInterrupt:
                    print("\n[INTERRUPTION] Arrêt du serveur...")
                    break
                except Exception as e:
                    print(f"[ERREUR] Écoute interrompue: {e}")
                    break
        except Exception as e:
            print(f"[ERREUR] Impossible de démarrer le serveur: {e}")
        finally:
            self.server_socket.close()
            print("[INFO] Serveur arrêté.")

if __name__ == "__main__":
    server = Server()
    server.ecoute()
