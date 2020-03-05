#include <stdio.h>

int main() {
    char m[4];
    int d;
    scanf("%s %d", m, &d);
    printf((m[0] == 'O' && d == 31) || (m[0] == 'D' && d == 25) ?"yup\n" : "nope\n");
}
