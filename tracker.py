import socket


class Tracker:
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    peers = []

    def __init__(self, tracker_ip_port):
        self.socket.bind(tracker_ip_port)

    def listen(self):
        while True:
            peer_port, peer_address = self.socket.recvfrom(128)
            print('Connection from: {}'.format(peer_address))
            self.peers.append((peer_address, int(peer_port)))

            self.socket.sendto(b'ready', peer_address)

            if len(self.peers) == 2:
                print('Got 2 clients, sending details to each one.')
                break

    def return_peers(self):
        p1, p1_known_port = self.peers.pop()
        p1_address, p1_port = p1
        p2, p2_known_port = self.peers.pop()
        p2_address, p2_port = p2

        print('Peer 1 ---> {} {}'.format(p1_address, p1_port))
        self.socket.sendto('{} {}'.format(p1_address, p1_port).encode(), p2)
        print('Peer 2 ---> {} {}'.format(p2_address, p2_port))
        self.socket.sendto('{} {}'.format(p2_address, p2_port).encode(), p1)


if __name__ == '__main__':
    address_port = "0.0.0.0", 55555

    tracker = Tracker(address_port)
    tracker.listen()
    tracker.return_peers()

