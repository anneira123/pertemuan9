from collections import namedtuple
Hewan = namedtuple ( 'hewan', ['nama', 'jenis'])

hewan1 = Hewan ('chimi', 'kucing')
hewan2 = Hewan ('miki', 'tikus')

print("nama :", getattr (hewan1, 'nama'))
print("nama:" , getattr (hewan2, 'jenis'))

print("nama :", getattr (hewan1, 'nama'))
print("nama:" , getattr (hewan2, 'jenis'))

print (type(hewan1))
print (type(hewan2))