import csv

import requests
import os
import re
from datetime import date
import matplotlib.pyplot as plt


class Pump:
    def __init__(self, number_pump):
        self.number_pump = number_pump

    # ubah pump
    def change_pump(self):
        print("Nomor pompa sekarang: ", self.number_pump)
        try:
            number = int(input("Nomor Pompa Baru: "))
            if number > 0:
                if number != self.number_pump:
                    self.number_pump = number
                    print("Nomor pompa berhasil di ubah")
                else:
                    print("Nomor Pompa Tidak Berubah")
            else:
                print("Masukkan tidak Valid, pompa tidak berubah")
        except ValueError:
            print("Masukkan tidak Valid, pompa tidak berubah")


# fungsi mengambil member dan dijalankan pertama kali
# ketika program dijalankan
def get_member():
    list_member = list()

    if not os.path.isfile('member_list.csv'):
        print('create file')
        with open('member_list.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nama", "Poin", "Waktu_Isi_Terakhir"])
    if not os.path.isfile('history_bbm.csv'):
        with open('history_bbm.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["No_Dispenser", "ID_member", "Jenis", "Jumlah", "Waktu", "Uploaded"])

    with open('member_list.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            list_member.append(row)
    return list_member


# fungsi membaca file history
# dan mengembalikan berupa list
def get_history():
    list_history = list()
    with open('history_bbm.csv', 'r', newline="") as read_obj:
        reader = csv.reader(read_obj)
        for row in reader:
            list_history.append(row)
    return list_history


# fungsi menampilkan menu
def display_menu():
    menu = ["-- menu --",
            "1. Tampilkan Jenis dan Harga bahan bakar ",
            "2. Ganti Nomor Pompa",
            "3. Tampilkan Informasi Member",
            "4. Isi Bahan Bakar",
            "5. Upload Data Penjualan",
            "6. Tampilkan Visualisasi Penjualan Harian",
            "7. Tampilkan Visualisasi Penjualan Sepanjang Waktu",
            "0. Exit"]
    for i in menu:
        print(i)


# fungsi mengambil harga
def get_fuel():
    try:
        response = requests.get('http://52.221.79.154/api/fuelTypes')
        if response.status_code == 200:
            return response.json()
        else:
            print('gagal menampilkan fuel')
    except requests.exceptions.RequestException as e:
        print('error: ', e)


# fungsi menampilkan
# bbm dan harga nya
def show_fuel():
    print("jenis BBM per liter")
    for i in fuels:
        print(i['name'], '-', i['price'])


# fungsi menampilkan
# id member
def show_id():
    print("Berikut list ID member yang terdaftar:")
    for i in member[1:]:
        print("-  ", i[0])


# fungsi menampilkan
# member berdasarkan id
def show_member(id):
    find = False
    for x in member:
        if id == x[0]:
            find = True
            print("ID member: ", x[0])
            print("Nama: ", x[1])
            print("Poin: ", x[2])
            print("Waktu pengisian terakhir: ", x[3])

    if not find:
        print("ID member tidak ditemukan")


# fungsi mendapatkan
# tanggal hari ini
def get_date():
    return str(date.today().day) + "/" + str(date.today().month) + "/" + str(date.today().year)


# fungsi menulis history
# setelah pengisian bahan bakar
def write_history(no, id, jenis, jumlah):
    list_member = get_member()
    today = get_date()

    for i in list_member:
        if id in i:
            i[2] = int(i[2]) + 1
            i[3] = today

    with open('member_list.csv', 'w', newline="") as write_obj:
        writer = csv.writer(write_obj)
        for i in list_member:
            writer.writerow(i)

    with open('history_bbm.csv', "a", newline="") as write_obj:
        writer = csv.writer(write_obj)
        writer.writerow([no, id, jenis, jumlah, today, False])


# fungsi mengecek
# inputan id member
def is_valid(x):
    return re.search("^\d{8}[A-Z]{3}$", x)


# fungsi menyimpan data history
# setelah berhasil dikirim
def save_data(list_history):
    for i in list_history[1:]:
        i[5] = True
    with open('history_bbm.csv', 'w', newline="") as write_obj:
        writer = csv.writer(write_obj)
        for i in list_history:
            writer.writerow(i)


# fungsi mengirim data
# ke url yang telah ditentukan
def upload_data():
    list_history = get_history()
    list_json = list()
    list_key = ["date", "fuelVolume", "fuelType", "nominal", "memberNo"]

    for i in list_history[1:]:
        if i[5] == 'False':
            price = 0
            for fuel in fuels:
                if i[2] in fuel['name']:
                    price = int(fuel['price']) * int(i[3])
                    break
            item = {
                list_key[0]: i[4],
                list_key[1]: i[3],
                list_key[2]: i[2],
                list_key[3]: price,
                list_key[4]: i[1]
            }
            list_json.append(item)
    # todo ganti angka terakhir dengan no kelompok
    response = requests.post("http://52.221.79.154/api/recap/765", json=list_json)
    if response.status_code == 200:
        print("berhasil mengirim data")
        save_data(list_history)
    else:
        print("gagal mengirim data")


# fungsi menampilkan penjualan harian
def visualize_history(search_date):
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
              '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    
    list_history = get_history()
    del list_history[0]
    list_history = list(filter(lambda x: x[4] == search_date, list_history))
    if len(list_history) > 0:
        list_history = list(map(lambda x: [x[2], int(x[3])], list_history))
        dict_history = {}

        for jenis, jumlah in list_history:
            total = dict_history.get(jenis, 0) + jumlah
            dict_history[jenis] = total

        plt.style.use('ggplot')
        plt.title(str("penjualan tanggal " + search_date))

        plt.bar(dict_history.keys(), dict_history.values(), color=colors)
        plt.show()
    else:
        print("data tidak ditemukan")


# fungsi menampilkan
# penjualan sepanjang waktu
def visualize_all():
    list_history = get_history()
    del list_history[0]
    if len(list_history) > 0:
        list_history = list(map(lambda x: [x[4], int(x[3])], list_history))
        dict_history = {}

        for jenis, jumlah in list_history:
            total = dict_history.get(jenis, 0) + jumlah
            dict_history[jenis] = total

        plt.style.use('ggplot')
        plt.title(str("penjualan sepanjang waktu"))
        plt.plot(dict_history.keys(), dict_history.values(), )
        plt.show()


# fungsi utama yang akan dijalankan
def main():
    global current_pump
    global member
    global fuels
    current_pump = Pump(1)
    member = get_member()
    fuels = get_fuel()
    is_exit = True
    while is_exit:
        display_menu()
        input_user = input("Pilihan menu: ")
        if input_user == '1':
            show_fuel()
            input("Press Enter to continue...")
        elif input_user == '2':
            current_pump.change_pump()
            input("Press Enter to continue...")
        elif input_user == '3':
            if len(member) == 1:
                print("- tidak ada member")
            else:
                show_id()
                id_member = input("Masukkan ID member yang ingin ditampilkan: ")
                if is_valid(id_member):
                    show_member(id_member)
                else:
                    print("ID member tidak valid")
            input("Press Enter to continue...")
        elif input_user == '4':
            show_fuel()
            jenis = input("pilih jenis BBM: ")
            find = False
            price = 0
            for fuel in fuels:
                if jenis in fuel['name']:
                    find = True
                    price = fuel['price']
            if find:
                try:
                    liter = int(input("masukkan jumlah liter: "))
                    total = price * liter
                    print("Total Harga: ", total)
                    is_lanjut = input("Lanjutkan pembelian\t(LANJUT/BATAL)?: ")
                    if is_lanjut == "LANJUT":
                        id_member = input("masukkan ID member (opsional): ")
                        if is_valid(id_member) or id_member == "-":
                            write_history(current_pump.number_pump, id_member, jenis, liter)
                            print("Transaksi selesai")
                        else:
                            print("id tidak valid")
                    elif is_lanjut == "BATAL":
                        print("Tidak jadi membeli")
                except ValueError:
                    print("Input error")
            else:
                print("jenis bensin tidak ditemukan")

            input("Press Enter to continue...")
        elif input_user == '5':
            upload_data()
            input("Press Enter to continue...")
        elif input_user == '6':
            search_date = input("masukkan tanggal: ")
            visualize_history(search_date)
        elif input_user == '7':
            visualize_all()
        elif input_user == '0':
            upload_data()
            is_exit = False
            input("Press Enter to continue...")
        os.system('cls')


if __name__ == "__main__":
    main()
