#2-misol
class Hayvon:
    def __init__(self, nomi):
        self.nomi = nomi

    def ovoz(self):
        print("Ovoz chiqardi", end=" ")

class Mushuk(Hayvon):
    def ovoz(self):
        super().ovoz()
        print("Miyov.")

h1 = Hayvon("mimi")
h1.ovoz()

print()

m1 = Mushuk("hihi")
m1.ovoz()
