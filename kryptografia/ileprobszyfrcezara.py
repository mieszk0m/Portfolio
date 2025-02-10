alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_size = 26

plaintext = "Zorro fly zealotry zipper"

ciphertext = ""

key = 15 #przesunięcie permutacji czyli klucz szyfrowania 

print("Tekst jawny: ", plaintext)
for text in plaintext.lower().split():
    for char in text:
        ciphertext = ciphertext + alphabet[(alphabet.index(char) + key) % alphabet_size] 
print("Szyfrogram: ",  ciphertext, "(spacje usunięte)")
for i in range (1,26):
    decodedtext = ""
    for text in ciphertext:
        for char in text:
            decodedtext = decodedtext + alphabet[(alphabet.index(char)- i) % alphabet_size]
    print(i, "możliwość odkodowanego kodu ",  decodedtext,  "(spacje usunięte)")
#1 25, gdyż ilość możliwość przesunąć - 1 (szyfrogram)
#2 brute force to sprawdzenie wszystkich możliwych rozwiązań
#3 kodować każdą litere bez związku z kodowaniem innych liter.