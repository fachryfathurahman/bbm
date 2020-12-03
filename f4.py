import re
from datetime import date

from f1 import get_fuel


# fungsi mengecek
# inputan id member
from f3 import get_member


def is_valid(x):
    return re.search("^\d{8}[A-Z]{3}$", x)


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


def get_input_fuel(number_pump):
    fuels = get_fuel()
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
                    write_history(number_pump, id_member, jenis, liter)
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
