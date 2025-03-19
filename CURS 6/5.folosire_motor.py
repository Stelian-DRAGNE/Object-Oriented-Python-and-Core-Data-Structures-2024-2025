
from motor import Motor, MotorElectric, MotorBenzina


# masina1 = MotorBenzina("Qwerty", 70, 180, 5)
# print(masina1)

bmw = MotorBenzina("858", 320, 218, 13, 60, 7)
print(bmw)

bmw += 100
print(bmw)

bmw.refill()
print(bmw)

bmw += 100
print(bmw)

bmw += 100
print(bmw)