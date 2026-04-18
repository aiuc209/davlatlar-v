davlatlar = ["O'zbekiston", "Rossiya", "AQSH", "Xitoy"]
poytaxtlar = ["Toshkent", "Moskva", "Vashington", "Pekin"]

for davlat, poytaxt in zip(davlatlar, poytaxtlar):
    print(f"Poytaxti — {poytaxt} {davlat} davlati uchun")
