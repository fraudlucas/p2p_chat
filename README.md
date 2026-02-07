# P2P Chat Application

A simple peer-to-peer (P2P) messaging system built with Python to demonstrate fundamental P2P networking concepts.

## 📚 Educational Purpose

This repository was created to teach students the core concepts of **peer-to-peer networking architecture**, including:
- How peers discover each other using a centralized tracker
- Direct communication between peers without a central server
- UDP socket programming in Python
- Threading for simultaneous sending and receiving of messages

## 🏗️ Architecture

The application uses a **hybrid P2P model** with a centralized tracker:

```
Peer 1 ←─────────────────┐
                         │
                    Tracker Server
                         │
Peer 2 ←─────────────────┘
   │                  ▲
   │ (discovers)      │ (registers)
   │                  │
   └──────────────────┘
   (direct P2P communication)
```

### Components

- **Tracker** (`tracker.py`): A centralized server that:
  - Listens for incoming peer registrations
  - Collects connection information from peers
  - Facilitates peer discovery by sharing peer addresses
  - Enables direct peer-to-peer connection establishment

- **Peer** (`peer.py`): A P2P client that:
  - Registers with the tracker server
  - Receives information about another peer
  - Establishes direct communication with the peer
  - Can send and receive messages in real-time

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Both machines must be on the same network or have network connectivity

### Installation

Clone the repository:
```bash
git clone <repository-url>
cd p2p_chat
```

No additional dependencies are required (uses Python standard library only).

## 📖 How to Run

### Step 1: Start the Tracker Server

On a machine/terminal that will act as the tracker (e.g., localhost):
```bash
python tracker.py
```

You should see output like:
```
Connection from: ('127.0.0.1', 50001)
Connection from: ('127.0.0.1', 50002)
Got 2 clients, sending details to each one.
```

### Step 2: Start Two Peer Clients

In two separate terminals/machines, run:
```bash
python peer.py
```

**First Peer Output:**
```
Checked in with tracker server, waiting for peer...
got peer
  ip:          127.0.0.1
  source port: 50001
connecting 127.0.0.1 50001

ready to exchange messages
> 
```

**Second Peer Output:**
```
Checked in with tracker server, waiting for peer...
got peer
  ip:          127.0.0.1
  source port: 50002
connecting 127.0.0.1 50002

ready to exchange messages
> 
```

### Step 3: Exchange Messages

Once both peers are running, you can type messages in either terminal:

**Peer 1 Terminal:**
```
> Hello from Peer 1!
> This is a test message
> 
```

**Peer 2 Terminal:**
```
> peer: Hello from Peer 1!
> peer: This is a test message
> Hello back from Peer 2!
> 
```

## 🔧 Configuration

### Peer Port Configuration

To change the port that a peer listens on, edit the `__init__` method in `peer.py`:

```python
def __init__(self):
    self.peer_port = None
    self.peer_ip = None
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.socket.bind(('0.0.0.0', 50001))  # Change 50001 to your desired port
```

For example, to use port 50002:
```python
self.socket.bind(('0.0.0.0', 50002))
```

### Tracker Address Configuration

To modify the tracker address or port, edit the main section in `peer.py`:

```python
if __name__ == "__main__":
    tracker = "127.0.0.1", 55555  # Change tracker IP and port here
```

### Tracker Server Configuration

To change the tracker server address/port, edit `tracker.py`:

```python
if __name__ == '__main__':
    address_port = "0.0.0.0", 55555  # Change listening address and port
```

## 💡 Key Concepts Demonstrated

1. **UDP Communication**: Uses unreliable but fast UDP protocol for messaging
2. **Service Discovery**: Tracker facilitates peer discovery without direct knowledge
3. **Threading**: Simultaneous sending and receiving using Python threads
4. **Socket Programming**: Low-level network socket operations
5. **Decoupled Communication**: Once peers know each other, they communicate directly

## 📝 Notes

- This is a **simplified educational implementation** and is not production-ready
- Uses UDP, so messages are not guaranteed to be delivered in order or at all
- Limited to 2 peers (by design, for simplicity)
- Peers must be started after the tracker is running
- The tracker automatically exits after connecting 2 peers

## 🎓 Learning Extensions

Consider these enhancements to deepen understanding:
- Add TCP for reliable message delivery
- Support multiple peers (modify tracker logic)
- Add persistent peer registration/lookup
- Implement encryption for messages
- Add message acknowledgment and retry logic
- Create a GUI for better user experience

## 📄 License

Feel free to use this for educational purposes. 
