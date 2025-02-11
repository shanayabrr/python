import numpy as npy
a = npy.array([[532,310,630], [150,230,600],[700,230,630]])
b = npy.array([[502,300,380], [100,130,400],[600,130,230]])
print("element Array : \n",a)
print("\n")
print("element array : \n",b)
print("="*40)

def kalkulasi():
    print("pengurangan 2 array(A-B) \n",(a-b))
    print("\n")
    print("pengurangan 2 array(A+B) \n",(a+b))
    print("\n")
    print("pengurangan 2 array(AxB) \n",(a*b))
    print("\n")
    print("pengurangan 2 array(A/B) \n",(a/b))
    print("-"*40)

def tranpose():
    print("hasil transpose Array A \n", npy.transpose(a))
    print("/n")
    print("hasil transpose Array A \n", npy.transpose(a))
    print("-"*40)

def sorting():
    print('Array Awal A')
    print(a)
    print("\n")
    print('setelah diturunkan berdasarkan kolom')
    a.sort(axis=0)
    print(a)
    print("\n")
    print('setelah diurutkan berdasarkan baris')
    a.sort(axis=1)
    print(a)
    print('-'*40)
kalkulasi()
tranpose()
sorting()

import statistics as sss
def statistik():
    x=npy.concatenate([a,b])
    y=x.ravel()
    z=x.flatten()
    print("hasil penggabungan array A dan B : \n", x)
    print("nilai rata rata dari array gabungan : ", npy.mean(x))
    print("nilai tengah dari array gabungan : ", npy.median(x))
    print("nilai yang paling banyak muncul dari array gabungan : ", sss.mode(y))
    print("nilai variance dari sample (pvarians) : ", sss.pvariance(y))
    print("nilai variance dari seluruh populasi (varians) : ", sss.variance(y))
    print("-"*40)
    print("\n")
    print("elemen array a: \n", a)
    print("menambahkan elemen pada array A dengan perintah append ==>", npy.append(a,[100]))
    print("menambahkan elemen pada array A dengan perintah insert ==>", npy.insert(a,2,[200]))
    
statistik()
import numpy as namp
m = int(input('masukan jumlah baris :'))
n = int(input('masukan jumlah kolom :'))

data =[[]for k in range (0,n)]
for i in range (0,m):
    for j in range (0,n):
        print('masukan elemen array [',i,',',j,']: ',end= '')
        x = int (input())
        data[i].append(x)
print("\n elemen array yang di masukan : ")
print(namp.array(data))
