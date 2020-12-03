import matplotlib.pyplot as plt


def get_history():
    list_history = list()
    with open('history_bbm.csv', 'r', newline="") as read_obj:
        for line in read_obj:
            row = line.split(',')
            row = list(map(str.strip, row))
            list_history.append(row)

    return list_history


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
