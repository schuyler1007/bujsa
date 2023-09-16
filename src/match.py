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



    

            
extract_data('../misc/little.csv', 'l')
