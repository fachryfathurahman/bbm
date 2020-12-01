import os
import re

from io_file import get_member, write_history
from network import get_fuel, upload_data
from pump import Pump
from visualize import visualize_all, visualize_history, display_menu, show_fuel, show_id, show_member


# fungsi mengecek
# inputan id member
def is_valid(x):
    return re.search("^\d{8}[A-Z]{3}$", x)


# fungsi utama yang akan dijalankan
def main():
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


if __name__ == '__main__':
    main()
