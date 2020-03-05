#include <stdio.h>
#include <string.h>

void encode(const char* msg, size_t len) {
    int run = 1;
    int index = 1;
    while (index < len) {
        if (msg[index] == msg[index-1]) {
            run++;
        } else {
            printf("%c%d", msg[index-1], run);
            run = 1;
        }
        index++;
    }
    printf("%c%d", msg[len-1], run);
}

void decode(const char* msg, size_t len) {
    for (int i = 0; i < len; i += 2) {
        int repeats = msg[i+1] - '0';
        while (repeats--) putchar(msg[i]);
    }
}

int main() {
    char x, msg[101];
    scanf("%c %s", &x, msg);
    if (x == 'E') {
        encode(msg, strlen(msg));
    } else {
        decode(msg, strlen(msg));
    }
    putchar('\n');
    return 0;
}