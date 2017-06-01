#include <cstdio>
#include <queue>

typedef std::pair<int,int> p;

struct comparator
{
    bool operator()(p const& lhs, p const& rhs) const
    {
        return lhs.second < rhs.second;
    }
};

void election()
{
    int n;
    scanf("%d",&n);
    double vote_sum = 0;
    std::priority_queue<p, std::vector<p>, comparator> votes;
    for (int i = 1; i <= n; i++)
    {
        p entry;
        entry.first = i;
        scanf("%d",&entry.second);
        vote_sum += entry.second;
        votes.push(entry);
    }
    p v1 = votes.top();
    votes.pop();
    p v2 = votes.top();
    if (v1.second == v2.second) printf("no winner\n");
    else if (v1.second / vote_sum > 0.5) printf("majority winner %d\n", v1.first);
    else printf("minority winner %d\n", v1.first);
}

int main()
{
    int n;
    scanf("%d",&n);
    while(n--) election();
    return 0;
}