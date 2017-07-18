#include <cstdio>
#include <cstring>
#include <vector>

struct stack
{
    int* mem;
    int* curr;

    stack(int max_cap) {
        mem = new int[max_cap];
    }

    ~stack() {
        delete[] mem;
    }

    bool is_empty() {
        return mem == curr;
    }

    void push(int x) {
        *(curr++) = x;
    }

    int pop() {
        return *(--curr);
    }

    void reset() {
        curr = mem;
    }
};

struct graph
{
    std::vector<int>* edges;

    graph(int v) {
        edges = new std::vector<int>[v + 1];
    }

    void add_edge(int from, int to) {
        edges[from].push_back(to);
    }
};

int spread(graph& g, stack& open, bool* closed)
{
    int sum = 0;
    while(!open.is_empty()) {
        int current = open.pop();
        if (closed[current]) continue;
        closed[current] = true;
        sum++;
        for (std::vector<int>::iterator it = g.edges[current].begin(); it != g.edges[current].end(); ++it) {
            if (!closed[*it]) open.push(*it);
        }
    }
    return sum;
}

int main() {
    stack open(40000);
    bool visited[10001];
    int n;
    scanf("%d",&n);
    while(n--) {
        open.reset();
        memset(visited, 0, sizeof(bool) * 10001);
        int v, e, s;
        scanf("%d %d %d", &v, &e, &s);
        graph g(v);
        while(e--)
        {
            int a, b;
            scanf("%d %d", &a, &b);
            g.add_edge(a, b);
        }
        while(s--)
        {
            int a;
            scanf("%d", &a);
            open.push(a);
        }
        printf("%d\n", spread(g, open, visited));
    }
    return 0;
}