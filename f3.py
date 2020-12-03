# fungsi mengambil member dan dijalankan pertama kali
# ketika program dijalankan
import os


def get_member():
    list_member = list()

    if not os.path.isfile('member_list.csv'):
        print('create file')
        with open('member_list.csv', 'w', newline='') as file:
            header = ["ID", "Nama", "Poin", "Waktu_Isi_Terakhir"]
            for item in header:
                file.write(item + ',')
            file.write('\n')
    if not os.path.isfile('history_bbm.csv'):
        with open('history_bbm.csv', 'w', newline='') as file:
            header = ["No_Dispenser", "ID_member", "Jenis", "Jumlah", "Waktu", "Uploaded"]
            for item in header:
                file.write(item + ',')
            file.write('\n')

    with open('member_list.csv', 'r') as file:
        for line in file:
            row = line.split(',')
            row = list(map(str.strip, row))
            list_member.append(row)
    return list_member


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
