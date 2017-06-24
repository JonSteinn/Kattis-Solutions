#include <stdio.h>
#include <unordered_map>
#include <unordered_set>
#include "BFS_Queue.h"
#include "Pair_Stack.h"

#define FIRE '*'
#define FIRE2 'X'
#define EMPTY '.'
#define PLAYER '@'

short one = 1;

struct grid {
    int r, c;
    char** data;
    grid(int r, int c) {
        this->r = r;
        this->c = c;
        data = (char**)malloc(sizeof(char*) * r);
        for (int i = 0; i < r; i++) data[i] = (char*)malloc(sizeof(char)*(c+1));
    }
    ~grid() {
        for (int i = 0; i < r; i++) free(data[i]);
        free(data);
    }

    void set_fire(int r, int c) {
        *(*(data + r) + c) = FIRE2;
    }

    bool has_fire_init(int r, int c) {
        return data[r][c] == FIRE;
    }

    bool has_fire(int r, int c) {
        return data[r][c] == FIRE2;
    }

    bool is_clear(int r, int c) {
        return data[r][c] == EMPTY;
    }

    bool has_player(int r, int c) {
        return data[r][c] == PLAYER;
    }

    void read(Pair_Stack& fire_iterable, short& init_r, short& init_c) {
        for (int i = 0; i < r; i++) {
            scanf("%s", data[i]);
            for (int j = 0; j < c; j++) {
                if (has_fire_init(i, j)) {
                    fire_iterable.push((short)j, (short)i);
                } else if (has_player(i,j)) {
                    init_r = (short)i;
                    init_c = (short)j;
                }
            }
        }
    }

    void find_goals(std::unordered_set<int>& goals) {
        for (int i = 0; i < c; i++) {
            if (is_clear(0, i) || has_player(0,i)) goals.insert(i);
            if (is_clear(r-1,i) || has_player(r-1,i)) goals.insert((r-1) * c + i);
        }
        for (int i = 0; i < r; i++) {
            if (is_clear(i,0) || has_player(i,0)) goals.insert(i * c);
            if (is_clear(i,c-1) || has_player(i,c-1)) goals.insert(i * c + c - 1);
        }
    }
};

void wildfire(Pair_Stack& from, Pair_Stack& to, grid& room) {
    while (!from.is_empty()) {
        FNode* fn = from.pop();
        short f_c = fn->x;
        short f_r = fn->y;
        if (room.has_fire(f_r, f_c)) continue;
        room.set_fire(f_r, f_c);
        if (f_r > 0 && room.is_clear(f_r-1,f_c)) to.push(f_c, f_r - one);
        if (f_r < room.r-1 && room.is_clear(f_r+1,f_c)) to.push(f_c, f_r + one);
        if (f_c > 0 && room.is_clear(f_r,f_c-1)) to.push(f_c - one, f_r);
        if (f_c < room.c-1 && room.is_clear(f_r,f_c+1)) to.push(f_c + one, f_r);
    }
}


void test_case(int r, int c) {
    int total = r * c;
    short init_r = 0, init_c = 0;
    Pair_Stack fire_iterable0((r * c)<<2), fire_iterable1((r * c)<<2);
    std::unordered_set<int> goals((size_t)(((r<<1)+(c<<1)))<<1);
    grid room(r,c);

    room.read(fire_iterable0, init_r, init_c);
    room.find_goals(goals);

    char* closed = (char*)calloc((size_t)total, sizeof(char));
    BFS_Queue open(total << 2);
    open.add(init_c, init_r, 0);

    int path_cost = -1;
    int spread_fire = 0;

    while (!open.is_empty()) {
        Node* current = open.poll();
        short curr_c = current->x;
        short curr_r = current->y;
        int curr_cost = current->cost;
        int one_dim = curr_r * c + curr_c;
        if (closed[one_dim]) continue;
        closed[one_dim] = 1;

        if (goals.find(one_dim) != goals.end()) {
            path_cost = curr_cost;
            break;
        }

        for (int i = spread_fire; i <= curr_cost + 1; i++) {
            spread_fire++;
            if (spread_fire % 2) {
                wildfire(fire_iterable0, fire_iterable1, room);
            } else {
                wildfire(fire_iterable1, fire_iterable0, room);
            }
        }

        if (curr_r > 0 && !closed[(curr_r-1)*c + curr_c] && room.is_clear(curr_r-1,curr_c)) {
            open.add(curr_c, curr_r - one, curr_cost + 1);
        }
        if (curr_r < r - 1 && !closed[(curr_r+1)*c + curr_c] && room.is_clear(curr_r+1,curr_c)) {
            open.add(curr_c, curr_r + one, curr_cost + 1);
        }
        if (curr_c > 0 && !closed[curr_r*c + curr_c - 1] && room.is_clear(curr_r, curr_c-1)) {
            open.add(curr_c - one, curr_r, curr_cost + 1);
        }
        if (curr_c < c - 1 && !closed[curr_r*c + curr_c + 1] && room.is_clear(curr_r, curr_c+1)) {
            open.add(curr_c + one, curr_r, curr_cost + 1);
        }
    }

    if (path_cost < 0) printf("IMPOSSIBLE\n");
    else printf("%d\n", path_cost + 1);

    free(closed);
}

int main() {
    int n;
    scanf("%d",&n);
    while(n--) {
        int c, r;
        scanf("%d %d",&c,&r);
        test_case(r, c);
    }
    return 0;
}