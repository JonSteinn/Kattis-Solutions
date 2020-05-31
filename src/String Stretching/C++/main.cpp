// A rather horrible rewrite of my .py version to see how fast it was... 
// Probably can be optimized at some points... 

#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <set>
#include <vector>
#include <algorithm>
#include <string.h>
#include <math.h>

using namespace std;

char mem[100][201][201];
string str;
int char_count = 0;
string sstr;
int sstrl;
vector<int> ordered_lengths;
unordered_set<string> known;
unordered_set<string> invalid;
vector<char> left_order, right_order;
unordered_map<int, unordered_map<char,int>> ratios;


int gcd(unordered_map<char,int>& ratios) {
    int g = -1;
    for (auto it = ratios.begin(); it != ratios.end(); ++it) {
        g = g < 0 ? it->second : __gcd(g, it->second);
    }
    return g;
}

void fill_counter(unordered_map<char,int>& cnt) {
    for (auto it = str.begin(); it != str.end(); ++it) {
        if (cnt.find(*it) == cnt.end()) {
            cnt[*it] = 1;
            char_count++;

        } else  {
            cnt[*it]++;
        }
    }
}

void set_ratios() {
    unordered_map<char, int> counter;
    fill_counter(counter);
    int d = gcd(counter);

    int in_ind = str.size()/d;
    ordered_lengths.push_back(in_ind);
    ratios[in_ind] = unordered_map<char, int>();
    for (auto it = counter.begin(); it != counter.end(); ++it) {
        ratios[in_ind][it->first] = it->second / d;
    }

    int top = sqrt(d);
    for (int i=2; i <= top; i++) {
        if (d%i == 0) {
            int j = d/i;
            if (j!=i) {
                int j_ind = str.size()/j;
                ratios[j_ind] = unordered_map<char, int>();
                for (auto it = counter.begin(); it != counter.end(); ++it) {
                    ratios[j_ind][it->first] = it->second / j;
                }
                ordered_lengths.push_back(j_ind);
            }
            int i_ind = str.size()/i;
            ratios[i_ind] = unordered_map<char, int>();
            for (auto it = counter.begin(); it != counter.end(); ++it) {
                ratios[i_ind][it->first] = it->second / i;
            }
            ordered_lengths.push_back(i_ind);
        }
    }

    sort(ordered_lengths.begin(),ordered_lengths.end());
}

void get_order(vector<char>& order, string& str, bool reverse=false) {
    unordered_set<char> used;
    int total = 0;
    if (reverse) {
        for (auto it = str.rbegin(); it != str.rend(); it++) {
            if (used.find(*it) == used.end()) {
                order.push_back(*it);
                used.insert(*it);
                total++;
                if (total == char_count) return;
            }
        }
        return;
    }
    for (auto it = str.begin(); it != str.end(); ++it) {
        if (used.find(*it) == used.end()) {
            order.push_back(*it);
            used.insert(*it);
            total++;
            if (total == char_count) return;
        }
    }
}

void fast_io() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
}

void init() {
    fast_io();
    cin >> str;
    set_ratios();
    get_order(left_order, str);
    get_order(right_order, str, true);
}

bool pruner_rec_helper(string& rem, string& substr, int k, int x) {
    vector<int> lis;
    lis.push_back(x);

    while (lis.size() < 5 && lis[lis.size()-1] != -1) {
        lis.push_back(rem.find(substr, lis[lis.size()-1] + 1));
    }
    if (lis[lis.size()-1] != -1) return true;
    lis.pop_back();

    vector<string> strings;
    for (auto z : lis) {
        strings.push_back(rem.substr(0,z) + rem.substr(z+k));
        if (strings[strings.size()-1].size() == 0) {
            known.insert(strings[strings.size()-1]);
            return true;
        }
    }

    vector<int> zs;
    bool all_neg = true;
    for (auto s : strings) {
        zs.push_back(s.find(substr));
        if (zs[zs.size()-1] != -1) all_neg = false;
    }

    if (all_neg) return false;

    for (int i = 0; i < zs.size(); i++) {
        if (pruner_rec_helper(strings[i], substr, k, zs[i])) return true;
    }

    return false;
}

bool pruner(string& substr, int n, int i) {
    string rem_string = str.substr(0,i) + str.substr(i+n);
    int x = rem_string.find(substr);
    if (x == string::npos) return false;
    return pruner_rec_helper(rem_string, substr, n, x);
}

bool is_valid(string& substr, int n, int i) {
    vector<char> lo, ro;
    get_order(lo,substr);
    get_order(ro,substr,true);

    if (lo.size() != left_order.size()) return false;
    for (int i = 0; i < lo.size(); i++) {
        if (lo[i] != left_order[i] || ro[i] != right_order[i]) return false;
    }

    unordered_map<char,int> cnt;
    for (auto it = substr.begin(); it != substr.end(); ++it) {
        if (cnt.find(*it) == cnt.end()) {
            cnt[*it] = 1;
        } else  {
            cnt[*it]++;
        }
    }

    unordered_map<char,int> str_cnt = ratios[substr.size()];
    if (cnt.size() != str_cnt.size()) return false;
    for (auto it = cnt.begin(); it != cnt.end(); ++it) {
        if (it->second != str_cnt[it->first]) return false;
    }

    return pruner(substr, n, i);
}

void generate_valid_substrings_of_length(set<string>& container, int n) {
    for (int i = 0; i < str.size()-n+1; i++) {
        string substr = str.substr(i,n);
        if (container.find(substr) != container.end()) continue;
        if (invalid.find(substr) != invalid.end()) continue;

        if (is_valid(substr, n, i)) {
            container.insert(substr);
        }
    }
}

bool dp(int i, int l, int r) {
    if (i == sstrl) return l==r;
    
    if (mem[i][l][r] == 0) {
        if (sstr[i] != str[l] || sstr[sstrl-1] != str[r-1]) mem[i][l][r] = -1;
        else if (dp(i+1,l+1,r)) mem[i][l][r] = 1;
        else {
            mem[i][l][r] = -1; // should be fine as l is not decremented
            for (int offset = sstrl; offset < r-l-sstrl+i+1; offset += sstrl) {
                if (dp(0, l+1, l+1+offset) && dp(i+1, l+1+offset, r)) {
                    mem[i][l][r] = 1;
                    break;
                }
            }
        } 
    }
    return mem[i][l][r] == 1;
}

bool stretchable(const string& substring) {
    memset(mem, 0, sizeof(mem));
    sstr = substring;
    sstrl = sstr.size();
    return dp(0,0,str.size());
}

void de_stretch() {
    if (ratios.find(1) != ratios.end()) {
        cout << str[0] << '\n';
        return;
    }

    if (ratios.size() == 0) {
        cout << str << '\n';
        return;
    }

    for (auto it = ordered_lengths.begin(); it != ordered_lengths.end(); ++it) {
        set<string> possible;
        generate_valid_substrings_of_length(possible, *it);

        for (auto it = possible.begin(); it != possible.end(); ++it) {
            if (invalid.find(*it) != invalid.end()) continue;


            if (known.find(*it) != known.end() || stretchable(*it)) {
                cout << *it << '\n';
                return;
            } else {
                string repeat = *it;
                int top = str.size() / (*it).size();
                for (int i = 2; i < top; i++) {
                    repeat += *it;
                    if (ratios.find(i*(*it).size()) != ratios.end()) {
                        invalid.insert(repeat);
                    }
                }
            }
        }
    }

    cout << str << '\n';
}

int main() {
    init();
    de_stretch();
    return 0;
}