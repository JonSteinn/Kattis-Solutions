#include <stdio.h>
#include <stdlib.h>

#define MAX_ITEMS 2000
#define MAX_WEIGHT 2000

typedef struct {
    int weight;
    int value;
} KnapsackItem;

typedef struct {
    KnapsackItem items[MAX_ITEMS];
    int memory[MAX_ITEMS+1][MAX_WEIGHT+1];
    int solution[MAX_ITEMS];
    int solution_length;
    int c, n;
} Knapsack;

int max(int a, int b) { return a < b ? b : a; }

int bottom_up_knapsack(Knapsack *k) {
    for (int i = 0; i <= k->n; i++) { 
        for (int c = 0; c <= k->c; c++) { 
            if (i == 0 || c == 0) k->memory[i][c] = 0; 
            else if (k->items[i-1].weight <= c) k->memory[i][c] = max(k->items[i-1].value+k->memory[i-1][c-k->items[i-1].weight],k->memory[i-1][c]); 
            else k->memory[i][c] = k->memory[i-1][c]; 
        } 
    }
    return k->memory[k->n][k->c];
}

void find_solution(Knapsack *k, int best) {
    k->solution_length = 0;
    int c = k->c; 
    for (int i = k->n; i > 0 && best > 0; i--) {
        if (best != k->memory[i-1][c]) {
            k->solution[k->solution_length++] = i-1;
            best -= k->items[i-1].value;
            c -= k->items[i-1].weight;
        }
    } 
}

void print_solution(Knapsack *k) {
    printf("%d\n", k->solution_length);
    if (k->solution_length > 0) {
        for (int i = 0; i < k->solution_length; i++) {
            if (i) putchar(' ');
            printf("%d", k->solution[i]);
        }
        putchar('\n');
    }
}

int main() {
    Knapsack *k = (Knapsack*)malloc(sizeof(Knapsack));
    while (scanf("%d %d", &k->c, &k->n) == 2) {
        for (int i = 0; i < k->n; i++) {
            scanf("%d %d", &k->items[i].value, &k->items[i].weight);
        }
        int best = bottom_up_knapsack(k);
        find_solution(k, best);
        print_solution(k);
    }
    free(k);

    return 0;
}