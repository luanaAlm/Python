from random import randint
from time import sleep

md2 = randint(1,30)
def gentree():
    print('\033c')
    for x in range(1,23):
        md1 = randint(1,md2)
        if x == 1:
            ch = "$"
        elif md1 % 4 == 0:
            ch = "o"
        elif md1 % 3 == 0:
            ch = "i"
        else:
            ch = "*"
        print("{:^33} ".format(ch*x))
    sleep(.75)
while True:
    gentree()

