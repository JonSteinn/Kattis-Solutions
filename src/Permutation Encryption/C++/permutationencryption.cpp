#include <cstdio>
#include <string>
#include <iostream>

int main()
{
    while(1)
    {
        int n;
        scanf("%d", &n);
        if (n == 0) break;

        int arr[n];
        for (int i = 0; i < n; i++) scanf("%d", arr + i);

        std::string msg;
        std::cin.ignore();
        std::getline(std::cin, msg);
        size_t remainder = msg.length() % n;
        if (remainder > 0) msg.append(n - (msg.length() % n), ' '); // padding

        size_t iterations = msg.length() / n;
        printf("'");
        for (int i = 0; i < iterations; i++)
        {
            for (int j = 0; j < n; j++)
            {
                printf("%c", msg[i * n  + arr[j] - 1]);
            }
        }
        printf("'\n");

    }
    return 0;
}