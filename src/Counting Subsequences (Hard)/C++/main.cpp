#include <stdio.h>
#include <unordered_map>

typedef long long ll;

int main()
{
    int n;
    scanf("%d", &n);
    while(n--) {
        int len;
        scanf("%d", &len);
        if (len > 0 ) {
            ll counter = 0;
            std::unordered_map<ll, int> occurrences((size_t)(len / 0.7));
            occurrences[0] = 1;
            ll last = 0;
            ll current = 0;
            for (int i = 0; i < len; i++) {
                scanf("%lld", &current);
                current += last;
                ll key = current - 47;
                if (occurrences.find(key) != occurrences.end()) {
                    counter += occurrences[key];
                }
                if (occurrences.find(current) == occurrences.end()) {
                    occurrences[current] = 0;
                }
                occurrences[current]++;
                last = current;
            }
            printf("%lld\n", counter);
        } else {
            printf("0\n");
        }
    }
    return 0;
}