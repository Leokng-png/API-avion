import requests
import json
import os

response = requests.get("https://opensky-network.org/api/states/all")
data = response.json()
avions = data['states']
print(len(avions))
def nettoyer_avion(avion):
    return {
        'icao24': avion[0],
        'callsign': avion[1].strip(),
        'origin_country': avion[2],
        'time_position': avion[3],
        'last_contact': avion[4],
        'longitude': avion[5],
        'latitude': avion[6],
        'baro_altitude': avion[7],
        'on_ground': avion[8],
        'velocity': avion[9],
        'true_track': avion[10],
        'vertical_rate': avion[11],
        'sensors': avion[12],
        'geo_altitude': avion[13],
        'squawk': avion[14],
        'spi': avion[15],
        'position_source': avion[16]
    }
avions_nettoyes = [nettoyer_avion(avion) for avion in avions]
vols_par_pays = {}
for avion in avions_nettoyes:
    pays = avion['origin_country']
    if pays not in vols_par_pays:
        vols_par_pays[pays] = []
    vols_par_pays[pays].append(avion)
os.makedirs('vols_par_pays', exist_ok=True)
for pays, liste_avions in vols_par_pays.items():
    nom_fichier = os.path.join('vols_par_pays', f"{pays}.json")
    with open(nom_fichier, 'w') as f:
        json.dump(liste_avions, f, indent=4)
