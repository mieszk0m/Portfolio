import random
plaintext = "tobeornottobethatisthequestionwhethertisnoblerinthemindtosuffertheslingsandarrowsofoutrageousfortuneortotakearmsagainstaseaoftroublesandbyopposingendthem"
alphabet_a = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
klucz = []
x = len(alphabet)
for i in range (1,27):
    y  = random.randint(0, 26-i)
    klucz = klucz + [alphabet[y]]
    alphabet.remove(alphabet[y])
print(klucz)
decodedtext = ""
for i in range (0,len(plaintext)):
    for j in range (0,len(alphabet_a)):
        if plaintext[i] == alphabet_a [j]:
            decodedtext = decodedtext + klucz[j]
print(decodedtext)
rozwiązanie = ""
for i in range (0,len(decodedtext)):
    for j in range (0,len(alphabet_a)):
        if decodedtext[i] == klucz [j]:
            rozwiązanie = rozwiązanie + alphabet_a[j]
print(rozwiązanie)