import os
import hashlib

def generuj_klucze_winternitz(w, funkcja_hash=hashlib.sha256):
    rozmiar_hashu = funkcja_hash().digest_size * 8 
    liczba_elementow = rozmiar_hashu // w

    klucz_prywatny = [os.urandom(funkcja_hash().digest_size) for _ in range(liczba_elementow)]

    klucz_publiczny = []
    for element in klucz_prywatny:
        for _ in range(2 ** w - 1):
            element = funkcja_hash(element).digest()
        klucz_publiczny.append(element)

    return klucz_prywatny, klucz_publiczny


w = 16
klucz_prywatny, klucz_publiczny = generuj_klucze_winternitz(w)


def podpisz_winternitz(wiadomosc, klucz_prywatny, w, funkcja_hash=hashlib.sha256):
    hash_wiadomosci = funkcja_hash(wiadomosc.encode()).digest()
    rozmiar_bloku = w // 8 
    liczba_blokow = len(hash_wiadomosci) // rozmiar_bloku
    bloki_hashu = [int.from_bytes(hash_wiadomosci[i:i+rozmiar_bloku], 'big') for i in range(0, len(hash_wiadomosci), rozmiar_bloku)]

    suma_kontrolna = (2**w - 1) * liczba_blokow - sum(bloki_hashu)
    bloki_sumy_kontrolnej = [(suma_kontrolna >> (i * w)) & ((2**w) - 1) for i in range(liczba_blokow)]

    podpis = []
    #podpiswane bloki skrótu wiadomosci
    for i, blok in enumerate(bloki_hashu):
        element = klucz_prywatny[i]
        for _ in range((2 ** w) - 1 - blok):
            element = funkcja_hash(element).digest()
        podpis.append(element)
    
    #podpisywane y bloki sumy kontrolnej
    for i, blok in enumerate(bloki_sumy_kontrolnej):
        element = klucz_prywatny[liczba_blokow + i] 
        for _ in range((2 ** w) - 1 - blok):
            element = funkcja_hash(element).digest()
        podpis.append(element)

    return podpis
#jak uzyc
wiadomosc = "1234576543"
podpis = podpisz_winternitz(wiadomosc, klucz_prywatny, w)


def zweryfikuj_winternitz(wiadomosc, podpis, klucz_publiczny, w, funkcja_hash=hashlib.sha256):
    hash_wiadomosci = funkcja_hash(wiadomosc.encode()).digest()
    rozmiar_bloku = w // 8

    liczba_blokow = len(hash_wiadomosci) // rozmiar_bloku

    bloki_hashu = [int.from_bytes(hash_wiadomosci[i:i+rozmiar_bloku], 'big') for i in range(0, len(hash_wiadomosci), rozmiar_bloku)]

    suma_kontrolna = (2**w - 1) * liczba_blokow - sum(bloki_hashu)
    bloki_sumy_kontrolnej = [(suma_kontrolna >> (i * w)) & ((2**w) - 1) for i in range(liczba_blokow)]

    #p do przechowywania przetworzonych elementów podpisu
    p = []

    #elementy podpisu odpowiadajace skrotowi wiadomosci
    for i, element_podpisu in enumerate(podpis[:liczba_blokow]):
        for _ in range(bloki_hashu[i]):
            element_podpisu = funkcja_hash(element_podpisu).digest()
        p.append(element_podpisu)

    #przetworzenie elementu podpisu odpowiadajace sumie kontrolnej
    for i, element_podpisu in enumerate(podpis[liczba_blokow:]):
        for _ in range(bloki_sumy_kontrolnej[i]):
            element_podpisu = funkcja_hash(element_podpisu).digest()
        p.append(element_podpisu)

    #porownanie wektor p z kluczem publicznym
    for i, element_p in enumerate(p):
        if element_p != klucz_publiczny[i]:
            return False

    return True


wynik = zweryfikuj_winternitz(wiadomosc, podpis, klucz_publiczny, w)
