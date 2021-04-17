#Soal 1 Tugas 7

pembukaan = "Perhitungan pada Persegi"
a = pembukaan.center(50, "=")
print(a)

import math
sisi = float(input("Masukkan sisinya: "))


#Menghitung luas persegi dan pembulatan ke atas
luas = sisi*sisi
print("Luas persegi adalah", luas,  "cm persegi")
print("Hasil pembulatan ke atas luas persegi adalah", math.ceil(luas), "cm persegi")
print()

#Menghitung keliling persegi dan pembulatan ke bawah
keliling = sisi+sisi
print("Keliling persegi adalah", keliling, "cm")
print("Hasil pembulatan kebawah persegi adalah", math.floor(keliling), "cm")
print()

#Mengitung diagonal persegi
diagonal = 2*(sisi**2)
print("Panjang diagonal persegi adalah", math.sqrt(diagonal))