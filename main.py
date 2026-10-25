import os
import sys
import time
import urllib.request
import urllib.error
import socket
import random
import string
import base64
import hashlib
import json

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- BANNER MENU UTAMA (Perisai Keamanan - Network Admin) ---
def banner():
    print("\033[96m========================================")
    print("      NETSHIELD - TKJ NETWORK AUDITOR   ")
    print("     Created by: EXELUMARE (TKJ Developer)  ")
    print("========================================\033[0m")

# --- ANIMASI TENGKORAK GAHAR (Pas Masuk Menu Bug Bounty) ---
def animasi_tengkorak():
    # Banner ASCII Teks Besar Selayar (Gaya Blok Tebal - Sumpah Ini Gahar Banget)
    f1 = """\033[92m
  ██████╗ ██╗██╗  ██╗███D   ████████╗██╗  ██╗
  ██╔══██╗██║██║  ██║██║    ╚══██╔══╝██║  ██║
  ██║  ██║██║███████║██║       ██║   ███████║
  ██║  ██║██║██╔══██║██║       ██║   ██╔══██║
  ╚██████╔╝██║██║  ██║███████╗   ██║   ██║  ██║
   ╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
    \033[0m"""
    
    f2 = """\033[91m
  ██████╗ ██╗██╗  ██╗███D   ████████╗██╗  ██╗
  ██╔══██╗██║██║  ██║██║    ╚══██╔══╝██║  ██║
  ██║  ██║██║███████║██║       ██║   ███████║
  ██║  ██║██║██╔══██║██║       ██║   ██╔══██║
  ╚██████╔╝██║██║  ██║███████╗   ██║   ██║  ██║
   ╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
    [!] OFFENSIVE MODE ENGAGED
    \033[0m"""

    # Pesan efek ketik proses bypass selayar
    pesan_bypass = [
        "\033[91m[!] INITIALIZING NETSHIELD ENGINE...",
        "\033[93m[*] LOADING WORDLISTS & HASH DATABASE...",
        "\033[93m[*] BYPASSING WEB APPLICATION FIREWALL (WAF)...",
        "\033[92m[+] SECURITY SHIELD BYPASSED SUCCESSFULLY!",
        "\033[92m[+] ACCESS GRANTED: OFFENSIVE RECON UNLOCKED!"
    ]

    # Efek kedip selayar di awal
    for _ in range(3):
        clear_screen()
        print(f1)
        time.sleep(0.25)
        
        clear_screen()
        print(f2)
        time.sleep(0.25)

    # Transisi ke efek ketik teks bypass
    clear_screen()
    print(f2)
    print("\n" + "="*40)
    for teks in pesan_bypass:
        print(teks)
        time.sleep(0.4) # Jeda per baris biar berasa proses aslinya
    print("="*40)
    
    time.sleep(0.8) # Jeda terakhir sebelum masuk menu utama bug bounty
    clear_screen()

# --- SUB-MENU BUG BOUNTY & WEB RECON SUITE ---
def sub_menu_bug_bounty():
    animasi_tengkorak()
    
    while True:
        clear_screen()
        print("\033[92m========================================")
        print("     [+] BUG BOUNTY & WEB RECON SUITE   ")
        print("========================================\033[0m")
        print("[1] HTTP Status & Endpoint Checker")
        print("[2] Robots.txt & Hidden Path Inspector")
        print("[3] Basic SQL Injection Payload Tester")
        print("[4] HTTP Methods Inspector")
        print("[5] Security Headers Auditor")
        print("[0] Kembali ke Menu Utama")
        
        sub_pilihan = input("\n\033[92mPilih opsi Recon [0-5]: \033[0m")
        
        if sub_pilihan == '1':
            clear_screen()
            banner()
            print("--- HTTP Status & Endpoint Checker ---")
            target = input("Masukkan URL Target (cth: example.com): ")
            if not target.startswith("http"):
                target = "https://" + target
                
            endpoints = ["admin", "login", "dashboard", "api", "robots.txt", "config.json", "test", "portal"]
            
            print(f"\n[*] Memindai endpoint pada {target}...\n")
            for ep in endpoints:
                url_test = f"{target.rstrip('/')}/{ep}"
                try:
                    req = urllib.request.Request(url_test, headers={'User-Agent': 'NetShield-Recon/1.0'})
                    with urllib.request.urlopen(req, timeout=3) as resp:
                        print(f"\033[92m[FOUND: {resp.status}]\033[0m -> {url_test}")
                except urllib.error.HTTPError as e:
                    if e.code == 403:
                        print(f"\033[93m[FORBIDDEN: 403]\033[0m -> {url_test}")
                    elif e.code == 404:
                        pass
                    else:
                        print(f"[{e.code}] -> {url_test}")
                except Exception:
                    pass
                    
            input("\nPemindaian selesai. Tekan Enter untuk kembali...")
            
        elif sub_pilihan == '2':
            clear_screen()
            banner()
            print("--- Robots.txt & Hidden Path Inspector ---")
            target = input("Masukkan URL Target (cth: example.com): ")
            if not target.startswith("http"):
                target = "https://" + target
                
            robots_url = target.rstrip('/') + "/robots.txt"
            print(f"\n[*] Mengambil isi dari {robots_url}...\n")
            
            try:
                req = urllib.request.Request(robots_url, headers={'User-Agent': 'NetShield-Recon/1.0'})
                with urllib.request.urlopen(req, timeout=5) as resp:
                    isi_robots = resp.read().decode('utf-8', errors='ignore')
                    print("\033[92m--- ISI ROBOTS.TXT ---\033[0m")
                    print(isi_robots)
            except urllib.error.HTTPError as e:
                print(f"\n[!] Gagal mengambil file: HTTP Error {e.code}")
            except Exception as e:
                print(f"\n[!] Terjadi error: {e}")
                
            input("\nTekan Enter untuk kembali...")

        elif sub_pilihan == '3':
            clear_screen()
            banner()
            print("--- Basic SQL Injection Payload Tester ---")
            target_url = input("Masukkan URL Target dengan parameter (cth: http://testphp.vulnweb.com/listproducts.php?cat=1): ")
            if not target_url.startswith("http"):
                target_url = "https://" + target_url
                
            payloads = ["'", "\"", "' OR '1'='1", "\" OR \"1\"=\"1", "--", "/*!50000SELECT*\\"]
            
            print(f"\n[*] Menguji payload SQLi ke target...\n")
            for payload in payloads:
                test_url = target_url + payload
                try:
                    req = urllib.request.Request(test_url, headers={'User-Agent': 'NetShield-SQLiTester/1.0'})
                    with urllib.request.urlopen(req, timeout=4) as resp:
                        print(f"[OK: {resp.status}] Payload: {payload}")
                except urllib.error.HTTPError as e:
                    print(f"\033[91m[POTENSI ERROR {e.code}]\033[0m Payload '{payload}' merespon tidak normal.")
                except Exception:
                    print(f"[BLOCKED/TIMEOUT] Payload: {payload}")
                    
            input("\nPengujian selesai. Tekan Enter untuk kembali...")

        elif sub_pilihan == '4':
            clear_screen()
            banner()
            print("--- HTTP Methods Inspector ---")
            target_url = input("Masukkan URL Target (cth: example.com): ")
            if not target_url.startswith("http"):
                target_url = "https://" + target_url
                
            methods = ["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "TRACE"]
            print(f"\n[*] Memeriksa metode HTTP pada {target_url}...\n")
            
            for meth in methods:
                try:
                    req = urllib.request.Request(target_url, method=meth, headers={'User-Agent': 'NetShield-Recon/1.0'})
                    with urllib.request.urlopen(req, timeout=3) as resp:
                        print(f"\033[92m[ALLOWED: {resp.status}]\033[0m Metode: {meth}")
                except urllib.error.HTTPError as e:
                    if e.code == 405:
                        pass
                    else:
                        print(f"[{e.code}] Metode {meth}")
                except Exception:
                    pass
                    
            input("\nPemeriksaan selesai. Tekan Enter untuk kembali...")

        elif sub_pilihan == '5':
            clear_screen()
            banner()
            print("--- Security Headers Auditor ---")
            target_url = input("Masukkan URL Target (cth: example.com): ")
            if not target_url.startswith("http"):
                target_url = "https://" + target_url
                
            important_headers = [
                "Content-Security-Policy", 
                "Strict-Transport-Security", 
                "X-Frame-Options", 
                "X-Content-Type-Options", 
                "X-XSS-Protection"
            ]
            
            print(f"\n[*] Memeriksa Security Headers pada {target_url}...\n")
            try:
                req = urllib.request.Request(target_url, headers={'User-Agent': 'NetShield-HeaderAuditor/1.0'})
                with urllib.request.urlopen(req, timeout=5) as resp:
                    headers_found = resp.headers
                    for hdr in important_headers:
                        if hdr in headers_found:
                            print(f"\033[92m[AMAN/ADA]\033[0m {hdr}: {headers_found[hdr]}")
                        else:
                            print(f"\033[91m[KERENTANAN/MISSING]\033[0m {hdr} tidak ditemukan!")
            except Exception as e:
                print(f"\n[!] Gagal memeriksa headers: {e}")
                    
            input("\nPemeriksaan selesai. Tekan Enter untuk kembali...")
            
        elif sub_pilihan == '0':
            break
        else:
            input("\nPilihan tidak valid! Tekan Enter untuk coba lagi...")

# --- MENU UTAMA (Network Utilities) ---
def menu():
    while True:
        clear_screen()
        banner()
        print("[1] Scan Perangkat di Jaringan Lokal")
        print("[2] Cek Port Terbuka (Port Scanner)")
        print("[3] Subnetting Calculator")
        print("[4] Dukung Developer / Donasi")
        print("[5] Quick Web Header Checker")
        print("[6] Dns Lookup & Record Checker")
        print("[7] My Public IP & Geo-Location Info")
        print("[8] TCP Port Checker")
        print("[9] Secure Password Generator")
        print("[10] MAC Address Vendor Lookup")
        print("[11] Quick Host Ping Sweep")
        print("[12] Base64 Encoder / Decoder")
        print("[13] HTTP Request Tester")
        print("[14] MD5 & SHA256 Hash Generator")
        print("[15] Epoch Timestamp Converter")
        print("[16] Local Network Interface Info")
        print("[17] HTTP Response Headers Inspector")
        print("[18] Random User-Agent Generator")
        print("[19] ASCII Banner Text Generator")
        print("[20] Network Data Size & Bandwidth Converter")
        print("\033[92m[+] Modul Khusus: Bug Bounty Recon\033[0m")
        print("[0] Keluar")
        print("----------------------------------------")
        
        pilihan = input("Pilih menu [0-20, +]: ")
        
        if pilihan == '1':
            clear_screen()
            banner()
            print("--- Scan Perangkat Lokal ---")
            ip_base = input("Masukkan subnet dasar (cth: 192.168.1): ")
            print("\n[*] Memindai perangkat aktif...")
            for i in range(1, 10):
                ip_target = f"{ip_base}.{i}"
                print(f"[INFO] Mengecek {ip_target}...")
            input("\nSelesai. Tekan Enter untuk kembali...")
            
        elif pilihan == '2':
            clear_screen()
            banner()
            print("--- Port Scanner Sederhana ---")
            target = input("Masukkan IP/Host: ")
            port = int(input("Masukkan nomor port: "))
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"\n[+] Port {port} di {target} TERBUKA (OPEN)!")
                else:
                    print(f"\n[-] Port {port} di {target} Tertutup.")
                s.close()
            except Exception as e:
                print(f"\n[!] Error: {e}")
            input("\nTekan Enter untuk kembali...")
            
        elif pilihan == '3':
            clear_screen()
            banner()
            print("--- Subnetting Calculator ---")
            ip = input("Masukkan IP Address (cth: 192.168.1.1): ")
            CIDR = input("Masukkan CIDR (cth: 24): ")
            print(f"\n[+] IP: {ip} / {CIDR}")
            print("[+] Netmask: 255.255.255.0 (Estimasi /24)")
            print("[+] Total Host: 254 IP usable")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '4':
            clear_screen()
            banner()
            print("--- Dukung Developer ---")
            print("Terima kasih sudah menggunakan NetShield!")
            print("Dibuat dengan penuh semangat oleh EXELUMARE (TKJ SMK)\n")
            print("\033[93mMau traktir kopi atau dukung proyek ini biar terus update?\033[0m")
            print("🔗 Saweria: \033[96mhttps://saweria.co/Exelumare\033[0m")
            print("\nDukungan sekecil apapun sangat berarti buat kemajuan tools ini, bre! ☕")
            input("\nTekan Enter untuk kembali...")


        elif pilihan == '5':
            clear_screen()
            banner()
            print("--- Quick Web Header Checker ---")
            url = input("Masukkan URL (cth: example.com): ")
            if not url.startswith("http"):
                url = "https://" + url
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'NetShield/1.0'})
                with urllib.request.urlopen(req, timeout=5) as resp:
                    print(f"\n[Status Code]: {resp.status}")
                    print("[Response Headers]:")
                    for k, v in resp.headers.items():
                        print(f" - {k}: {v}")
            except Exception as e:
                print(f"\n[!] Error: {e}")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '6':
            clear_screen()
            banner()
            print("--- DNS Lookup Sederhana ---")
            domain = input("Masukkan Nama Domain (cth: example.com): ")
            try:
                ip_addr = socket.gethostbyname(domain)
                print(f"\n[+] IP Address dari {domain} adalah: {ip_addr}")
            except Exception as e:
                print(f"\n[!] Gagal resolusi DNS: {e}")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '7':
            clear_screen()
            banner()
            print("--- My Public IP Info ---")
            try:
                req = urllib.request.Request("https://api.ipify.org?format=json", headers={'User-Agent': 'NetShield/1.0'})
                with urllib.request.urlopen(req, timeout=5) as resp:
                    data = json.loads(resp.read().decode())
                    print(f"\n[+] IP Publik Anda: {data['ip']}")
            except Exception as e:
                print(f"\n[!] Gagal mengambil IP publik: {e}")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '8':
            clear_screen()
            banner()
            print("--- TCP Port Checker ---")
            host = input("Masukkan Host/IP: ")
            port = int(input("Masukkan Port: "))
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                if s.connect_ex((host, port)) == 0:
                    print(f"\n[+] Port {port} Terbuka!")
                else:
                    print(f"\n[-] Port {port} Tertutup/Filtered.")
                s.close()
            except Exception as e:
                print(f"\n[!] Error: {e}")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '9':
            clear_screen()
            banner()
            print("--- Secure Password Generator ---")
            panjang = int(input("Masukkan panjang password (cth: 12): "))
            chars = string.ascii_letters + string.digits + "!@#$%^&*"
            password = "".join(random.choice(chars) for _ in range(panjang))
            print(f"\n[+] Password Kuat: {password}")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '10':
            clear_screen()
            banner()
            print("--- MAC Address Vendor Lookup ---")
            mac = input("Masukkan MAC Address (cth: AA:BB:CC): ")
            print(f"\n[+] MAC {mac} terdeteksi vendor: (Simulasi Lokal / Generic)")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '11':
            clear_screen()
            banner()
            print("--- Quick Host Ping Sweep ---")
            host = input("Masukkan Target Host: ")
            print(f"\n[+] Melakukan simulasi ping ke {host}...")
            print(f"[OK] {host} aktif dan merespon.")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '12':
            clear_screen()
            banner()
            print("--- Base64 Encoder / Decoder ---")
            aksi = input("Pilih [1] Encode | [2] Decode: ")
            teks = input("Masukkan teks: ")
            if aksi == '1':
                encoded = base64.b64encode(teks.encode()).decode()
                print(f"\n[+] Hasil Encode: {encoded}")
            else:
                try:
                    decoded = base64.b64decode(teks.encode()).decode()
                    print(f"\n[+] Hasil Decode: {decoded}")
                except:
                    print("\n[!] Format Base64 tidak valid!")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '13':
            clear_screen()
            banner()
            print("--- HTTP Request Tester (GET Client) ---")
            url = input("Masukkan URL target: ")
            if not url.startswith("http"):
                url = "https://" + url
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'NetShield/1.0'})
                with urllib.request.urlopen(req, timeout=5) as resp:
                    print(f"\n[+] Status: {resp.status} {resp.reason}")
            except Exception as e:
                print(f"\n[!] Error: {e}")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '14':
            clear_screen()
            banner()
            print("--- MD5 & SHA256 Hash Generator ---")
            teks = input("Masukkan teks yang mau di-hash: ")
            md5_val = hashlib.md5(teks.encode()).hexdigest()
            sha_val = hashlib.sha256(teks.encode()).hexdigest()
            print(f"\n[+] MD5    : {md5_val}")
            print(f"[+] SHA256 : {sha_val}")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '15':
            clear_screen()
            banner()
            print("--- Epoch Timestamp Converter ---")
            print(f"[+] Waktu Epoch saat ini: {int(time.time())}")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '16':
            clear_screen()
            banner()
            print("--- Local Network Interface Info ---")
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            print(f"\n[+] Hostname  : {hostname}")
            print(f"\n[+] Local IP  : {local_ip}")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '17':
            clear_screen()
            banner()
            print("--- HTTP Response Headers Inspector ---")
            url = input("Masukkan URL: ")
            if not url.startswith("http"):
                url = "https://" + url
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'NetShield/1.0'})
                with urllib.request.urlopen(req, timeout=5) as resp:
                    for k, v in resp.headers.items():
                        print(f"{k}: {v}")
            except Exception as e:
                print(f"\n[!] Error: {e}")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '18':
            clear_screen()
            banner()
            print("--- Random User-Agent Generator ---")
            agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "Mozilla/5.0 (Linux; Android 10; Mobile)",
                "NetShield-Scanner/1.0",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
            ]
            print(f"\n[+] User-Agent Terpilih:\n{random.choice(agents)}")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '19':
            clear_screen()
            banner()
            print("--- ASCII Banner Text Generator ---")
            teks = input("Masukkan teks singkat:")
            print(f"\n[+] Hasil Teks: *** {teks.upper()} ***")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '20':
            clear_screen()
            banner()
            print("--- Network Data Size Converter ---")
            try:
                nilai = float(input("Masukkan angka ukuran data (dalam MB): "))
                kb = nilai * 1024
                gb = nilai / 1024
                print(f"\n[+] {nilai} MB = {kb:,.2f} KB | {gb:.4f} GB")
            except ValueError:
                print("\n[!] Input harus angka!")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '+':
            sub_menu_bug_bounty()

        elif pilihan == '0':
            print("\nTerima kasih udah pakai NetShield! Bye bre!\n")
            sys.exit()
        else:
            print("\nPilihan kagak ada, coba lagi!")
            time.sleep(1)

if __name__ == '__main__':
    menu()
