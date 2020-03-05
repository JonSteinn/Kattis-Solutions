#include <stdio.h>

/**
Winning strategy:

Remove all T leaving even number of H remaining. If H + T/2 is even,
then removing T (2 at a time) leaves Heads even (adding one at each removal).
To make H+T/2 even, we can increment T by one. Note that T must be even before
we start removing it (2 at a time).
*/

int main() {
    while(1) {
        int h, t;
        scanf("%d %d", &h, &t);
        if (!h && !t) break;
        printf("%d\n", ((h % 2) * 2 + (t % 4) * 3) % 4 + (t+((h % 2) * 2 + (t % 4) * 3) % 4)/2 + (h+(t+((h % 2) * 2 + (t % 4) * 3) % 4)/2)/2);
    }
    return 0;
}