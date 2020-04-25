#include <stdio.h>
#include <stdlib.h>

#define POSSIBLE_STEPS 8
#define MAX_QUEUE 10000
#define IB 32

typedef struct {
    int r, c;
} Step;

typedef struct {
    int r,c,g_r,g_c,l_r,l_c;
    Step steps[POSSIBLE_STEPS];
} World;

typedef struct {
    int cost[MAX_QUEUE];
    int arr[MAX_QUEUE];
    int head, tail;
} Queue;

void init_queue(Queue *queue, int first) {
    queue->arr[0] = first;
    queue->cost[0] = 0;
    queue->tail = 1;
    queue->head = 0;
}

int *init_ds(World *world, Queue *queue) {
    //int *visited = (int*)calloc((world->r*world->c)/IB,sizeof(int));
    int *visited = (int*)calloc(world->r * world->c,sizeof(int));
    int g_init = world->g_r * world->c + world->g_c;
    //visited[g_init/IB] |= (1<<(g_init % IB));
    visited[g_init] = 1;
    init_queue(queue, g_init);
    return visited;
}

void test_case(World *world) {
    Queue queue;
    int *visited = init_ds(world, &queue);

    while (queue.head != queue.tail) {
        int curr = queue.arr[queue.head];
        int curr_cost = queue.cost[queue.head++];
        int curr_c = curr % world->c;
        int curr_r = (curr-curr_c) / world->c;

        for (int i = 0; i < POSSIBLE_STEPS; i++) {
            int n_r = curr_r + world->steps[i].r;
            int n_c = curr_c + world->steps[i].c;

            // Found
            if (n_r == world->l_r && n_c == world->l_c) {
                printf("%d\n", curr_cost+1);
                free(visited);
                return;
            }

            // OOB
            if (n_r < 0 || n_r >= world->r || n_c < 0 || n_c >= world->c) continue;

            // visited
            int n_one = n_r * world->c + n_c;
            //if (visited[n_one/IB] & (1<<(n_one % IB))) continue;
            if (visited[n_one]) continue;

            // Unexplored
            //visited[n_one/IB] |= (1<<(n_one % IB));
            visited[n_one] = 1;
            queue.arr[queue.tail] = n_one;
            queue.cost[queue.tail++] = curr_cost + 1;
        }
    }

    printf("impossible\n");
    free(visited);
}

void init_world_steps(World *world) {
    world->steps[0] = (Step){-2,-1};
    world->steps[1] = (Step){-2,1};
    world->steps[2] = (Step){-1,-2};
    world->steps[3] = (Step){-1,2};
    world->steps[4] = (Step){1,-2};
    world->steps[5] = (Step){1,2};
    world->steps[6] = (Step){2,-1};
    world->steps[7] = (Step){2,1};
}

int main() {
    World world;
    init_world_steps(&world);
    while (scanf("%d %d %d %d %d %d", &world.r, &world.c, &world.g_r, &world.g_c, &world.l_r, &world.l_c)==6) {
        if (world.g_r == world.l_r && world.g_c == world.l_c) {
            printf("0\n");
        } else {
            world.g_r--;
            world.g_c--;
            world.l_r--;
            world.l_c--;
            test_case(&world);
        }
    }
    return 0;
}