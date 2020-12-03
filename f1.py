# fungsi menampilkan
# bbm dan harga nya
import requests


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


def show_fuel():
    print("jenis BBM per liter")
    for i in get_fuel():
        print(i['name'], '-', i['price'])

