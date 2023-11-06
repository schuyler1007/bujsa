import csv

"""Big Class: Object representing bigs, with their name, list of littles (strings) they 
want to take in order of rank, and the maximum they want to take 
"""
class Big:
    def __init__(self, name, littles, max_num):
        # name: string
        self.name = name
        # littles: list of string of little's name they want
        self.littles = littles
        # max_num: max number of littles they can take
        self.max_num = max_num
        # result: list of string of little's name assigned
        self.result = []
"""Little Class: Object representing littles, with their name, and list of bigs (strings) they
want to take in order of rank
"""
class Little:
    def __init__(self, name, bigs):
        # name: string
        self.name = name
        # bigs: list of string of big's name they want
        self.bigs = bigs
        # result: string of big's name assigned
        self.result = ''

"""extract_data(filename,lorb): Function that takes data from either littles.csv or bigs.csv and
converts them into a list of little or big objects
"""
def extract_data(filename, lorb):
    # member_obj: objects of big or little
    member_obj = []
    # using the given file
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        # if the input is the littles file, append littles objects to file
        if lorb == 'l':
            for row in reader:
                member_obj.append(Little(row[1], row[3:]))
        # if the input is the bigs file, append bigs objects to file 
        if lorb == 'b':
            for row in reader:
                member_obj.append(Big(row[2], row[5:], row[4]))
    return member_obj


# Extract data for littles
littles = extract_data('../misc/littles1AMNoDupe.csv', 'l')[1:]
littlesAmt = len(littles)
# Reformat names of all little objects to be lowercase first name
for i in littles:
    i.name = i.name.split(" ")[0].lower()

# Prints out the names of all littles with proper formatting for big_little_matching.cpp
print("{", end="")
for i in littles[:littlesAmt-1]:
    print("\""+i.name+"\"", end=",")
print("\""+littles[littlesAmt-1].name+"\"}")


# Extract data for bigs
bigs = extract_data('../misc/bigs3.csv','b')[1:]
bigsAmt = len(bigs)
# Reformat names of all big objects to be lowercase first name 
for i in bigs:
    i.name = i.name.split(" ")[0].lower()

# Prints out the names of all bigs with proper formatting for big_little_matching.cpp
print("\n{", end="")
for i in bigs[:bigsAmt-1]:
    print("\""+i.name+"\"", end=",")
print("\""+bigs[bigsAmt-1].name+"\"}")


print("\n{", end="")
for i in bigs[:bigsAmt-1]:
    print(i.max_num, end=",")
print(bigs[bigsAmt-1].max_num+"}")


for i in bigs:
    newLittlesList = []
    for j in i.littles:
        newLittlesList.append(j.split(" ")[0].lower())
    i.littles = newLittlesList

for i in littles:
    newBigsList = []
    for j in i.bigs:
        newBigsList.append(j.split(" ")[0].lower())
    i.bigs = newBigsList


for i in bigs:
    for j in littles:
        if (j.name in i.littles and i.name in j.bigs):
            bigsRank = (i.littles.index(j.name)) 
            littlesRank = (j.bigs.index(i.name))
            bigsRank = (7 - bigsRank)
            littlesRank = (7 - littlesRank)
            print(bigsRank*littlesRank)
        else:
            print("0")

print("Littles:",littlesAmt)
print("Bigs:",bigsAmt)
