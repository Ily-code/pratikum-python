from os import umask


umur = int (input("Masukkan umur anda: "))

if umur in range (0,5):
    print("Masa balita yang bahagia")
elif umur in range (6,12):
    print("Masih masa pertumbuhan")
elif umur in range (13,20):
    print("Kamu seorang remaja!")
elif umur in range (21,60):
    print("Saatnya menjadi dewasa")
else:
     print("Waktunya pensiun")

