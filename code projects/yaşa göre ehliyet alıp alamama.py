print("Ehliyet uygunluğu programına holgeldiniz.")





yaş = int(input("Yaşınızı giriniz: "))
kimlik_kart = input("kimlik kartınız var mı?(E/H): ").upper()
biyometrik = input("Biyometrik fotoğrafınız var mı?(E/H): ").upper()
sicilkayıt = input("Adli sicil kaydınız var mı?(E/H): ").upper()
öğrencibelge = input("öğrenim belgeniz var mı?(E/H): ").upper()

if yaş > 18 and kimlik_kart == "E" and biyometrik == "E" and sicilkayıt == "E" and öğrencibelge == "E":
    print("Ehliyet almaya uygunsunuz.")
else:
    print("Ehliyet almaya uygun değilsiniz.")
    
