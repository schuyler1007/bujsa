//
// Created by 河田佳楓 on 2022/02/12.
// Edited by Theo :D
//

#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; i++)
#define little_total 20
#define big_total 11

struct Big{
    int big_no;
    string name;
    int little_num;
    vector<int> little_pref;
};

struct Little{
    int little_no;
    string name;
    vector<int> big_pref;
};

int main(){
    int total_pref[big_total][little_total];
    vector<Big> bigs(big_total);
    rep(i,big_total){
        bigs[i].big_no = i;
        string in_name;
        int in_little_num;
        cin >> in_name >> in_little_num;
        bigs[i].name = in_name;
        bigs[i].little_num = in_little_num;
        rep(j,little_total){
            int in_pref;
            cin >> in_pref;
            bigs[i].little_pref.push_back(in_pref);
        }
    }
    vector<Little> lils(little_total);
    rep(i,little_total){
        lils[i].little_no = i;
        string in_name;
        cin >> in_name;
        lils[i].name = in_name;
        rep(j,big_total){
            int in_pref;
            cin >> in_pref;
            lils[i].big_pref.push_back(in_pref);
        }
    }

    rep(b,big_total){
        rep(l,little_total){
            total_pref[b][l] = bigs[b].little_pref[l] * lils[l].big_pref[b];
        }
    }



}

