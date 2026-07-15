import time

teks = """
Tidak semua kisah harus didengar.
Sebagian cukup dipahami oleh hati.
"""

for huruf in teks:
    print(huruf, end="", flush=True)
    time.sleep(0.05)
