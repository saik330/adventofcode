

from cmath import sin
from curses.ascii import isupper

def part2():
    #Lowercase item types a through z have priorities 1 through 26.
    #Uppercase item types A through Z have priorities 27 through 52.
    LOWOFFSET  = -96
    HIGHOFFSET = -38
    i=0
    elfgroups={}
    elgn=0
    
    with open("./input.txt") as f:

        ls = f.readlines()

        sindex = 0
        while sindex < len(ls):
            l = ls[sindex].rstrip('\n')
            for c in l:
                if c in ls[sindex+1] and c in ls[sindex+2]:
                    elfgroups[elgn] =c

            sindex +=3
            elgn+=1
        sump=0
        for k in elfgroups:
            d =elfgroups[k]
            if isupper(d):
                sump += ord(d)+HIGHOFFSET
            else:
                sump += ord(d) + LOWOFFSET
    
    print(sump)
def part1():
    #Lowercase item types a through z have priorities 1 through 26.
    #Uppercase item types A through Z have priorities 27 through 52.
    LOWOFFSET  = -96
    HIGHOFFSET = -38
    duplicates= []
    with open("./input.txt") as f:
        for l in f:
            l = l.rstrip("\n")
            print(l)
            firsthalf  = l[:-int(len(l)/2)]
            secondhalf = l[int(len(l)/2):]
            i = 0
            hdup ={}
            while i < len(firsthalf):
                if firsthalf[i] in secondhalf:
                    print(firsthalf[i])
                    hdup[firsthalf[i]]=1
                i+=1
            for k in hdup.keys():
                duplicates.append(k)
    print(duplicates)
    sump = 0
    for d in duplicates:
        if isupper(d):
            #print(d)
            #print(ord(d)+HIGHOFFSET)
            sump += ord(d)+HIGHOFFSET
        else:
            #print(d)
            #print(ord(d)+LOWOFFSET)
            sump += ord(d) + LOWOFFSET
        
    print(sump)
part2()
