firstnum = int(input("İlk sayıyı giriniz: "))
secondnum = int(input("İkinci sayıyı giriniz: "))
thirdnum = int(input("Kaçar Kaçar artacağını seçiniz: "))

for x in range(firstnum, secondnum, thirdnum):
    if x % 2 != 0:
        print(x)