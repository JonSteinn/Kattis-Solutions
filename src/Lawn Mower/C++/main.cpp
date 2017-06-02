#include <cstdio>
#include <vector>
#include <stack>

struct interval
{
    double min, max;
    interval(double min, double max) : min(min), max(max) {}

    bool intersect(const interval& other)
    {
        return max >= other.min && other.max >= min;
    }

    void join(const interval& other)
    {
        if (other.min < min) min = other.min;
        if (other.max > max) max = other.max;
    }

    bool contains(const interval& other)
    {
        return min <= other.min && max >= other.max;
    }
};

bool covers(std::stack<interval>& intervals, interval& goal)
{
    while (intervals.size() > 1)
    {
        bool found = false;
        interval curr = intervals.top();
        intervals.pop();

        std::stack<interval> temp;

        while (!intervals.empty())
        {
            interval next = intervals.top();
            intervals.pop();
            if (curr.intersect(next))
            {
                curr.join(next);
                found = true;
            }
            else temp.push(next);
        }
        if (!found && temp.size() > 0) return false;

        intervals = temp;
        intervals.push(curr);
    }
    return intervals.top().contains(goal);
}

int main()
{
    interval h_goal(0.0, 75.0), v_goal(0.0, 100.0);
    while(1)
    {
        int n_x, n_y;
        double w;
        scanf("%d %d %lf", &n_x, &n_y, &w);
        if (n_x == 0 && n_y == 0 && w == 0.0) break;
        w /= 2.0;
        std::stack<interval> horizontal, vertical;
        for (int i = 0; i < n_x; i++)
        {
            double c;
            scanf("%lf", &c);
            interval next = interval(c - w, c + w);
            if (h_goal.intersect(next)) horizontal.push(next);
        }
        for (int i = 0; i < n_y; i++)
        {
            double c;
            scanf("%lf", &c);
            interval next = interval(c - w, c + w);
            if (v_goal.intersect(next)) vertical.push(next);
        }
        printf(covers(horizontal, h_goal) && covers(vertical, v_goal) ? "YES\n" : "NO\n");
    }
    return 0;

}