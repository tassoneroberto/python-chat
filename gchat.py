import sys
import select
import socket

IP_ADDRESS = '127.0.0.1'
PORT = 12345
MAX_CLIENTS = 20
BUFFER_SIZE = 4096
ENCODING = 'utf-8'


def chat_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((IP_ADDRESS, PORT))
    server.listen(MAX_CLIENTS)
    all_sockets = [server, sys.stdin]
    print("Chat Server started!")
    print("IP address: " + IP_ADDRESS)
    print("Max clients: " + str(MAX_CLIENTS))
    while True:
        rlist, wlist, _ = select.select(
            all_sockets, [], [], 0)
        for read_socket in rlist:
            if read_socket == server:
                conn, address = server.accept()
                all_sockets.append(conn)
            elif read_socket == sys.stdin:
                message = sys.stdin.readline().strip().replace('\n', ' ').replace('\r', '')
                if message != '':
                    for s in all_sockets:
                        if s != server and s != sys.stdin:
                            s.send(
                                bytearray(str(message) + ' [by Server]', ENCODING))
            else:
                message = read_socket.recv(BUFFER_SIZE)
                print(str(message, ENCODING),
                      "[by "+str(read_socket.getpeername())+"]")
                if message:
                    for s in all_sockets:
                        if s != server and s != read_socket and s != sys.stdin:
                            s.send(bytearray(
                                str(message, ENCODING)+' [by ' + str(read_socket.getpeername()) + ']', ENCODING))
                else:
                    if read_socket in all_sockets:
                        all_sockets.remove(read_socket)
    server.close()


def chat_client(host):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, PORT))
    print('Connected!')
    while True:
        all_sockets = [sys.stdin, client]
        rlist, wlist, xlist = select.select(
            all_sockets, [], [])
        for s in rlist:
            if s == client:
                message = s.recv(BUFFER_SIZE)
                sys.stdout.write(str(message, ENCODING)+"\n")
            else:
                message = sys.stdin.readline().strip().replace('\n', ' ').replace('\r', '')
                client.send(bytearray(message, ENCODING))


if __name__ == "__main__":
    if(len(sys.argv) == 2):
        sys.exit(chat_client(sys.argv[1]))
    elif(len(sys.argv) == 1):
        sys.exit(chat_server())
    else:
        raise Exception('Error')
