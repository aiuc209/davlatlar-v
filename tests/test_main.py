def create_poytaxt_satri(davlatlar, poytaxtlar):
    result = []
    for davlat, poytaxt in zip(davlatlar, poytaxtlar):
        result.append(f"Poytaxti — {poytaxt}")
    return result

def test_create_poytaxt_satri():
    davlatlar = ["O'zbekiston", "Rossiya", "AQSH"]
    poytaxtlar = ["Toshkent", "Moskva", "Vashington"]
    expected_result = ["Poytaxti — Toshkent", "Poytaxti — Moskva", "Poytaxti — Vashington"]
    assert create_poytaxt_satri(davlatlar, poytaxtlar) == expected_result

def test_create_poytaxt_satri_empty_lists():
    davlatlar = []
    poytaxtlar = []
    expected_result = []
    assert create_poytaxt_satri(davlatlar, poytaxtlar) == expected_result

def test_create_poytaxt_satri_unequal_length_lists():
    davlatlar = ["O'zbekiston", "Rossiya"]
    poytaxtlar = ["Toshkent", "Moskva", "Vashington"]
    expected_result = ["Poytaxti — Toshkent", "Poytaxti — Moskva"]
    assert create_poytaxt_satri(davlatlar, poytaxtlar) == expected_result
