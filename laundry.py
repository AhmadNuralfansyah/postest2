
list_laundry = []


regular = 2000
medium = 5000
express = 8000


def login():
    global username  
    print("\n===========Login Admin==========")
    username = str(input("Masukan Username : "))
    pas = input("Masukan Password : ")

    if username == "1" and pas == "1":
        admin()
    else:
        print("Invalid")
        login()


def admin():
    print("\n==============ADMIN ONLY===============")
    print(f"Selamat Datang {username}")
    print("Silahkan pilih aksi")
    print("1. Lihat Laundry")
    print("2. Update Status Laundry")
    print("3. Hapus laundry")
    print("4. Keluar")

    aksi = input("Silahkan pilih aksi : ")

    if aksi == "1":
        view()
    elif aksi == "2":
        update()
    elif aksi == "3":
        hapus()
    elif aksi == "4":
        first()
    else:
        print("Invalid")
        admin()


def hapus():
    view()
    nomor_laundry = int(input("pilih list yang akan di hapus ")) - 1
    if 0 <= nomor_laundry < len(list_laundry):
        hapus_list = list_laundry.pop(nomor_laundry)
        print(f"Laundry atas nama {hapus_list[0]} telah dihapus")
    else:
        print("Invalid")
    admin()  


def update():
    view()
    nomor_laundry = int(input("Pilih baris yang ingin di update: ")) - 1
    if 0 <= nomor_laundry < len(list_laundry):
            new_status = str(input("Status saat ini: "))
            list_laundry[nomor_laundry][4] = new_status
            print("Status updated successfully.")
    else:
        print("Invalid")
    login()  
    


def view():
    if not list_laundry:
        print("List kosong")
    else:
        print("\n=============List Laundry=============")
        for nomor_laundry, record in enumerate(list_laundry):
            nama, berat, nmpaket, hasil, status = record
            print(f"{nomor_laundry + 1}. Customer: {nama}, Berat: {berat} kg, Paket {nmpaket}, Harga Rp{hasil}, Status {status}")
            


def costu():
    print("======SELAMAT DATANG DI LAUNDRY=======")
    print("Paket Laundry yang tersedia")
    print("1. Regular")
    print("2. Medium")
    print("3. Express")
    paket = input("\nSilahkan Pilih Paket : ")

    berat = float(input("Masukan berat laundry(kg) : "))

    nama = str(input("Atas nama pemilik: "))

    if paket == '1':
        hasil = berat * regular
        nmpaket = "Regular"
        status = "Pending"
        list_laundry.append([nama, berat, nmpaket, hasil, status])
        print("\n=========Laundry anda Sedang di Proses============")
        print(f"Atas nama {nama}")
        print(f"Paket {nmpaket}")
        print(f"Berat {berat} Kg")
        print(f"Harga Rp {hasil} ")

        back = input("Selesai, Silahkan tekan 1 untuk tambah laundry lagi  = ")
        if back == "1":
            costu()
        else:
            print("Invalid")
            return

    elif paket == '2':
        nmpaket = "Medium"
        hasil = medium * berat
        status = "Pending"
        list_laundry.append([nama, berat, nmpaket, hasil, status])
        print("\nLaundry anda Sedang di Proses")
        print(f"Atas nama {nama}")
        print(f"Paket {nmpaket}")
        print(f"Berat {berat} Kg")
        print(f"Harga Rp{hasil} ")

        back = input("Selesai, Silahkan tekan 1 untuk tambah laundry = ")
        if back == "1":
            costu()
        else:
            print("Invalid")
            return

    elif paket == '3':
        hasil = express * berat
        nmpaket = "Express"
        status = "Pending"
        list_laundry.append([nama, berat, nmpaket, hasil, status])
        print("\nLaundry anda Sedang di Proses")
        print(f"Atas nama {nama}")
        print(f"Paket {nmpaket}")
        print(f"Berat {berat} Kg")
        print(f"Harga Rp{hasil} ")

        back = input("Selesai, Silahkan tekan 1 untuk tambah laundry = ")
        if back == "1":
            costu()
        else:
            print("Invalid")
            return
            

    else:
        print("Invalid")
        costu()


def first():
    while True:
        print("\n============= SELAMAT DATANG DI LAUNDRY ===============")
        print("MASUK SEBAGAI :")
        print("1. Admin")
        print("2. Customer")
        print("3. Keluar")
        user = input("(1/2) = ")
        if user == "1":
            login()
        elif user == "2":
            costu()
        elif user == "3":
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    first()
