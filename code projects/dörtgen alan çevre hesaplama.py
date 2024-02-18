print("Alan&Çevre hesaplayıcıya hoş geldiniz.")

sekil = input("Hesaplamak istediğiniz geometrik şekli yazınız: ").upper()
ac = input("Alan mı Çevre mi hesaplamak istediğinizi yazınız: ").upper()

if sekil == "ÜÇGEN" and ac == "ALAN":
    ucgentaban = float(input("üçgeninizin taban uzunluğunu yazınız: "))
    ucgenyukseklik = float(input("üçgeninizin yüksekliğini yazınız: "))
    
if sekil == "ÜÇGEN" and ac == "ÇEVRE":
    ucgenkenar1 = float(input("üçgeninizin ilk kenarının uzunluğunu yazınız: "))
    ucgenkenar2 = float(input("üçgeninizin ikinci kenarının uzunluğunu yazınız:"))
    ucgenkenar3 = float(input("üçgeninizin üçüncü kenarının uzunluğunu yazınız: "))

if sekil == "DAIRE" and ac == "ALAN" or sekil == "DAIRE" and ac == "ÇEVRE":
    pi = float(input("pi sayısını kaç alacağınızı seçiniz: "))
    daire_r = float(input("dairenizin yarıçapının uzunluğunu yazınız: "))
    
if sekil == "DÖRTGEN" and ac == "ALAN" or sekil == "DÖRTGEN" and "ÇEVRE":
    dörtgenkısa = float(input("dörtgeninizin kısa kenar uzunluğunu yazınız: "))
    dörtgenuzun = float(input("dörtgeninizin uzun kenar uzunluğunu yazınız: "))
    
    

    
    
