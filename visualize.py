# fungsi menampilkan
# penjualan sepanjang waktu
import matplotlib.pyplot as plt

from io_file import get_history, get_member
from network import get_fuel


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
    else:
        print("Data history kosong")


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


# fungsi menampilkan
# bbm dan harga nya
def show_fuel():
    print("jenis BBM per liter")
    for i in get_fuel():
        print(i['name'], '-', i['price'])


# fungsi menampilkan
# id member
def show_id():
    print("Berikut list ID member yang terdaftar:")
    for i in get_member()[1:]:
        print("-  ", i[0])


# fungsi menampilkan
# member berdasarkan id
def show_member(id):
    find = False
    for x in get_member():
        if id == x[0]:
            find = True
            print("ID member: ", x[0])
            print("Nama: ", x[1])
            print("Poin: ", x[2])
            print("Waktu pengisian terakhir: ", x[3])

    if not find:
        print("ID member tidak ditemukan")
