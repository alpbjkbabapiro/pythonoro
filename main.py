import random
karekterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sayi = int (input ("parolaniz nekadar uzun olsun"))

parola  = ""

for i in range (sayi):
    parola += random.choice(karekterler)
print(parola)