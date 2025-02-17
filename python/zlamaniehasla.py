import hashlib
skrot = "d47d08f5d4ea8bde0bfd4e96fff25d5b6c55539d"
odpowiedz = ""

sprawdzane = 500000000
znaleziono = 0
while znaleziono == 0:
    tymskrot = hashlib.sha1(str(sprawdzane).encode()).hexdigest()
    if tymskrot == skrot:
        znaleziono = 1
        odpowiedz = sprawdzane
    sprawdzane += 1
print(odpowiedz)