print (" Praktikum Modul 5","\n",
       "Nama     :Xenyx S","\n",
"NIM/Kelas:L200170089/C","\n","\n")

#no2
pertama = [1,4,6,7,10,12]
kedua = [2,3,5,8,11]

def gabung(A,B):
    la = len(A)
    lb = len(B)
    c = list()
    i = 0
    j = 0
    while i < la and j < lb:
        if A[i] < B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            j += 1
    while i < la:
        c.append(A[i])
        i += 1
    while j > lb:
        c.append(B[j])
        j += 1
    return c

print("list pertama",pertama)
print("list kedua",kedua)
print("\nkedua list digabung menjadi ...\n")

print(gabung(pertama, kedua))

#no3
def swap(A,p,q):
    temp = A[p]
    A[p] = A[q]
    A[q] = temp
    
def cariposisiterkecil(A, darisini, sampaisini):
    posisiterkecil = darisini
    for i in range(darisini+1, sampaisini):
        if A[1] < A[posisiterkecil]:
            posisiterkecil = 1
    return posisiterkecil

def bubblesort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
                
def selectionsort(A):
    n = len(A)
    for i in range (n-1):
        indexkecil = cariposisiterkecil(A,i,n)
        if indexkecil != i:
            swap(A,i,indexkecil)

def insertionsort(A):
    n = len(A)
    for i in range (1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubblesort(u_bub);ak=detak();print('Buble      : %g detik' %(ak-aw));
aw = detak();selectionsort(u_sel);ak=detak();print('Selection  : %g detik' %(ak-aw));
aw = detak();insertionsort(u_ins);ak=detak();print('Insertion  : %g detik' %(ak-aw));

