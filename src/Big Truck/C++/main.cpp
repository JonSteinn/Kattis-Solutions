#include <cstdio>
#include <vector>
#include <queue>


struct Pair {
    int vertex;
    int weight;

    Pair(int vertex, int weight) : vertex(vertex), weight(weight) {}
};

struct Triple {
    int vertex;
    int cost;
    int packages;

    Triple(int vertex, int cost, int packages) : vertex(vertex), cost(cost), packages(packages) {};

    bool operator<(const Triple& rhs) const {
        return this->cost == rhs.cost ? this->packages < rhs.packages : this->cost > rhs.cost;
    }
};

struct Graph {
    std::vector<Pair>* edges;
    int* packages;
    int V;
    int shortest;
    int package_sum;

    Graph() {
        scanf("%d",&V);
        edges = new std::vector<Pair>[V + 1];
        packages = new int[V + 1];
        this->V = V;
        this->shortest = 2147483647;
        this->package_sum = 0;
    }

    ~Graph() {
        delete[] edges;
        delete[] packages;
    }

    void read_packages() {
        for (int i = 1; i <= V; i++) scanf("%d", packages + i);
    }

    void read_edges() {
        int E;
        scanf("%d",&E);
        while(E--) {
            int a, b, d;
            scanf("%d %d %d", &a, &b, &d);
            edges[a].push_back(Pair(b, d));
            edges[b].push_back(Pair(a, d));
        }
    }

    bool possible() {
        return shortest != 2147483647;
    }

    void search() {
        std::priority_queue<Triple> pq;
        pq.push(Triple(1, 0, packages[1]));
        bool visited[V + 1]{0};

        while (!pq.empty()) {

            Triple current = pq.top();
            pq.pop();

            if (current.vertex == V) {
                shortest = current.cost;
                package_sum = current.packages;
                break;
            }

            if (visited[current.vertex]) continue;
            visited[current.vertex] = true;

            for (std::vector<Pair>::iterator it = edges[current.vertex].begin(); it != edges[current.vertex].end(); ++it) {
                if (!visited[it->vertex]) pq.push(Triple(it->vertex, current.cost + it->weight, current.packages + packages[it->vertex]));
            }
        }
    }

};


int main() {
    Graph G;
    G.read_packages();
    G.read_edges();
    G.search();
    if (G.possible()) printf("%d %d\n", G.shortest, G.package_sum);
    else printf("impossible\n");
    return 0;
}