import socket

def skanna_mal(mal, antal_portar):
    print(f"\nBörjar skanna för {mal}")
    for port in range(1, antal_portar + 1):
        skanna_port(mal, port)

def skanna_port(ip_adress, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            resultat = sock.connect_ex((ip_adress, port))
            if resultat == 0:
                print(f"[+] Port {port} är öppen")
    except Exception as e:
        print(f"Fel: {e}")

mal_lista = input("[] Ange mål att skanna (separera med kommatecken): ").strip().split(',')
antal_portar = int(input("[] Ange antal portar du vill skanna: "))

print("[*] Skannar flera mål")
for mal in mal_lista:
    skanna_mal(mal.strip(), antal_portar)