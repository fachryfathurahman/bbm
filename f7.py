from f6 import get_history
import matplotlib.pyplot as plt


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
