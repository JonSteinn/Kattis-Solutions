#include <stdio.h>
#include <string.h>

int main() {
    int map[10] = {0,2,4,6,8,1,3,5,7,9};

    int n;
    scanf("%d",&n);
    while(n--) {
        char num[101];
        scanf("%s", num);
        size_t len = strlen(num);

        int sum = 0;
        for (int i = len - 2; i >= 0; i -= 2) sum += map[num[i] - '0'];
        for (int i = len - 1; i >= 0; i -= 2) sum += num[i]-'0';
        printf(sum % 10 ? "FAIL\n" : "PASS\n");
    }

    return 0;
}