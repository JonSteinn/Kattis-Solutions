#include <stdio.h>
#include <unordered_set>
#include <stack>


int main()
{
    int w, h;
    scanf("%d %d",&w,&h);

    int player_pos = -1;

    char grid[h][w + 1];
    for (int i = 0; i < h; i++)
    {
        scanf("%s", grid[i]);
        if (player_pos < 0)
        {
            for (int j = 0; j < w; j++)
            {
                if (grid[i][j] == 'P')
                {
                    player_pos = i * w + j;
                }
            }
        }
    }

    int counter = 0;

    // DFS

    std::unordered_set<int> closed;
    std::stack<int> open;
    open.push(player_pos);

    while(!open.empty())
    {
        int current = open.top();
        open.pop();

        if (closed.find(current) != closed.end()) continue;
        closed.insert(current);

        int a = current / w;
        int b = current - a * w;
        if (grid[a][b] == 'G') counter++;

        bool add_1 = false, add_2 = false, add_3 = false, add_4 = false;

        int next1 = current - 1;
        if (closed.find(next1) == closed.end())
        {
            a = next1 / w;
            b = next1 - a * w;
            if (grid[a][b] == 'T') continue;
            if (grid[a][b] != '#') add_1 = true;
        }

        int next2 = current + 1;
        if (closed.find(next2) == closed.end())
        {
            a = next2 / w;
            b = next2 - a * w;
            if (grid[a][b] == 'T') continue;
            if (grid[a][b] != '#') add_2 = true;
        }

        int next3 = current - w;
        if (closed.find(next3) == closed.end())
        {
            a = next3 / w;
            b = next3 - a * w;
            if (grid[a][b] == 'T') continue;
            if (grid[a][b] != '#') add_3 = true;
        }

        int next4 = current + w;
        if (closed.find(next4) == closed.end())
        {
            a = next4 / w;
            b = next4 - a * w;
            if (grid[a][b] == 'T') continue;
            if (grid[a][b] != '#') add_4 = true;
        }

        if (add_1) open.push(next1);
        if (add_2) open.push(next2);
        if (add_3) open.push(next3);
        if (add_4) open.push(next4);
    }

    printf("%d\n", counter);

    return 0;
}