import socket

domain = input("Masukkan domain: ")

try:
    ip = socket.gethostbyname(domain)
    print("IP Address:", ip)
except:
    print("Domain tidak ditemukan")
