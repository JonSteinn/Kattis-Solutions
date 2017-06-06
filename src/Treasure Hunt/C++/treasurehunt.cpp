#include <stdio.h>
#include <unordered_set>

struct position
{
    int r, c;
    position(int r, int c)
    {
        this->r = r;
        this->c = c;
    }

    void moveUp(char dir)
    {
        if (dir == 'N') r--;
        else if (dir == 'S') r++;
        else if (dir == 'W') c--;
        else c++;
    }

    bool out_of_bounds(int r, int c)
    {
        return !(this->r >= 0 && this->r < r && this->c >= 0 && this->c < c);
    }

    int toInt(int c)
    {
        return this->r * c + this->c;
    }

};

int main()
{
    int r, c, step_counter = 0;
    scanf("%d %d",&r,&c);
    char level[r][c+1];
    for (int i = 0; i < r; i++) scanf("%s",level[i]);
    std::unordered_set<int> visited;
    struct position pos(0,0);
    while(1)
    {
        if (pos.out_of_bounds(r, c))
        {
            printf("Out\n");
            break;
        }
        if (visited.find(pos.toInt(c)) != visited.end())
        {
            printf("Lost\n");
            break;
        }
        char val = level[pos.r][pos.c];
        if (val == 'T')
        {
            printf("%d\n", step_counter);
            break;
        }
        int index = pos.toInt(c);
        visited.insert(index);
        pos.moveUp(val);
        step_counter++;
    }
    return 0;
}