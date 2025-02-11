import numpy as nampy

n= int(input('masukan jumlah baris :'))
m= int(input('masukan jumlah kolom :'))
  
data =[[] for k in range (0,n)]
for i in range (0,m):
   for j in range (0,n):
       print ('masukan elemen array [',i,',',j,']: ',end='')
       x =int (input())
       data[i].append(x)
print("\nelemen array yang dimasukan : ")
print(nampy.array(data))