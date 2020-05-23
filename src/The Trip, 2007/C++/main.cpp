#include <stdio.h>
#include <unordered_map>
#include <unordered_set>

typedef std::unordered_map<int,int> dict;
typedef std::unordered_set<int> set;
typedef dict::iterator dit;
typedef set::iterator sit;

void place_bags(dict& bags, int n) {
    set remove;
    while (n) {
        bool first = true;
        for (dit it = bags.begin(); it != bags.end(); ++it) {
            if (first) first = false;
            else putchar(' ');

            if (it->second > 0) {
                printf("%d", it->first);
                it->second--;
                n--;
            }

            if (it->second == 0) remove.insert(it->first);
        }
        putchar('\n');
        for (sit it = remove.begin(); it != remove.end(); ++it) bags.erase(*it);
        remove.clear();
    }
}

void test_case(int n) {
    dict bags;
    int k = 0, b;
    for (int i = 0; i < n; i++) {
        scanf("%d", &b);
        bags[b] = bags.find(b) == bags.end() ? 1 : bags[b] + 1;
        k = std::max(k, bags[b]);
    }
    printf("%d\n", k);
    place_bags(bags, n);
}

int main() {
    int n;
    for (int i = 0; ; i++) { 
        scanf("%d", &n);
        if (!n) break;
        if (i) putchar('\n');
        test_case(n);
    }
    return 0;
}