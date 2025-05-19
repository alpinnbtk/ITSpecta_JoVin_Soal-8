list_buku = []
lanjut = True
while lanjut == True:
    print("Selamat Datang di Program Penyimpanan Buku. Silahkan pilih menu yang anda inginkan : ")
    print("1. Tambah Data Buku.")
    print("2. Lihat Data Buku.")
    print("3. Edit Data Buku.")
    print("4. Hapus Data Buku.")
    print("5. Jumlah Buku Terjual.")

    pilihan = int(input("Pilihan Anda : "))

    if pilihan == 1:
        nama_buku = input("Inputkan judul buku : ")
        harga_buku = int(input("Inputkan harga buku : "))
        stok_buku = int(input("Inputkan stok buku : "))
        banyaknya_terjual = 0
        list_buku.append([nama_buku, harga_buku, stok_buku, banyaknya_terjual])
        print("Buku tersebut telah disimpan.")

    elif pilihan == 2:
        for i in range(0, len(list_buku)):
            print("Buku No", (i+1), " : ")
            print("Nama Buku : ", list_buku[i][0])
            print("Harga Buku : ", list_buku[i][1])
            print("Stok Buku : ", list_buku[i][2], "\n")
    elif pilihan == 3:
        for i in range(0, len(list_buku)):
            print("Buku No", (i+1), " : ")
            print("Nama Buku : ", list_buku[i][0])
            print("Harga Buku : ", list_buku[i][1])
            print("Stok Buku : ", list_buku[i][2], "\n")
        
        edit = int(input("Buku mana yang mau anda edit ? (Masukkan No Buku) : "))
        print()

        nama_buku = input("Inputkan judul buku : ")
        harga_buku = int(input("Inputkan harga buku : "))
        stok_buku = int(input("Inputkan stok buku : "))
        banyaknya_terjual = int(input("Banyaknya buku yang terjual : "))
        list_buku.remove(edit-1)
        list_buku.insert(edit-1, [nama_buku, harga_buku, stok_buku, banyaknya_terjual])
        print("Buku tersebut telah diedit.")
    elif pilihan == 4:
        for i in range(0, len(list_buku)):
            print("Buku No", (i+1), " : ")
            print("Nama Buku : ", list_buku[i][0])
            print("Harga Buku : ", list_buku[i][1])
            print("Stok Buku : ", list_buku[i][2], "\n")
        
        edit = int(input("Buku mana yang mau anda edit ? (Masukkan No Buku) : "))
        print()

        list_buku.remove(edit-1)
        print("Buku tersebut telah dihapus.")
    elif pilihan == 5:
        for i in range(0, len(list_buku)):
            print("Buku No", (i+1), " : ")
            print("Nama Buku : ", list_buku[i][0])
            print("Harga Buku : ", list_buku[i][1])
            print("Stok Buku : ", list_buku[i][2], "\n")
        
        edit = int(input("Buku mana yang mau anda beli ? (Masukkan No Buku) : "))
        print()

        banyak = int(input("Berapa banyak yang ingin dibeli ? : "))

        if list_buku[edit-1][2] >= banyak:
            list_buku[edit-1][2] -= banyak
            list_buku[edit-1][3] += banyak
            print("Buku berhasil dibeli!")
        else:
            print("Stok yang tersedia tidak cukup!")
        
    elif pilihan == 6:
         for i in range(0, len(list_buku)):
            print("Buku No", (i+1), " : ")
            print("Nama Buku : ", list_buku[i][0])
            print("Harga Buku : ", list_buku[i][1])
            print("Stok Buku : ", list_buku[i][2], "\n")

            if list_buku[i][3] >= 1 and list_buku[i][3] <= 2:
                print("Status : Buku Terjual Normal")
            elif list_buku[i][3] >= 3 and list_buku[i][3] < 50:
                print("Status : Buku Terjual Banyak")
            elif list_buku[i][3] > 50:
                print("Status : Buku Sangat Laris")
    else:
        print("Menu tersebut tidak tersedia!")

    lanjut = input("Lanjut menggunakan Aplikasi ? (Y / N)")
    if lanjut == "N":
        lanjut = False

