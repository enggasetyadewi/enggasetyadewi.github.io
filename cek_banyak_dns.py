import socket

domains = [
    "google.com",
    "github.com",
    "youtube.com"
]

for domain in domains:
    try:
        ip = socket.gethostbyname(domain)
        print(f"{domain} -> {ip}")
    except:
        print(f"{domain} -> Gagal")
