while True:
    print("\n=== MENU ===")
    print("1. Halo")
    print("2. Biodata")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("Halo Engga!")
    elif pilihan == "2":
        print("Nama: Engga Setya Dewi")
        print("Pekerjaan: Maison 114 Cafe")
    elif pilihan == "3":
        print("Sampai jumpa!")
        break
    else:
        print("Pilihan tidak tersedia")
