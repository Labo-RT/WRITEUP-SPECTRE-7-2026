import socket
import threading

FLAG = "Bravo ! Voici le flag : S7{App_Ech0_S3rv}"

class Server:
    def __init__(self, host='0.0.0.0', port=57777):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def gestion(self, connexion, adresse):
        try:
            print(f"\nConnecté avec {adresse}")
            connexion.send(FLAG.encode('utf-8'))
            connexion.close()
        except Exception as e:
            print(f"[ERREUR] Erreur avec {adresse}: {e}")
        finally:
            try:
                connexion.close()
            except:
                pass

    def ecoute(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(3)
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
