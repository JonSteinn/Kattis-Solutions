#include <stdio.h>
#include <string>
#include <vector>
#include <queue>
#include <cstring>

void experiment()
{
    std::priority_queue<std::string, std::vector<std::string>, std::greater<std::string>> pq;

    int n;
    scanf("%d", &n);
    while (n-- > 0)
    {
        char buffer[11];
        scanf("%s", buffer);
        pq.push(std::string(buffer));
    }

    std::string _old = pq.top(); pq.pop();
    while (pq.size() > 0)
    {
        std::string _new = pq.top(); pq.pop();
        if (!strncmp(_new.c_str(), _old.c_str(), strlen(_old.c_str())))
        {
            printf("No\n");
            return;
        }
        else _old = _new;
    }
    printf("Yes\n");
}
int main()
{
    int n;
    scanf("%d", &n);
    while (n-- > 0) experiment();
    return 0;
}