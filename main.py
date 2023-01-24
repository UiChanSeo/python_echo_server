###############################################
# main.py

from signal_process import init_signal, fint_socket
from socket_control import init_socket, do_server

HOST = '0.0.0.0'
PORT = 8888
socket_handle = None

if __name__ == "__main__":
    socket_handle = init_socket(HOST, PORT)
    init_signal()
    do_server()
    fint_socket()
