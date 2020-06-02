#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <assert.h>

#define PPOS -1
#define NPOS 1

int min(int a, int b) { return a<b?a:b; }
int max(int a, int b) { return a<b?b:a; }

// Bruteforce
int play(int k, int a, int b) {
    char *positions = (char*)calloc(k+1,sizeof(char));
    int curr = -1, winner = -1;
    while (1) {
        curr++;
        if (positions[curr] == 0) {
            positions[curr] = PPOS;
            if (curr == k) {
                winner = 1;
                break;
            }
            if (curr+a <= k && k <= curr+b) {
                winner = 0;
                break;
            }
            if (curr+a <= k) {
                int top = min(curr+b,k);
                for (int i = curr+a; i <= top; i++) positions[i] = NPOS;
            }
        }
    }
    free(positions);
    return winner;
}

// gcc main.c -o main
// ./main > test.c
int main() {
    printf("#include <stdio.h>\n#include <stdlib.h>\n#include <assert.h>\n\n#define ALEX 0\n#define BARB 1\n\n");
    printf("int play(int k, int a, int b) {\n    // TODO\n    return 0;\n}\n\n");
    printf("int main() {\n");
    srand(time(NULL));
    int n = 1000, inner = 5;
    while (n--) {
        for (int i = 0; i < inner; i++) {
            int k = 1 + rand() % (n+6);
            int a = 1 + rand() % (n+6);
            int b = a + rand() % (n+6);
            printf("    assert(play(%d,%d,%d) == %s);\n", k, a, b, play(k, a, b) == 1 ? "BARB" : "ALEX");
        }
    }
    printf("    return 0;\n}\n");
    return 0;
}