

from cmath import sin
from curses.ascii import isupper

def part2():
    dups =0
    with open("./input.txt") as f:
        for l in f:
            l = l.rstrip("\n")
            lelf,relf = l.split(",")
            lst,lend = lelf.split("-")
            rst,rend = relf.split("-")

            lsects = set(range(int(lst),int(lend)+1))
            rsects = set(range(int(rst),int(rend)+1))

            intersectipn = lsects.intersection(rsects)
            if len(intersectipn):
                dups+=1
    print(dups)
def part1():
    dups =0
    with open("./input.txt") as f:
        for l in f:
            l = l.rstrip("\n")
            lelf,relf = l.split(",")
            lst,lend = lelf.split("-")
            rst,rend = relf.split("-")

            lsects = set(range(int(lst),int(lend)+1))
            rsects = set(range(int(rst),int(rend)+1))

            if lsects.issubset(rsects) or rsects.issubset(lsects):
                dups+=1
    print(dups)
part2()
