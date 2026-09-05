import zmq

context = zmq.Context()
poller = zmq.Poller()

client_socket = context.socket(zmq.ROUTER)
client_socket.bind("tcp://*:5555")
poller.register(client_socket, zmq.POLLIN)

server_socket = context.socket(zmq.DEALER)
server_socket.bind("tcp://*:5556")
poller.register(server_socket, zmq.POLLIN)

print("Broker iniciado.", flush=True)

while True:
    socks = dict(poller.poll())

    if socks.get(client_socket) == zmq.POLLIN:
        while True:
            msg = client_socket.recv()
            if client_socket.getsockopt(zmq.RCVMORE):
                server_socket.send(msg, zmq.SNDMORE)
            else:
                server_socket.send(msg)
                break

    if socks.get(server_socket) == zmq.POLLIN:
        while True:
            msg = server_socket.recv()
            if server_socket.getsockopt(zmq.RCVMORE):
                client_socket.send(msg, zmq.SNDMORE)
            else:
                client_socket.send(msg)
                break