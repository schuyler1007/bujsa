import sys
from collections import deque

type_flow = int
type_cost = int
INF = float('inf')

class Edge:
    def __init__(self, rev, from_, to, cap, cost):
        self.rev = rev
        self.from_ = from_
        self.to = to
        self.cap = cap
        self.initial_cap = cap
        self.cost = cost

class Graph:
    def __init__(self, n=0):
        self.V = n
        self.list = [[] for _ in range(n)]
    
    def init(self, n=0):
        self.V = n
        self.list = [[] for _ in range(n)]
    
    def resize(self, n=0):
        self.V = n
    
    def reset(self):
        for i in range(self.V):
            for e in self.list[i]:
                e.cap = e.initial_cap
    
    def redge(self, e):
        if e.from_ != e.to:
            return self.list[e.to][e.rev]
        else:
            return self.list[e.to][e.rev + 1]
    
    def addedge(self, from_, to, cap, cost):
        self.list[from_].append(Edge(len(self.list[to]), from_, to, cap, cost))
        self.list[to].append(Edge(len(self.list[from_]) - 1, to, from_, 0, -cost))

def min_cost_flow(G, s, t, inif):
    V = G.V
    dist = [INF] * V
    prevv = [-1] * V
    preve = [-1] * V
    
    res = 0
    f = inif
    
    while f > 0:
        dist = [INF] * V
        dist[s] = 0
        update = True
        
        while update:
            update = False
            for v in range(V):
                if dist[v] == INF:
                    continue
                for i, e in enumerate(G.list[v]):
                    if e.cap > 0 and dist[e.to] > dist[v] + e.cost:
                        dist[e.to] = dist[v] + e.cost
                        prevv[e.to] = v
                        preve[e.to] = i
                        update = True

        if dist[t] == INF:
            return 0
        
        d = f
        v = t
        while v != s:
            d = min(d, G.list[prevv[v]][preve[v]].cap)
            v = prevv[v]
        
        f -= d
        res += dist[t] * d
        
        v = t
        while v != s:
            e = G.list[prevv[v]][preve[v]]
            re = G.redge(e)
            e.cap -= d
            re.cap += d
            v = prevv[v]
    
    return res

if __name__ == "__main__":
    little = ["kate", "takahito", "ella", "sarah", "parker", "nana", "kyla", "mahoko", "chasen", "kamahiwa", "madoka", "simon", "josh", "michelle", "daisy", "gabby", "joeun", "jenny", "sam"]
    big = ["sam", "noelle", "niki", "miori", "afiq", "hugo", "elena", "anna", "tomoki", "theo", "alexander"]
    num_matches = [2, 10, 1, 1, 10, 10, 2, 2, 1, 1, 2]
    
    num_big = len(big)
    num_little = len(little)
    
    G = Graph(num_big + num_little + 2)
    
    S_node = num_big + num_little
    T_node = num_big + num_little + 1
    
    gains = [0, 0, 12, 0, 0, 0, 0, 0, 35, 30, 0, 4, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 18, 0, 0, 6, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 49, 0, 24, 0, 0, 0, 0, 0, 35, 0, 0, 0, 0, 0, 0, 0, 0, 35, 0, 0, 36, 12, 0, 0, 18, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 0, 0, 12, 0, 0, 12, 21, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 49, 42, 0, 28, 21, 35, 0, 16, 0, 30, 14, 0, 49, 0, 12, 2, 0, 0, 36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 0, 0, 0, 0, 21, 12, 0, 30, 0, 0, 0, 0, 0, 0, 0, 28, 5, 3, 0, 0, 49, 0, 0, 0, 0, 24, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 8, 6, 0, 0, 49, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Replace with the actual gain values in a list of lists
    
    loop_count = 0
    for i in range(num_big):
        for j in range(num_little):
            gain = gains[loop_count]
            loop_count += 1
            if gain != 0:
                gain = (49 - gain) * 2
                G.addedge(i, j + num_big, 1, gain)
    
    print(f"Total loop iterations: {loop_count}")
    
    for i in range(num_big):
        G.addedge(S_node, i, num_matches[i], 0)
    
    for j in range(num_little):
        G.addedge(j + num_big, T_node, 1, 0)
    
    res = min_cost_flow(G, S_node, T_node, num_little)
    
    print(f"Min Gain: {res}")
    
    with open("big_little_matches_s25-PYTHON.csv", "w") as outfile:
        outfile.write("Big,Little\n")
        for i in range(num_big):
            for e in G.list[i]:
                if e.initial_cap == 1 and e.cap == 0:
                    print(f"{big[i]} and {little[e.to - num_big]} are matched")
                    outfile.write(f"{big[i]},{little[e.to - num_big]}\n")
