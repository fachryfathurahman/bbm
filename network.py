# default fuel jika program tidak
#  terhubung internet
import requests

from io_file import get_history, save_data


def get_default_json():
    return [{"id": "pertamacks", "name": "Pertamacks", "price": 8500},
            {"id": "pertamacks_super", "name": "Pertamacks Super", "price": 9000},
            {"id": "pertamacks_pro", "name": "Pertamacks Pro", "price": 9500},
            {"id": "pertamacks_lite", "name": "Pertamacks Lite", "price": 8000},
            {"id": "deckslite", "name": "Deckslite", "price": 9200}, {"id": "decks", "name": "Decks", "price": 9500},
            {"id": "vroom", "name": "Vroom", "price": 15000}, {"id": "pletocks", "name": "Pletocks", "price": 5000}]


# fungsi mengambil harga
def get_fuel():
    try:
        response = requests.get('http://52.221.79.154/api/fuelTypes')
        if response.status_code == 200:
            return response.json()
        else:
            return get_default_json()
    except requests.exceptions.RequestException as e:
        return get_default_json()


# fungsi mengirim data
# ke url yang telah ditentukan
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
