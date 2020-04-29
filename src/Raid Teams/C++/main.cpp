#include <bits/stdc++.h>
using namespace std;

bool compare_first(tuple<string,int,int,int> *&lhs, tuple<string,int,int,int> *&rhs) { 
    if (get<1>(*lhs) == get<1>(*rhs)) return get<0>(*lhs) > get<0>(*rhs);
    return get<1>(*lhs) < get<1>(*rhs);
}
bool compare_second(tuple<string,int,int,int> *&lhs, tuple<string,int,int,int> *&rhs) { 
    if (get<2>(*lhs) == get<2>(*rhs)) return get<0>(*lhs) > get<0>(*rhs);
    return get<2>(*lhs) < get<2>(*rhs);
}
bool compare_third(tuple<string,int,int,int> *&lhs, tuple<string,int,int,int> *&rhs) { 
    if (get<3>(*lhs) == get<3>(*rhs)) return get<0>(*lhs) > get<0>(*rhs);
    return get<3>(*lhs) < get<3>(*rhs);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    unordered_set<string> selected;
    vector<tuple<string,int,int,int>*> by_first;
    vector<tuple<string,int,int,int>*> by_second;
    vector<tuple<string,int,int,int>*> by_third;

    int n;
    cin >> n;
    
    tuple<string,int,int,int> mem[n];
    for (int i = 0; i < n; i++) {
        cin >> get<0>(mem[i]) >> get<1>(mem[i]) >> get<2>(mem[i]) >> get<3>(mem[i]);
        by_first.push_back(&mem[i]);
        by_second.push_back(&mem[i]);
        by_third.push_back(&mem[i]);
    }

    sort(by_first.begin(), by_first.end(), compare_first);
    sort(by_second.begin(), by_second.end(), compare_second);
    sort(by_third.begin(), by_third.end(), compare_third);

    while (1) {
        vector<string> team;

        while (!by_first.empty()) {
            tuple<string,int,int,int> player = *by_first.back();
            by_first.pop_back();
            if (selected.find(get<0>(player)) != selected.end()) continue;
            selected.insert(get<0>(player));
            team.push_back(get<0>(player));
            break;
        }
        if (team.size() == 0) break;

        bool second_found = false;
        string second;
        while (!by_second.empty()) {
            tuple<string,int,int,int> player = *by_second.back();
            by_second.pop_back();
            if (selected.find(get<0>(player)) != selected.end()) continue;
            selected.insert(get<0>(player));
            team.push_back(get<0>(player));
            break;
        }
        if (team.size() == 1) break;        

        bool third_found = false;
        string third;
        while (!by_third.empty()) {
            tuple<string,int,int,int> player = *by_third.back();
            by_third.pop_back();
            if (selected.find(get<0>(player)) != selected.end()) continue;
            selected.insert(get<0>(player));
            team.push_back(get<0>(player));
            break;
        }
        if (team.size() == 2) break;

        sort(team.begin(), team.end());

        cout << team[0] << ' ' << team[1] << ' ' << team[2] << '\n';
    }

    return 0;
}