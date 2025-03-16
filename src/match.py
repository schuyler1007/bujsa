import csv

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

class Little:
    def __init__(self, name, bigs):
        # name: string
        self.name = name
        # bigs: list of string of big's name they want
        self.bigs = bigs
        # result: string of big's name assigned
        self.result = ''

def extract_data(filename, lorb):
    # member_obj: objects of big or little
    member_obj = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        if lorb == 'l':
            for row in reader:
                member_obj.append(Little(row[1], row[3:]))
        if lorb == 'b':
            for row in reader:
                member_obj.append(Big(row[1], row[4:], row[3]))
    return member_obj



# Extract data for littles
littles = extract_data('../data/Spring2025/littles.csv', 'l')[1:]
littlesAmt = len(littles)
# Reformat names of all little objects to be lowercase first name
for i in littles:
    i.name = i.name.split(" ")[0].lower()


    

            
extract_data('../misc/little.csv', 'l')

# Extract data for bigs
bigs = extract_data('../data/Spring2025/bigs.csv','b')[1:]
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
