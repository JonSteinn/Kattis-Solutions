#include <stdio.h>
#include <string.h>

int main() {
    int occ = 0;
    char input[12];
    for (int i = 0; i < 5; i++) {
        scanf("%s", input);
        if (strstr(input, "FBI") != NULL) occ += (1<<i);
    }
    if (!occ) {
        printf("HE GOT AWAY!\n");
    } else {
        int first = 1;
        for (int i = 0; i < 5; i++) {
            if (occ & (1 << i)) {
                printf(first ? "%d" : " %d", i+1);
                first = 0;
            }
        }
        putchar('\n');
    }
    return 0;
}
