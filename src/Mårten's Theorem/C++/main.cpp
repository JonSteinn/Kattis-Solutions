#include <iostream>
#include <unordered_map>
#include <vector>

/* Tree structure... explanation format
std::vector<
        std::pair<
            int,
            std::vector<
                std::pair<
                    int,
                    std::vector<
                        int
                    >
                >
            >
        >
    > x(
        26, 
        std::make_pair(
            -1, 
            std::vector<std::pair<int,std::vector<int>>>(
                26, 
                std::make_pair(
                    -1, 
                    std::vector<int>(
                        26,
                        -1
                    )
                )
            )
        )
    );
*/

typedef std::unordered_map<std::string, int> Dictionary;
typedef std::vector<std::pair<int, int>> Queries;
typedef std::string String;
typedef std::vector<std::pair<int,std::vector<std::pair<int,std::vector<int>>>>> Tree;
#define TREE_INIT 26, std::make_pair(-1, std::vector<std::pair<int,std::vector<int>>>(26, std::make_pair(-1, std::vector<int>(26,-1))))

struct UnionFind {
    std::vector<int> p; 

    UnionFind(int n) : p(n, -1) { }

    int root(int x) {
        while (p[x] >= 0) {
            if (p[p[x]] >= 0) p[x] = p[p[x]];
            x = p[x];
        }
        return x;
    }

    bool connect(int x, int y) {
        int xp = root(x), yp = root(y);
        if (xp == yp) return false;
        if (p[xp] > p[yp]) std::swap(xp,yp);
        p[xp] += p[yp], p[yp] = xp;
        return true; 
    }

    bool are_connected(int x, int y) {
        return root(x) == root(y);
    }
};

bool validate(UnionFind& uf, Queries& queries) {
    for (std::pair<int,int> x : queries) {
        if (uf.are_connected(x.first, x.second)) return false;
    }
    return true;
}

void rhyme_eq_1(UnionFind& uf, Tree& tree, String& str, int i, int i1) {
    if (tree[i1].first == -1) {
        tree[i1].first = i;
        for (int i2 = 0; i2 < 26; i2++) {
            if (tree[i1].second[i2].first != -1) {
                uf.connect(i, tree[i1].second[i2].first);
            } else {
                for (int i3 = 0; i3 < 26; i3++) {
                    if (tree[i1].second[i2].second[i3] != -1) {
                        uf.connect(i, tree[i1].second[i2].second[i3]);
                    }
                }
            }
        }
    }
}

void rhyme_eq_2(UnionFind& uf, Tree& tree, String& str, int i, int i1, int i2) {
    if (tree[i1].first != -1) {
        uf.connect(i, tree[i1].first);
    } else if (tree[i1].second[i2].first == -1) {
        tree[i1].second[i2].first = i;
        for (int i3 = 0; i3 < 26; i3++) {
            if (tree[i1].second[i2].second[i3] != -1) {
                uf.connect(i, tree[i1].second[i2].second[i3]);
            }
        }
    }
}

void rhyme_eq_3(UnionFind& uf, Tree& tree, String& str, int i, int i1, int i2, int i3) {
    if (tree[i1].first != -1) {
        uf.connect(i, tree[i1].first);
    } else if (tree[i1].second[i2].first != -1) {
        uf.connect(i, tree[i1].second[i2].first);
    } else if (tree[i1].second[i2].second[i3] == -1) {
        tree[i1].second[i2].second[i3] = i;
    } else if (tree[i1].second[i2].second[i3] != i) {
        uf.connect(tree[i1].second[i2].second[i3],i);
    }
}

void add_rhyme_equivalence(UnionFind& uf, Tree& tree, String& str, int i) {
    switch (str.size()) {
        case 1:
            rhyme_eq_1(uf, tree, str, i, str[0]-'a');
            break;
        case 2:
            rhyme_eq_2(uf, tree, str, i, str[1]-'a', str[0]-'a');
            break;
        default:
            rhyme_eq_3(uf, tree, str, i, str[str.size()-1]-'a', str[str.size()-2]-'a', str[str.size()-3]-'a');
    }
}

int get_index_of(Dictionary& str2int, String& str, int& next_index) {
    int index;
    if (str2int.find(str) == str2int.end()) {
        index = next_index++;
        str2int[str] = index;
    } else {
        index = str2int[str];
    }
    return index;
}

void read(UnionFind& uf, Queries& queries, int n) {
    String a, b, op;
    int _a, _b, next_index = 0;
    Dictionary str2int;
    Tree tree(TREE_INIT);

    for (int i = 0; i < n; i++) {
        std::cin >> a >> op >> b;

        _a = get_index_of(str2int, a, next_index);
        _b = get_index_of(str2int, b, next_index);

        add_rhyme_equivalence(uf, tree, a, _a);
        add_rhyme_equivalence(uf, tree, b, _b);

        if (op[0] == 'n') queries.push_back(std::make_pair(_a, _b));
        else uf.connect(_a, _b);
    }
}

void fast_io() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
}

int main() {
    fast_io();
    int n;
    std::cin >> n;
    UnionFind uf(n<<1);
    Queries not_queries;
    read(uf, not_queries, n);
    std::cout << (validate(uf, not_queries) ? "yes\n" : "wait what?\n");
    return 0;
}