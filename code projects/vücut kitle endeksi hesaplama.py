print("Vücut kitle indeksi hesaplama aracına hoş geldiniz.")

weight = float(input("Kilonuzu giriniz: "))
height = float(input("Boyunuzu giriniz (Metre cinsinden): "))

vki = weight / height**2


print("Vücut kitle indeksiniz: ", vki)
if vki < 18.5:
    print("zayıfsınız")
elif vki >= 18.5 and vki < 24.9:
    print("Normal kilodasınız")
elif vki >= 24.9 and vki < 29.9:
    print("kilolusunuz")
elif vki >= 30 and vki < 39.9:
    print("obezsiniz")
elif vki > 40:
    print("aşırı obezsiniz")


