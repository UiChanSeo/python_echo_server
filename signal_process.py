###############################################
# signal_process.py
#

import signal
from socket_control import fint_socket


def signal_handler(sig_num, msg):
    fint_socket()


def init_signal():
    signal.signal(signal.SIGINT, signal_handler) 
