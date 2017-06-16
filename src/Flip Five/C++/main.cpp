#include <stdio.h>
#include <unordered_set>
#include <queue>

struct node
{
    node(short val, int cost) : val(val), cost(cost) {}
    short val;
    int cost;
};

short toggle(short x, int p)
{
    switch (p)
    {
        case 0:
            x ^= 1 << 0;
            x ^= 1 << 1;
            x ^= 1 << 3;
            return x;
        case 1:
            x ^= 1 << 0;
            x ^= 1 << 1;
            x ^= 1 << 2;
            x ^= 1 << 4;
            return x;
        case 2:
            x ^= 1 << 1;
            x ^= 1 << 2;
            x ^= 1 << 5;
            return x;
        case 3:
            x ^= 1 << 0;
            x ^= 1 << 3;
            x ^= 1 << 4;
            x ^= 1 << 6;
            return x;
        case 4:
            x ^= 1 << 1;
            x ^= 1 << 3;
            x ^= 1 << 4;
            x ^= 1 << 5;
            x ^= 1 << 7;
            return x;
        case 5:
            x ^= 1 << 2;
            x ^= 1 << 4;
            x ^= 1 << 5;
            x ^= 1 << 8;
            return x;
        case 6:
            x ^= 1 << 3;
            x ^= 1 << 6;
            x ^= 1 << 7;
            return x;
        case 7:
            x ^= 1 << 4;
            x ^= 1 << 6;
            x ^= 1 << 7;
            x ^= 1 << 8;
            return x;
        default:
            x ^= 1 << 5;
            x ^= 1 << 7;
            x ^= 1 << 8;
            return x;
    }
}

int main()
{
    int n;
    scanf("%d",&n);
    while(n--)
    {
        bool found_goal = false;
        short init = 0;
        char in[10];
        scanf("%s", in); scanf("%s", in + 3); scanf("%s", in + 6);
        for (int i = 0; i < 9; i++) if (in[i] == '*') init |= (1 << i);

        if (init == 0)
        {
            printf("0\n");
            continue;
        }

        // BFS

        std::queue<node> open;
        std::unordered_set<short> closed;

        open.push(node(init, 0));
        while(!open.empty())
        {
            node curr = open.front();
            open.pop();

            if (closed.find(curr.val) != closed.end()) continue;
            closed.insert(curr.val);

            for (int i = 0; i < 9; i++)
            {
                short next = toggle(curr.val, i);
                if (next == 0)
                {
                    printf("%d\n", curr.cost + 1);
                    found_goal = true;
                    break;
                }
                if (closed.find(next) == closed.end()) open.push(node(next, curr.cost + 1));
            }
            if (found_goal) break;
        }
    }
    return 0;
}