import secrets
import hashlib

# Poprawiony kod
def generowanie_kluczy():
    privat_keys = []
    public_keys = []
    for i in range(0, 256):
        a = secrets.randbits(256)
        b = secrets.randbits(256)
        privat_keys.append([a, b])
        public_keys.append([
            int.from_bytes(hashlib.sha256(a.to_bytes(32, 'big')).digest(), 'big'),
            int.from_bytes(hashlib.sha256(b.to_bytes(32, 'big')).digest(), 'big')
        ])
    return privat_keys, public_keys

def generowanie_podpisu(messege, private_keys):
    M = hashlib.sha256(messege.encode()).digest()
    sign = []
    pozycja = 0
    for byte in M:
        for bit in range(8):
            if (byte >> (7 - bit)) & 1:
                sign.append(private_keys[pozycja][1])
            else:
                sign.append(private_keys[pozycja][0])
            pozycja += 1
    return sign

def weryfikacja_podpisu(messege, sign, public_keys):
    M = hashlib.sha256(messege.encode()).digest()
    pozycja = 0
    for byte in M:
        for bit in range(8):
            if (byte >> (7 - bit)) & 1:
                if int.from_bytes(hashlib.sha256(sign[pozycja].to_bytes(32, 'big')).digest(), 'big') == public_keys[pozycja][1]:
                    pozycja += 1
                else:
                    return False
            else:
                if int.from_bytes(hashlib.sha256(sign[pozycja].to_bytes(32, 'big')).digest(), 'big') == public_keys[pozycja][0]:
                    pozycja += 1
                else:
                    return False
    return True

# Testowanie
klucz_prywatny, klucz_publiczny = generowanie_kluczy()
message = "Kot wlazł na płot i spadł na 4 łąpy"
podpis = generowanie_podpisu(message, klucz_prywatny)
wynik_weryfikacji = weryfikacja_podpisu(message, podpis, klucz_publiczny)
print(wynik_weryfikacji)
