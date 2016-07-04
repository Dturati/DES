from  Cifra import cifra
from Decifra import *
cadeia = '10100010'
chave = '0111111101'
print("Texto")
print(cadeia)
print("")
print("Chave")
print(chave)
print("")
res = cifra(cadeia,chave)
decifra(res,chave)