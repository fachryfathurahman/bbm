import os
from datetime import date


def get_history():
    list_history = list()
    with open('history_bbm.csv', 'r', newline="") as read_obj:
        for line in read_obj:
            row = line.split(',')
            row = list(map(str.strip, row))
            list_history.append(row)

    return list_history


# fungsi menyimpan data history
# setelah berhasil dikirim
def save_data(list_history):
    for i in list_history[1:]:
        i[5] = True
    print(list_history)
    with open('history_bbm.csv', 'w', newline="") as write_obj:
        for i in list_history:
            for item in i:
                if item != '':
                    write_obj.write(str(item)+',')
            write_obj.write('\n')


# fungsi mengambil member dan dijalankan pertama kali
# ketika program dijalankan
def get_member():
    list_member = list()

    if not os.path.isfile('member_list.csv'):
        print('create file')
        with open('member_list.csv', 'w', newline='') as file:
            header = ["ID", "Nama", "Poin", "Waktu_Isi_Terakhir"]
            for item in header:
                file.write(item+',')
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

# fungsi mendapatkan
# tanggal hari ini
def get_date():
    return str(date.today().day) + "/" + str(date.today().month) + "/" + str(date.today().year)


# fungsi menulis history
# setelah pengisian bahan bakar
def write_history(no, id, jenis, jumlah):
    list_member = get_member()
    print(list_member)
    print("this")
    today = get_date()

    for i in list_member:
        if id in i:
            i[2] = int(i[2]) + 1
            i[3] = today

    with open('member_list.csv', 'w', newline="") as write_obj:
        for i in list_member:
            for item in i:
                if item != '':
                    write_obj.write(str(item)+',')
            write_obj.write('\n')

    header = [no, id, jenis, jumlah, today, False]
    with open('history_bbm.csv', "a", newline="") as write_obj:
        for item in header:
            if item != '':
                write_obj.write(str(item)+",")
        write_obj.write("\n")
