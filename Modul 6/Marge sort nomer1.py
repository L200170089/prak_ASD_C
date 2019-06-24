class MhsTIF(object):
    def __init__(self, nama, no, kota, us):
        self.nama = nama
        self.no = no
        self.kota = kota
        self.uangSaku = us

c0 = MhsTIF("Ika", 10, "Sukoharjo", 240000)
c1 = MhsTIF("Budi", 51, "Sragen", 230000)
c2 = MhsTIF("Ahmad", 2, "Surakarta", 250000)
c3 = MhsTIF("Chandra", 18, "Surakarta", 235000)
c4 = MhsTIF("Eka", 4, "Boyolali", 240000)
c5 = MhsTIF("Fandi", 31, "Salatiga", 250000)
c6 = MhsTIF("Deni", 13, "Klaten", 245000)
c7 = MhsTIF("Galuh", 5, "Wonogiri", 245000)
c8 = MhsTIF("Janto", 23, "Klaten", 245000)
c9 = MhsTIF("Hasan", 64, "Karanganyar", 270000)
c10 = MhsTIF("Khalid", 29, "Purwodadi", 265000)

daftar = [c0.no, c1.no, c2.no, c3.no, c4.no, c5.no, c6.no, c7.no, c8.no, c9.no, c10.no]

def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i = 0 ; j = 0 ; k = 0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:
                A[k] = separuhKiri[i]
                i += 1
            else:
                A[k] = separuhKanan[j]
                j += 1
            k += 1

        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i += 1
            k += 1

        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            j += 1
            k += 1

        return A

print(daftar)
mergeSort(daftar)
print(daftar)