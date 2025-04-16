#!/usr/bin/env python3
import socket
import concurrent.futures
import ipaddress
import sys

# ANSI renk kodları
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"

print(f"{CYAN}-----LAN SCANNER NOROOT-----{RESET}")

def is_ip_alive(ip, port=80, timeout=0.5):
    try:
        with socket.create_connection((str(ip), port), timeout=timeout):
            return str(ip), f"{GREEN}Alive (Connection Accepted){RESET}"
    except ConnectionRefusedError:
        return str(ip), f"{YELLOW}Alive (Connection Refused){RESET}"
    except socket.timeout:
        return None  
    except OSError:
        return None  
def scan_network(network_cidr):
    ip_net = ipaddress.ip_network(network_cidr, strict=False)
    alive_hosts = []

    print(f"{CYAN}Scanning: {BOLD}{network_cidr}{RESET} ...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(is_ip_alive, ip) for ip in ip_net.hosts()]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                ip, status = result
                print(f"{ip} --> {status}")
                alive_hosts.append(ip)

    return alive_hosts

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{RED}Use: python lan_scan.py <IP/CIDR>")
        print(f"{RED}Example: python lan_scan.py 192.168.1.0/24{RESET}")
        sys.exit(1)

    network = sys.argv[1]
    aktif_cihazlar = scan_network(network)

    print(f"\n{CYAN}-----ACTIVE IP ADDRESSES -----{RESET}")
    for ip in aktif_cihazlar:
        print(f"{GREEN}{ip}{RESET}")


#GitHub by mirac-s  - github.com/mirac-s/lan-scanner-noroot