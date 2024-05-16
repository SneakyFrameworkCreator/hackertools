import random
import time
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

while True:
    wifi += random.randint(1, 100000)
    ip_address = '.'.join(str(random.randint(1, 500)) for _ in range(4))
    print(f'Wifi: {wifi} | IP Address: {ip_address}')
    
    user_data = {
        'wifi': wifi,
        'ip_address': ip_address,
    }
    
    wifi_data.append(user_data)
    
    # Zapisz dane do pliku JSON co 100 iteracji
    if len(wifi_data) % 10 == 0:
        save_data_to_json({'user': user_data}, 'wifi_data.json')
        print("Dane zostały zapisane do pliku JSON.")
    
    time.sleep(0.01)
