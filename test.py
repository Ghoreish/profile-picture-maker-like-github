import random
def make():
    l=[]
    for i in range(9):
        l.append("")
        for i in range(5):
            l[-1]+= "⬜" if random.randint(0,1) == 1 else "⬛"

    for i in l:
        print(i+i[-2::-1])

make()