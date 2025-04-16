#!/usr/bin/env python3
import socket
import concurrent.futures
import ipaddress
import sys

print("-----LAN SCANNER NOROOT-----")

def is_ip_alive(ip, port=80, timeout=0.5):
    try:
        with socket.create_connection((str(ip), port), timeout=timeout):
            return str(ip), "Alive (Connection Accepted)"
    except ConnectionRefusedError:
        return str(ip), "Alive (Connection Refused)"
    except socket.timeout:
        return str(ip), "Timeout"
    except OSError:
        return str(ip), "Unreachable"

def scan_network(network_cidr):
    ip_net = ipaddress.ip_network(network_cidr, strict=False)
    alive_hosts = []

    print(f"Scanning: {network_cidr} ...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(is_ip_alive, ip) for ip in ip_net.hosts()]
        for future in concurrent.futures.as_completed(futures):
            ip, status = future.result()
            if "Alive" in status:
                print(f"{ip} --> {status}")
                alive_hosts.append(ip)

    return alive_hosts

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: python lan_scan.py <IP Ağı/CIDR>")
        print("Example: python lan_scan.py 192.168.1.0/24")
        sys.exit(1)

    network = sys.argv[1]
    aktif_cihazlar = scan_network(network)

    print("\n-----Active IP Addresses List-----")
    for ip in aktif_cihazlar:
        print(ip)


#by github.com/mirac-s