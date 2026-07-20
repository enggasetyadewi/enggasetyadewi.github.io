import urllib.request

url = input("Masukkan website: ")

try:
    response = urllib.request.urlopen(url)
    print("Status:", response.status)
    print("Server aktif")
except Exception as e:
    print("Error:", e)
