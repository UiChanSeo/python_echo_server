###############################################
# socket_control.py
#

import socket
import sys
from _thread import start_new_thread

ready_socket = None
do_run = True

"""
# initialization of socket
#
# aHost [in] - Host address
# aPort [in] - port number
"""


def init_socket(aHost, aPort):
    global ready_socket
    ready_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f'Socket is created.[{ready_socket}]')

    # bind socket to local host and port
    try:
        ready_socket.bind((aHost, aPort))
    except socket.error as msg:
        print(f'Exception : \n\t{msg}')
        sys.exit()

    ready_socket.listen(10)
    print(f'Socket is now listening.')
    return ready_socket


"""
# finalization of socket connection
"""


def fint_socket():
    global ready_socket
    global do_run

    do_run = False

    if ready_socket is not None:
        ready_socket.close()


"""
# 1) ready user's request
# 2) accept user's request and make data thread.
#
# aReadySocker [in] - Ready Socket Class
"""


def do_server() -> bool:
    global ready_socket, do_run
    from server_thread import server_thread_handle

    if ready_socket is None:
        return False

    while do_run:
        # wait to accept a connection - blocking call
        # now keep talking with the client
        try:
            conn, addr = ready_socket.accept()
            if conn is not None:
                print(f'Connected with {addr[0]}:{str(addr[1])}')
                start_new_thread(server_thread_handle, (conn,))
        except Exception as e:
            print(f'Exception:\n\t{e}')

    return True
