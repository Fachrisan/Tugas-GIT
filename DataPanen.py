data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

print()
for k, d in data_panen.items():
    print(f"{d['nama_lokasi']}: {d['hasil_panen']}")

print() 
print(f"Jumlah hasil panen jagung dari lokasi 2: {data_panen['lokasi2']['hasil_panen']['jagung']}")

print()
print(f"Nama lokasi dari lokasi 3: {data_panen['lokasi3']['nama_lokasi']}")

print()
padilokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
kedelailokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']
padilokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
kedelailokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']
padilokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
kedelailokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']
padilokasi4 = data_panen['lokasi4']['hasil_panen']['padi']
kedelailokasi4 = data_panen['lokasi4']['hasil_panen']['kedelai']
padilokasi5 = data_panen['lokasi5']['hasil_panen']['padi']
kedelailokasi5 = data_panen['lokasi5']['hasil_panen']['kedelai']

print(f"Padi lokasi1: {padilokasi1}, kedelai lokasi1{kedelailokasi1}")
print(f"Padi lokasi2: {padilokasi2}, kedelai lokasi1{kedelailokasi2}")
print(f"Padi lokasi3: {padilokasi3}, kedelai lokasi1{kedelailokasi3}")
print(f"Padi lokasi4: {padilokasi4}, kedelai lokasi1{kedelailokasi4}")
print(f"Padi lokasi5: {padilokasi5}, kedelai lokasi1{kedelailokasi5}")


print()
hasil_panen_padi ={}
hasil_panen_kedelai ={}

for k , d in data_panen.items():
    hasil_panen_padi[k] = d['hasil_panen']['padi']
    hasil_panen_kedelai[k] = d['hasil_panen']['kedelai']

print("Hasil panen padi :", hasil_panen_padi)
print("Hasil panen kedelai :", hasil_panen_kedelai)

print()
for k , d in data_panen.items():
    padi = d ['hasil_panen']['padi']
    jagung = d ['hasil_panen']['jagung']

    print(f"{k} {d['nama_lokasi']}")
    if padi > 1300 or jagung > 800: 
        print("Memerlukan perhatian khusus")
    else:
        print("Dalam kondisi baik")
    




