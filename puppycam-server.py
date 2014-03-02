__author__ = 'Don Reilly'
import socket
import subprocess

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8456))
server_socket.listen(0)

connection = server_socket.accept()[0].makefile('rb')

try:
    cmdline = \
        "vlc --demux h264 - --sout " \
        "'#standard{access=http,mux=ogg,dst=54.186.4.203:8080'"
    player = subprocess.Popen(cmdline.split(), stdin=subprocess.PIPE)
    while True:
        data = connection.read(1024)
        if not data:
            break
        player.stdin.write(data)
finally:
    connection.close()
    server_socket.close()
    player.terminate()