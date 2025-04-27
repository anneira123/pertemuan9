from collections import namedtuple
Koordinat = namedtuple ( 'Koordinat', ['x', 'y'])

koordinat1 = Koordinat ('10', '22')
koordinat2 = Koordinat ('30', '14')

print("x :", getattr(koordinat1, 'x') )
print("y:", getattr(koordinat1, 'y') )

print("x :", getattr(koordinat2, 'x') )
print("y:", getattr(koordinat2, 'y') )

print (type(koordinat1))
print (type(koordinat2))