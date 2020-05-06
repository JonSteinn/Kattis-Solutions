#include <iostream>
#include <stdlib.h>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <vector>

using namespace std;

struct Vertex {
    int v;
    int price;
    int prestige;

    Vertex(int _v, int _price, int _prestige) : v(_v), price(_price), prestige(_prestige) { }
};

struct VertexComparator { 
    bool operator()(Vertex const& v1, Vertex const& v2) { 
        if (v1.price < v2.price) return false;
        if (v2.price < v1.price) return true;
        return v1.prestige < v2.prestige;
    } 
}; 

void fast_io() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

void djikstra(
    int budget,
    int visited_size,
    unordered_set<int>& sources,
    vector<int>& weights,
    vector<int>& values,
    unordered_map<int, unordered_map<int, pair<int,int>>>& edges
) {
    priority_queue<Vertex, vector<Vertex>, VertexComparator> queue;
    for (unordered_set<int>::iterator it = sources.begin(); it != sources.end(); ++it) queue.push(Vertex(*it, 0, 0));
    vector<bool> visited(visited_size, false);
    while (!queue.empty()) {
        Vertex curr = queue.top();
        queue.pop();
        if (visited[curr.v] || curr.price > budget) continue;
        visited[curr.v] = true;

        if (sources.find(curr.v) == sources.end()) {
            weights.push_back(curr.price);
            values.push_back(curr.prestige);
        }

        for (unordered_map<int, pair<int,int>>::iterator it = edges[curr.v].begin(); it != edges[curr.v].end(); ++it) {
            if (!visited[it->first]) {
                queue.push(Vertex(it->first, curr.price + it->second.first, curr.prestige + it->second.second));
            }
        }
    }
}

int construct_graph(int n, unordered_map<int, unordered_map<int, pair<int,int>>>& edges, unordered_set<int>& sources) {
    string dish, base, ingredient;
    int price, prestige;

    int next_index = 0;
    unordered_map<string, int> item_to_index_mapper;
    
    while (n--) {
        cin >> dish >> base>> ingredient >> price >> prestige;

        int base_i = -1;
        if (item_to_index_mapper.find(base) == item_to_index_mapper.end()) {
            base_i = next_index++;
            item_to_index_mapper[base] = base_i;
            sources.insert(base_i);
        } else {
            base_i = item_to_index_mapper[base];
        }

        int dish_i = -1;
        if (item_to_index_mapper.find(dish) == item_to_index_mapper.end()) {
            dish_i = next_index++;
            item_to_index_mapper[dish] = dish_i;
        } else {
            dish_i = item_to_index_mapper[dish];
            if (sources.find(dish_i) != sources.end()) sources.erase(dish_i);
        }

        if (edges.find(base_i) != edges.end() && edges[base_i].find(dish_i) != edges[base_i].end()) {
            pair<int,int> existing = edges[base_i][dish_i];
            if (price < existing.first || (price == existing.first && prestige > existing.second)) {
                edges[base_i][dish_i] = {price, prestige};
            }
        } else {
            edges[base_i][dish_i] = {price, prestige};
        }

    }

    return next_index;
}

int map_to_weights_and_values(vector<int>& weights, vector<int>& values, int n, int b) {
    unordered_map<int, unordered_map<int, pair<int,int>>> edges;
    unordered_set<int> sources;
    int vertices = construct_graph(n, edges, sources);
    djikstra(b, vertices, sources, weights, values, edges);
    return weights.size();
}

void print_results(vector<int>& weights, vector<int>& values, int n, int b, int *mem) {
    int col_size = b+1;

    int best = (mem + n*col_size)[b];
    printf("%d\n", best);

    while (b > 0 and (mem + n*col_size)[b-1] == best) b--;

    int c = b; 
    for (int i = n; i > 0 && best > 0; i--) {
        if (best != (mem + (i-1)*col_size)[c]) {
            best -= values[i-1];
            c -= weights[i-1];
        }
    }

    printf("%d\n", b - c);
}

void knapsack(vector<int>& weights, vector<int>& values, int n, int b) {
    int mem[n+1][b+1];
    for (int i = 0; i <= n; i++) { 
        for (int c = 0; c <= b; c++) { 
            if (i == 0 || c == 0) mem[i][c] = 0; 
            else if (weights[i-1] <= c) mem[i][c] = max(values[i-1]+mem[i-1][c-weights[i-1]],mem[i-1][c]); 
            else mem[i][c] = mem[i-1][c]; 
        } 
    }

    print_results(weights, values, n, b, (int*)mem);
}

int main() {
    fast_io();

    int b, n;
    cin >> b >> n;

    vector<int> weights, values;
    n = map_to_weights_and_values(weights, values, n, b);
    knapsack(weights, values, n, b);

    return 0;
}