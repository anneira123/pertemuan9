from collections import namedtuple
Orang = namedtuple("Orang", "nama anak")
john = Orang("John Doe", ["Timmy", "Jimmy"])

def tampilkan_info(self):
    print("Nama : ", self.nama)
    print("Nama anak : ")
    for i in range(len(self.anak)):
        print(f"{i+1}. {self.anak[i]}")

print(john)
print(id(john.anak))
john.anak.append("Tina")
print(john)
print(id(john.anak))