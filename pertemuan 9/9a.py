class Binatang :
    PENGGOLONGAN = ('besar', 'kecil')
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis 
    def binatang1 (self):
        return "%s %s" % (self.nama, self.jenis)
    
    @property
    def binatang2 (self):
        return "%s %s" % (self.nama, self.jenis)
    @classmethod
    def penggolongan_pada_binatang_dimulai_dengan (cls, strartwith):
        return [t for t in cls.PENGGOLONGAN if t.startwith(strartwith)]
    @staticmethod
    def penggolongan_pada_binatang_diakhiri_dengan (endswith):
        return [t for t in Binatang.PENGGOLONGAN if t.endswith(endswith)]
    
miko = Binatang("miko","kucing")

print(miko.binatang1())
print(miko.binatang2)

