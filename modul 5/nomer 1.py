print (" Praktikum Modul 5","\n",
       "Nama     :Xenyx S","\n",
"NIM/Kelas:L200170089/C","\n","\n")

#nomer 1
class MhsTIF(object):
    def __init__(self, nama, nim, asal, us):
        self.nama = nama
        self.nim = nim
        self.asal = asal
        self.uangsaku = us

    def __str__(self):
        s = self.nama + 'NIM' + str(self.nim)\
            + ' Tinggal di ' + self.asal \
            + ' Uang Saku Rp ' + str(self.uangsaku)\
            + ' tiap harinya.'

def swap(A,p,q):
    temp = A[p]
    A[p] = A[q]
    A[q] = temp
  
daftar = [(MhsTIF('retno','L200171552','sragen',10000)),
          (MhsTIF('murti','L200179999','merauke',2000)),
          (MhsTIF('schiffer','L200160005','sukoharjo',15000)),
          (MhsTIF('riki','L200170065','sragen',22000)),
          (MhsTIF('lina','L200170071','weru',23000)),
          (MhsTIF('maiden','L200170063','klaten',25000)),
          (MhsTIF('sven','L200170042','indramayu',25000)),
          (MhsTIF('silencer','L200170039','brebes',19000)),
          (MhsTIF('chronos','L200170047','bojonegoro',18000)),
          (MhsTIF('hidan','L200170079','bogor',21000))]

def ceknim(object):
    for i in object:
        print(i.nim)

def nimurut(object):
    n = len(object)
    for i in range(n-1):
        for j in range(n-i-1):
            if object[j].nim > object[j+1].nim:
                swap(object,j,j+1)
