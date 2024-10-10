import socket
import json

dns_records = {}

def handle_registration(message):
    parts = message.split("\n")
    if len(parts) < 5 or parts[0] != 'TYPE-A':
        return None

    hostname = parts[1].split("-")[1]
    ip_address = parts[2].split("-")[1]
    ttl = int(parts[3].split("=")[1])

    dns_records[hostname] = {'ip': ip_address, 'ttl': ttl}
    return f"Registered {hostname}"

def dns_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', 53533))

    while True:
        data, addr = sock.recvfrom(1024)
        message = data.decode('utf-8')

        if 'TYPE=A' in message:
            response = handle_registration(message)
            sock.sendto(response.encode('utf-8'), addr)

if __name__ == '__main__':
    dns_server()