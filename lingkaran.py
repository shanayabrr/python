#program : menghitung luas segitiga
#deklarasi variable
#author : Thoriqurrahman Akrami

#const
phi = 3.14
#variable jari-jari r
r = float(input("masukan jari-jari \t:")) #float (hasil bilangan rill/desimal)

#keliling
keliling = 2 * phi * r
luas = phi * r * r

#hasil
print("keliling lingkaran\t:", '{:0,.2f}'.format(keliling))
print('luas lingkaran\t\t:', luas)