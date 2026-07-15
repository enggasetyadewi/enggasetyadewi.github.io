import random

angka_rahasia = random.randint(1, 10)

tebakan = int(input("Tebak angka 1 sampai 10: "))

if tebakan == angka_rahasia:
    print("🎉 Selamat! Tebakan kamu benar.")
else:
    print("😅 Salah.")
    print("Angka yang benar adalah", angka_rahasia)

