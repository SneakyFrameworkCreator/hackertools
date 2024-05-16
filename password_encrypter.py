import string as str
import time
import random as rand
import json

def load_data_from_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []

def save_data_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

wifi_data = load_data_from_json('wifi_data.json')
if not wifi_data:
    wifi = 0
else:
    wifi = wifi_data[-1]['wifi']  # Startujemy od ostatniej wartości z pliku JSON

letters = str.digits + str.ascii_letters
names = [
    'Grace Cortez',
    'Alma Norman',
    'Aaron Evans',
    'Cameron Hamilton',
    'Jayden Chavez',
    'Walter Harper',
    'Ethan Frank',
    'Ruth Wong',
    'Cory Farmer',
    'Phillip Hicks',
    'Jeremiah Gregory'
]

while True:
    wifi += rand.randint(1, 100000)
    ip_address = '.'.join(str(rand.randint(1, 500)) for _ in range(4))
    
    user_data = {
        'wifi': wifi,
        'ip_address': ip_address,
        'username': ''.join(rand.choice(names)),
        'password': ''.join(rand.choice(letters) for _ in range(12))
    }
    
    wifi_data.append(user_data)
    
    # Zapisz dane do pliku JSON co 100 iteracji
    if len(wifi_data) % 100 == 0:
        save_data_to_json(wifi_data, 'wifi_data.json')
        print("Dane zostały zapisane do pliku JSON.")
    
    print(f'Wifi: {wifi} | IP Address: {ip_address} | Username: {user_data["username"]} | Password: {user_data["password"]}')
    
    time.sleep(0.05)
