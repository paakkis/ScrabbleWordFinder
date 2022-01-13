def kielletyt_sanat():
    with open("kielletyt.txt", encoding="utf-8") as kielletyt_sanat:
        return [kielletty_sana
                for kielletty_sana in set(kielletyt_sanat.read().split())]

def lataa_sanalista(max_pituus=15):
    with open("sanalista.txt", encoding="utf-8") as sanalista:
        return [sana
                for sana in set(sanalista.read().split())
                if (len(sana) > 1) and (len(sana) <= max_pituus) and sana not in kielletyt_sanat()]

def sanapisteet(sana):
    kirjain_pisteet = {'a': 1, 'b': 8, 'c': 10, 'd': 7,
                     'e': 1, 'f': 8, 'g': 8, 'h': 4,
                     'i': 1, 'j': 4, 'k': 2, 'l': 2,
                     'm': 3, 'n': 1, 'o': 2, 'p': 4,
                     'q': 10, 'r': 4, 's': 1, 't': 1,
                     'u': 4, 'v': 4, 'w': 4, 'x': 8,
                     'y': 4, 'z': 10, 'ä': 2, 'ö': 7}

    return sum([kirjain_pisteet[kirjain] for kirjain in sana])

def mahdollinen_sana(sana, kirjaimet):
    for kirjain in sana:
        if kirjain in kirjaimet:
            kirjaimet = kirjaimet.replace(kirjain, "", 1)
        else:
            return False
    return True

def sanassa_on_kirjaimet(sana, tarvittavat_kirjaimet):
    if not tarvittavat_kirjaimet:
        return True
    else:
        return all(kirjain in sana for kirjain in tarvittavat_kirjaimet)

def hae_kaikki_sanat(kirjaimet, tarvittavat_kirjaimet="", max_pituus=15, alkaa_kirjaimella="", loppuu_kirjaimella=""):
    kirjaimet += alkaa_kirjaimella + loppuu_kirjaimella
    sanat = [(sana, sanapisteet(sana))
             for sana in lataa_sanalista(max_pituus=max_pituus)
             if sana.startswith(alkaa_kirjaimella) and
             sana.endswith(loppuu_kirjaimella) and sanassa_on_kirjaimet(sana, tarvittavat_kirjaimet)
             and mahdollinen_sana(sana, kirjaimet)]

    print(sorted(sanat, key=lambda x: x[1], reverse=True))
