# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput
bruto = float(input("Tuliskan Angka Bruto: "))
tara = float(input("Tuliskan Angka Tara: "))

# Mengkonversi
netto = bruto - tara
persentara = tara / bruto * 100

# Menampilkan Hasil
print('=======================================')
print('Maka Netto = %d' %(netto))
print('Maka Persentase Tara %d Persen' %(persentara))
print('=======================================')
