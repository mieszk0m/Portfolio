import hashlib
from Winternitz import podpisz_winternitz, zweryfikuj_winternitz, generuj_klucze_winternitz, klucz_prywatny,klucz_publiczny,klucze_prywatne, klucze_publiczne, wiadomosc, w
def generuj_drzewo_merkle_i_sciezki(klucze_publiczne, funkcja_hash=hashlib.sha256):


    def stworz_sciezke_autentykacji(indeks, poziomy):
        sciezka = []
        for poziom in poziomy:
            para = (indeks ^ 1, poziom[indeks ^ 1])
            sciezka.append(para)
            indeks //= 2
        return sciezka

    #generowanie skrotow z kluczy publicznych
    skroty = [funkcja_hash(klucz).digest() for klucz in klucze_publiczne]


    poziomy = [skroty]

    #tworze drzewo
    while len(skroty) > 1:
        skroty_nowe = []
        for i in range(0, len(skroty), 2):
            skrot_polaczony = skroty[i] + (skroty[i + 1] if i + 1 < len(skroty) else skroty[i])
            skroty_nowe.append(funkcja_hash(skrot_polaczony).digest())

        poziomy.append(skroty_nowe)
        skroty = skroty_nowe

    sciezki_autentykacji = [stworz_sciezke_autentykacji(i, poziomy) for i in range(len(klucze_publiczne))]

    return poziomy[-1][0], sciezki_autentykacji

#funckja do podpisywania wiadomosci uzywając drzewa Merkle i Winternitza
def podpisz_wiadomosc_merkle_winternitz(wiadomosc, indeks_klucza, klucze_prywatne, sciezki_autentykacji, w, funkcja_hash=hashlib.sha256):
    podpis_winternitz = podpisz_winternitz(wiadomosc, klucze_prywatne[indeks_klucza], w)

    sciezka_autentykacji = sciezki_autentykacji[indeks_klucza]
    return podpis_winternitz, sciezka_autentykacji

#funcjea do weryfikacji podpisu
def zweryfikuj_podpis_merkle_winternitz(wiadomosc, podpis, sciezka_autentykacji, korzen_drzewa, klucze_publiczne, w, funkcja_hash=hashlib.sha256):
    podpis_winternitz, sciezka_autentykacji = podpis

    if not zweryfikuj_winternitz(wiadomosc, podpis_winternitz, klucze_publiczne[sciezka_autentykacji[0][0]//2], w):
        return False

#odtwarzanie korzenia drzewa Merklea
    skrot = funkcja_hash(klucze_publiczne[sciezka_autentykacji[0][0]//2]).digest()
    for indeks, wartosc in sciezka_autentykacji:
        if indeks % 2 == 0:

            skrot = funkcja_hash(skrot + wartosc).digest()
        else:
            skrot = funkcja_hash(wartosc + skrot).digest()

    return skrot == korzen_drzewa

#generuje drzewa merkla i sciezki autentykacji
korzen_drzewa, sciezki_autentykacji = generuj_drzewo_merkle_i_sciezki(klucze_publiczne)

indeks_klucza = 0

podpis, sciezka = podpisz_wiadomosc_merkle_winternitz(wiadomosc, indeks_klucza, klucze_prywatne, sciezki_autentykacji, w)
wynik_weryfikacji = zweryfikuj_podpis_merkle_winternitz(wiadomosc, (podpis, sciezka), korzen_drzewa, klucze_publiczne, w)
