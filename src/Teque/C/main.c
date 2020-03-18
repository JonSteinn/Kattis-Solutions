#include <stdio.h>

#include "teque.h"

int main() {
    int n, val;
    char buffer[12];

    scanf("%d",&n);

    Teque* teque = create_teque(n);

    while (n--) {
        scanf("%s %d", buffer, &val);

        if (buffer[0] == 'g') {
            printf("%d\n", get(teque,val));
        } else if (buffer[5] == 'b') {
            push_back(teque, val);
        } else if (buffer[5] == 'f') {
            push_front(teque, val);
        } else {
            push_middle(teque, val);
        }
    }

    destroy_teque(teque);

    return 0;
}