import time
a=1
toplam=0
sayi=input("Sayi Giriniz.... :")

while int(sayi)!=-1:
    toplam += int(sayi)
    sayi = input("Sayi Giriniz.... :")

print("Girdiğiniz sayıların toplamı="+str(toplam))