#include <stdio.h>
#include <queue>
#include <stack>

void test_case(int cases)
{
    std::priority_queue<int> pq;
    std::queue<int> q;
    std::stack<int> s;

    bool pq_valid = true, q_valid = true, s_valid = true;

    while(cases--)
    {
        int op, val;
        scanf("%d %d", &op, &val);

        if (op == 1)
        {
            if (pq_valid) pq.push(val);
            if (q_valid) q.push(val);
            if (s_valid) s.push(val);
        }
        else
        {
            if (pq_valid)
            {
                if (pq.empty() || pq.top() != val) pq_valid = false;
                else pq.pop();
            }
            if (q_valid)
            {
                if (q.empty() || q.front() != val) q_valid = false;
                else q.pop();
            }
            if (s_valid)
            {
                if (s.empty() || s.top() != val) s_valid = false;
                else s.pop();
            }
        }
    }

    int valid = (pq_valid ? 1 : 0) + (q_valid ? 1 : 0) + (s_valid ? 1 : 0);
    if (valid == 0) {
        printf("impossible\n");
    } else if (valid > 1) {
        printf("not sure\n");
    } else {
        printf(pq_valid ? "priority queue\n" : (q_valid ? "queue\n" : "stack\n"));
    }
}

int main()
{
    int n;
    while (scanf("%d", &n) != EOF) test_case(n);
    return 0;
}