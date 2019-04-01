"""Nama : Xenyx Shariikhudhdhuchaa
   NIM  : L200170089
   Kelas: C"""

#no 6
class SiswaSMA(Manusia):
    """Class Siswa merupakan turunan dari class Manusia"""
    def __init__(self, nama, NISN, jur, alamat):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.nisn = NISN
        self.jurusan = jur
        self.alamat = alamat
    def __str__(self):
        a = 'Nama       : ' + str(self.nama) \
            +'NISN      : ' + str(self.nisn) \
            +'Alamat    : ' + str(self.alamat) \
            +'Jurusan   : ' + str(self.jurusan)
        print (a)
    
    def ambilNama(self):
        print (self.nama)
    def ambilNisn(self):
        print (self.nisn)
    def ambilJurusan(self):
        print (self.jurusan)
    def ambilAlamat(self):
        print (self.alamat)
        