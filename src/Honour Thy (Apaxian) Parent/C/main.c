#include <stdio.h>
#include <string.h>

int main() {
    char first[11], second[11];
    scanf("%s %s", first, second);
    size_t f_len = strlen(first);
    switch (first[f_len-1]) {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            first[f_len - 1] = 0;
            break;
        case 'x':
            if (first[f_len-2] == 'e') first[f_len - 2] = 0;
            break;
    }
    printf("%s%s%s\n", first, "ex", second);
    return 0;
}
