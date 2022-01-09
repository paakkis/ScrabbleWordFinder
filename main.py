def lataa_sanalista(max_pituus=15):
    with open("sanalista.txt") as sanalista:
        return [sana
                for sana in set(sanalista.read().split())
                if (len(sana) > 1) and (len(sana) <= max_pituus)]

def sanapisteet(sana):
    kirjain_pisteet = {'a': 1, 'b': 4, 'c': 4, 'd': 2,
                     'e': 1, 'f': 4, 'g': 3, 'h': 3,
                     'i': 1, 'j': 10, 'k': 5, 'l': 2,
                     'm': 4, 'n': 2, 'o': 1, 'p': 4,
                     'q': 10, 'r': 1, 's': 1, 't': 1,
                     'u': 2, 'v': 5, 'w': 4, 'x': 8,
                     'y': 3, 'z': 10}

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
