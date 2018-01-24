import random


def generate_mine(n,m):
    camp = []
    for x in range(n):
        camp.append([])
    for x in camp:
        for y in range(m):
            rand = random.randint(3)
            if rand == 1:
                x.append("*")
            else:
                x.append(".")
    return camp

def scan_camp(camp):
    for x in range(len(camp)):
        
a = raw_input()
camp = []
while a != "0 0":
     l = list(map(int,a.split()))
     for x in range(l[0]):
         columns = raw_input()
         camp.append(columns)




