import socket
import threading


class Peer:

    def __init__(self):
        self.peer_port = None
        self.peer_ip = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', 50001))

    def checkin_tracker(self, tracker_ip_port):
        self.socket.sendto(b'0', tracker_ip_port)
        while True:
            data = self.socket.recv(1024).decode()

            if data.strip() == 'ready':
                print('Checked in with tracker server, waiting for peer...')
                break

        data = self.socket.recv(1024).decode()
        peer_ip, peer_port = data.split(' ')
        peer_port = int(peer_port)

        print('\ngot peer')
        print('  ip:          {}'.format(peer_ip))
        print('  source port: {}'.format(peer_port))

        self.peer_ip = peer_ip
        self.peer_port = peer_port

        # self.socket.sendto(b'0', (peer_ip, peer_port))
        print('connecting {} {}\n'.format(peer_ip, peer_port))

        print('ready to exchange messages\n')

    def listen_thread(self):
        def listen():
            print('Estou escutando aqui ====\n')
            while True:
                data = self.socket.recv(1024)
                print('\rpeer: {}\n> '.format(data.decode()), end='')

        listener = threading.Thread(target=listen, daemon=True)
        listener.start()

    def send_chat(self):
        while True:
            msg = input('> ')
            self.socket.sendto(msg.encode(), (self.peer_ip, self.peer_port))


if __name__ == "__main__":
    tracker = "127.0.0.1", 55555

    client = Peer()
    client.checkin_tracker(tracker)
    client.listen_thread()
    client.send_chat()
