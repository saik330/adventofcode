
elves = []
def main():
    with open("./problem1.txt") as f:
        calcount = 0
        for l in f:
            if l == "\n":
                print ("HERE")
                elves.append(calcount)
                calcount = 0
            else:
                calcount+=int(l)


main()
selves = sorted(elves,reverse=True)
print(selves[0]+selves[1]+selves[2])