import socket
import threading
import paramiko
import netifaces
import os
import time
from queue import Queue
from colorama import Fore, init

# ================= CONFIG =================
PORT = 22
TIMEOUT = 2
THREADS = 120
# =========================================

init(autoreset=True)

queue = Queue()
hosts = []


def banner():
    os.system("cls")
    print(Fore.CYAN + r"""
 ███████╗███████╗██╗  ██╗    ██████╗ ███████╗███╗   ███╗ ██████╗ ████████╗███████╗
 ██╔════╝██╔════╝██║  ██║    ██╔══██╗██╔════╝████╗ ████║██╔═══██╗╚══██╔══╝██╔════╝
 ███████╗███████╗███████║    ██████╔╝█████╗  ██╔████╔██║██║   ██║   ██║   █████╗  
 ╚════██║╚════██║██╔══██║    ██╔══██╗██╔══╝  ██║╚██╔╝██║██║   ██║   ██║   ██╔══╝  
 ███████║███████║██║  ██║    ██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝   ██║   ███████╗
 ╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚══════╝
    """)
    print(Fore.YELLOW + " SSH REMOTE TOOL")
    print(Fore.GREEN + " Author : Strom81")
    print(Fore.CYAN + "=" * 70 + "\n")


def get_local_network():
    gws = netifaces.gateways()
    iface = gws['default'][netifaces.AF_INET][1]
    addr = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]
    ip = addr['addr']
    p = ip.split('.')
    return f"{p[0]}.{p[1]}.{p[2]}."


def scan_ssh(ip):
    s = socket.socket()
    s.settimeout(TIMEOUT)
    try:
        s.connect((ip, PORT))
        banner = s.recv(1024).decode(errors="ignore").strip()
        banner = banner.replace("SSH-2.0-", "") if banner else "SSH detected"

        hosts.append({"ip": ip, "info": banner})
        print(Fore.GREEN + f"[✓] {ip:15} | {banner}")
    except:
        pass
    finally:
        s.close()


def worker():
    while not queue.empty():
        scan_ssh(queue.get())
        queue.task_done()


def elevate_root(chan, password):
    time.sleep(0.5)
    chan.send("sudo -i\n")
    time.sleep(0.5)
    chan.send(password + "\n")
    time.sleep(1)
    while chan.recv_ready():
        chan.recv(4096)


def ssh_terminal(host):
    os.system("cls")
    print(Fore.CYAN + "🔐 SSH REMOTE (AUTO ROOT)")
    print("=" * 70)
    print(f"IP   : {host['ip']}")
    print(f"INFO : {host['info']}")
    print("=" * 70)

    username = input("Username : ")
    password = input("Password : ")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(
            host["ip"],
            username=username,
            password=password,
            timeout=6,
            look_for_keys=False,
            allow_agent=False
        )

        chan = ssh.invoke_shell()
        time.sleep(1)
        chan.recv(4096)

        elevate_root(chan, password)

        print(Fore.GREEN + "\n[ROOT MODE AKTIF] ketik 'exit' untuk keluar\n")

        while True:
            cmd = input(f"root@{host['ip']}# ")
            if cmd.lower() == "exit":
                break
            chan.send(cmd + "\n")
            time.sleep(0.2)
            while chan.recv_ready():
                print(chan.recv(65535).decode(errors="ignore"), end="")

        ssh.close()

    except paramiko.AuthenticationException:
        print(Fore.RED + "\n❌ Authentication gagal")
        input("ENTER...")
    except Exception as e:
        print(Fore.RED + f"\n❌ Error: {e}")
        input("ENTER...")


def main():
    banner()

    base = get_local_network()
    print(Fore.YELLOW + f"Scanning network: {base}0/24\n")

    for i in range(1, 255):
        queue.put(base + str(i))

    for _ in range(THREADS):
        threading.Thread(target=worker, daemon=True).start()

    queue.join()

    if not hosts:
        print(Fore.RED + "\nTidak ada SSH host ditemukan.")
        return

    print("\nNO  IP ADDRESS        SSH INFO")
    print("────────────────────────────────────────────────────────")
    for i, h in enumerate(hosts, 1):
        print(f"{i:<3} {h['ip']:<16} {h['info']}")

    while True:
        try:
            c = int(input("\nPilih nomor host (0 = keluar): "))
            if c == 0:
                break
            if 1 <= c <= len(hosts):
                ssh_terminal(hosts[c - 1])
                break
        except:
            pass


if __name__ == "__main__":
    main()
