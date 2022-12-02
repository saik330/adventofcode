

#rock, paper, scissors
#a, b, c
#x, y ,z
def part1():
    HAND = {"X":1, "Y":2, "Z":3}
    SCORE = {"W":6,"D":3,"L":0}
    truthtable = {}
    truthtable["AZ"] = 0
    truthtable["AY"] = 6
    truthtable["AX"] = 3
    truthtable["BZ"] = 6
    truthtable["BY"] = 3
    truthtable["BX"] = 0
    truthtable["CZ"] = 3
    truthtable["CY"] = 0
    truthtable["CX"] = 6

    scorage = 0
    with open("./input.txt") as f:
        for l in f:
            l = l.rstrip("\n")
            print(l)
            th,yh = l.split()
            scorage+=HAND[yh]
            scorage+=truthtable[th+yh]
    print(scorage)
def part2():
    HAND = {"X":1, "Y":2, "Z":3}
    WLD ={"X":0, "Y":3, "Z":6}
    SCORE = {"W":6,"D":3,"L":0}
    truthtable = {}
    truthtable["AZ"] = 0
    truthtable["AY"] = 6
    truthtable["AX"] = 3
    truthtable["BZ"] = 6
    truthtable["BY"] = 3
    truthtable["BX"] = 0
    truthtable["CZ"] = 3
    truthtable["CY"] = 0
    truthtable["CX"] = 6

    scorage = 0
    with open("./input.txt") as f:
        for l in f:
            l = l.rstrip("\n")
            print(l)
            th,exres = l.split()
            scorage+=WLD[exres]
            #Because I can't be bothered to redo the table, easier to just search it
            for h in truthtable.keys():
                if truthtable[h] == WLD[exres]:
                    if h[0] == th:
                        print(h)
                        scorage+=HAND[h[1]]

    print(scorage)
part2()
