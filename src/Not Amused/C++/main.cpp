#include <stdio.h>
#include <map>

void day(int d)
{
    printf(d == 1 ? "Day %d\n" : "\nDay %d\n", d);
    std::map<std::string, std::pair<double,double>> tree_map;

    while(1)
    {
        char first[6];
        scanf("%s",first);
        if (first[0] == 'C')
        {
            for (std::map<std::string, std::pair<double, double>>::iterator it = tree_map.begin(); it != tree_map.end(); ++it)
            {
                printf("%s $%.2lf\n", it->first.c_str(), it->second.first);
            }
            break;
        }

        char second[21];
        int third;
        scanf("%s %d", second, &third);
        std::string name(second);

        if (first[1] == 'N')
        {
            if (tree_map.find(name) == tree_map.end())
            {
                tree_map.insert(std::pair<std::string, std::pair<double,double>>(name, std::pair<double, double>(0.0,0.0)));
            }
            tree_map[name].second = third;
        }
        else tree_map[name].first += (third - tree_map[name].second) * 0.1;
    }
}

int main() {
    int d = 1;
    char open[5];
    while (scanf("%s", open) == 1) day(d++);
    return 0;
}