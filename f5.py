
# fungsi mengirim data
# ke url yang telah ditentukan
import requests

from f1 import get_fuel

# fungsi menyimpan data history
# setelah berhasil dikirim
from f6 import get_history


def save_data(list_history):
    for i in list_history[1:]:
        i[5] = True
    with open('history_bbm.csv', 'w', newline="") as write_obj:
        for i in list_history:
            for item in i:
                if item != '':
                    write_obj.write(str(item)+',')
            write_obj.write('\n')


def upload_data():
    list_history = get_history()
    list_json = list()
    list_key = ["date", "fuelVolume", "fuelType", "nominal", "memberNo"]

    for i in list_history[1:]:
        if i[5] == 'False':
            price = 0
            for fuel in get_fuel():
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
