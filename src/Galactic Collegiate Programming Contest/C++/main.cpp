#include <stdio.h>
#include <vector>
#include <tuple>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

struct cmp {
    bool operator() (const tuple<int,int,int>& lhs, const tuple<int,int,int>& rhs) const {
        int x = get<0>(lhs), y = get<0>(rhs);
        if (x != y) return x > y;
        x = get<1>(lhs); y = get<1>(rhs);
        if (x != y) return x < y;
        return get<2>(lhs) < get<2>(rhs);
    }
};

typedef tree<tuple<int,int,int>, null_type, cmp, rb_tree_tag, tree_order_statistics_node_update> map_t;

int main() {
    int n, m, team, pen;
    scanf("%d %d", &n, &m);

    map_t t;
    vector<tuple<int,int,int>> keys(n);

    for (int i = 0; i < n; i++) {
        get<0>(keys[i]) = 0;
        get<1>(keys[i]) = 0;
        get<2>(keys[i]) = i+1;
        t.insert(keys[i]);
    }
    
    while(m--) {
        scanf("%d %d", &team, &pen);
        t.erase(keys[team-1]);
        get<0>(keys[team-1]) = get<0>(keys[team-1]) + 1;
        get<1>(keys[team-1]) = get<1>(keys[team-1]) + pen;
        t.insert(keys[team-1]);
        printf("%zu\n", 1 + t.order_of_key(keys[0]));
    }

    return 0;
}