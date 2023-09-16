#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)

typedef int FLOW;
typedef int COST;
const int MAX_V = 100;
const COST INF = INT_MAX/2;


struct Edge {
    int rev, from, to;
    FLOW cap, initial_cap;
    COST cost;
    Edge(int r, int f, int t, FLOW ca, COST co) : rev(r), from(f), to(t), cap(ca), initial_cap(ca), cost(co) {}
};


struct Graph{
    int V;
    vector<Edge> list[MAX_V];

    Graph(int n = 0) : V(n) {rep(i,MAX_V) list[i].clear(); }
    void init(int n = 0) {V = n; rep(i, MAX_V) list[i].clear();}
    void resize(int n = 0) {V = n;}
    void reset() { rep(i,V) rep(j,list[i].size()) list[i][j].cap = list[i][j].initial_cap; }
    inline vector<Edge>& operator[] (int i) {return list[i];}

    Edge &redge(Edge &e){
        if (e.from != e.to) return list[e.to][e.rev];
        else return list[e.to][e.rev + 1];
    }

    void addedge(int from, int to, FLOW cap, COST cost){
        list[from].push_back(Edge((int)list[to].size(), from, to, cap, cost));
        list[to].push_back(Edge((int)list[from].size() - 1, to, from, 0, -cost));
    }
};


COST MinCostFlow(Graph &G, int s, int t, FLOW inif) {
    COST dist[MAX_V];
    int prevv[MAX_V];
    int preve[MAX_V];

    COST res = 0;
    FLOW f = inif;
    while (f > 0) {
        fill(dist, dist + G.V, INF);
        dist[s] = 0;
        while (true) {
            bool update = false;
            for (int v = 0; v < G.V; ++v) {
                if (dist[v] == INF) continue;
                for (int i = 0; i < G[v].size(); ++i) {
                    Edge &e = G[v][i];
                    if (e.cap > 0 && dist[e.to] > dist[v] + e.cost) {
                        dist[e.to] = dist[v] + e.cost;
                        prevv[e.to] = v;
                        preve[e.to] = i;
                        update = true;
                    }
                }
            }
            if (!update) break;
        }

        if (dist[t] == INF) return 0;

        FLOW d = f;
        for (int v = t; v != s; v = prevv[v]) {
            d = min(d, G[prevv[v]][preve[v]].cap);
        }
        f -= d;
        res += dist[t] * d;
        for (int v = t; v != s; v = prevv[v]) {
            Edge &e = G[prevv[v]][preve[v]];
            Edge &re = G.redge(e);
            e.cap -= d;
            re.cap += d;
        }s
    }
    return res;
}


int main(){

    string big[] = {}; // bigs name comes here
    string little[] = {}; // littles name comes here
    int num_matches[] = {}; // how many littles each big wants comes here

    int num_big = 0, num_little = 0;
    cin >> num_big >> num_little;

    Graph G(num_big + num_little + 2);

    int S_node = num_big + num_little;
    int T_node = num_big + num_little + 1;

    for (int i=0; i<num_big; i++){
        for (int j=0; j<num_little; j++){
            int gain;
            cin >> gain;
            gain = 49 - gain;
            G.addedge(i, j+num_big, 1, gain);
        }
    }

    for (int i=0; i<num_big; i++){
        G.addedge(S_node, i, num_matches[i], 0);
    }

    for (int j=0; j<num_little; j++){
        G.addedge(j + num_big, T_node, 1, 0);
    }

    COST res = MinCostFlow(G,S_node, T_node, num_little);

    cout << "Min Gain: " << res << endl;

    for (int i=0; i<num_big; i++){
        for (auto e: G[i]){
            if (e.initial_cap == 1 && e.cap == 0){
                cout << big[i] << " and " << little[e.to - num_big] << " are matched" << endl;
            }
        }
    }

    return 0;
}