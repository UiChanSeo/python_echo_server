###############################################
# server_thread.py
#
import socket
from socket_control import do_run


def server_thread_handle(accepted_handle: socket):
    msgs = 'Welcome to the server. Type something and hit enter.\n'
    accepted_handle.send(msgs.encode('utf-8'))

    # Listen message and quit if user send '^C' with no data.
    # If user send message, this will be resend message.
    while do_run:
        data = accepted_handle.recv(1024)
        if data is not None or len(data) > 0:
            # if data in ['\r\n', '\r', '\n']:
            if data[0] in [0xff]:
                break
            try:
                data = data.decode('utf-8')
                print(f'Received : {data}')
                accepted_handle.sendall(f'OK... : {data}'.encode('utf-8'))
            except Exception as e:
                print(f'Exception:\n\t{e}')
    accepted_handle.close()
