#include <vector>
#include <queue>
#include <tuple>
#include <stdio.h>
#include <algorithm>

struct Node {
    Node(int r, int c, int cost ): r(r),c(c),cost(cost) {}
    int r;
    int c;
    int cost;
};

struct NodeCompare {
    bool operator()(const Node& lhs, const Node& rhs) {
        return lhs.cost > rhs.cost;
    }
};

int find(std::vector<std::vector<int>>& mat, int r, int c) {
    bool closed_set[r*c] = {false};
    std::priority_queue<Node, std::vector<Node>, NodeCompare> open_set;
    open_set.push(Node(0,0,0));

    while (!open_set.empty()) {
        // Get next
        Node current = open_set.top();
        open_set.pop();

        // Goal and visited check
        int one_dim = current.r * c + current.c;
        if (closed_set[one_dim]) continue;
        if (current.r == r-1 && current.c == c-1) return current.cost;
        closed_set[one_dim] = true;

        // Expand
        if (current.r > 0 && !closed_set[(current.r-1)*c + current.c]) {
            open_set.push(Node(current.r-1,current.c,std::max(current.cost,mat[current.r-1][current.c] - mat[current.r][current.c])));
        }
        if (current.r < r-1 && !closed_set[(current.r+1)*c + current.c]) {
            open_set.push(Node(current.r+1,current.c,std::max(current.cost,mat[current.r+1][current.c] - mat[current.r][current.c])));
        }
        if (current.c > 0 && !closed_set[current.r*c + current.c - 1]) {
            open_set.push(Node(current.r,current.c-1,std::max(current.cost,mat[current.r][current.c-1] - mat[current.r][current.c])));
        }
        if (current.c < c-1 && !closed_set[current.r*c + current.c + 1]) {
            open_set.push(Node(current.r,current.c+1,std::max(current.cost,mat[current.r][current.c+1] - mat[current.r][current.c])));
        }

    }
    // No path (won't happen)
    return -1;
}

int main() {
    int r,c;
    scanf("%d %d", &r, &c);
    std::vector<std::vector<int>> matrix(r, std::vector<int>(c, 0));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d",&matrix[i][j]);
        }
    }
    printf("%d\n", find(matrix,r,c));
}