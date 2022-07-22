from os import umask


umur = int (input("Masukkan umur anda: "))

if umur <= 12:
    print("Masa kecil yang bahagia")
elif umur in range (13,20):
    print("Kamu seorang remaja!")
else:
    print("Saatnya menjadi dewasa")

