#include <iostream>
#include <queue>
#include <stdlib.h>
#include <unordered_map>
#include <unordered_set>
#include <vector>

void fast_io() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);
}

struct Vertex {
  int v;
  int cost;

  Vertex(int _v, int _cost) : v(_v), cost(_cost) {}
};

struct VertexComparator {
  bool operator()(Vertex const &v1, Vertex const &v2) {
    return (v2.cost < v1.cost);
  }
};

int main() {
  fast_io();
  int n, m;
  std::cin >> n >> m;

  std::vector<std::vector<Vertex>> edges(n);
  for (int i = 0; i < n; i++)
    edges.push_back(std::vector<Vertex>());

  for (int i = 0; i < m; i++) {
    int src, dst, cost;
    std::cin >> src >> dst >> cost;
    dst--;
    src--;
    edges[src].push_back(Vertex(dst, cost));
    edges[dst].push_back(Vertex(src, cost));
  }

  std::priority_queue<Vertex, std::vector<Vertex>, VertexComparator> queue;
  std::vector<bool> visited(n, false);
  queue.push(Vertex(0, 0));
  while (!queue.empty()) {
    Vertex curr = queue.top();
    queue.pop();
    if (visited[curr.v])
      continue;
    visited[curr.v] = true;

    if (curr.v == n - 1) {
      std::cout << curr.cost << "\n";
      break;
    }

    for (auto it = edges[curr.v].begin(); it != edges[curr.v].end(); ++it) {
      if (!visited[it->v]) {
        queue.push(Vertex(it->v, it->cost + curr.cost));
      }
    }
  }

  return 0;
}