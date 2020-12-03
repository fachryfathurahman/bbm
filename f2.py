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
