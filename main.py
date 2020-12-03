import os
import re

from f1 import show_fuel
from f2 import Pump
from f3 import get_member, show_id, show_member
from f4 import is_valid, get_input_fuel

from f5 import upload_data
from f6 import visualize_history
from f7 import visualize_all


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


# fungsi utama yang akan dijalankan
def main():
    current_pump = Pump(1)
    member = get_member()

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
            get_input_fuel(current_pump.number_pump)
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
