"""Nama : Xenyx Shariikhudhdhuchaa
   NIM  : L200170089
   Kelas: C"""


#no 1c
    def hitungVokal(self):
        vocal = 0
        z = self.teks
        huruf = "aiueoAIUEO"
        for i in z:
            if i in huruf:
                vocal += 1
        return vocal
    