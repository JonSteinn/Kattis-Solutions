#include <stdio.h>
#include <math.h>
#include <unordered_set>

#define HAPPY 1
#define UNHAPPY 0
#define UNKNOWN -1

struct feelings
{
    std::unordered_set<int> happy;
    std::unordered_set<int> unhappy;

    void add_happies(const std::unordered_set<int>& h)
    {
        happy.insert(h.begin(), h.end());
    }

    void add_unhappies(const std::unordered_set<int>& h)
    {
        unhappy.insert(h.begin(), h.end());
    }

    int status(int n)
    {
        return happy.find(n) != happy.end() ? HAPPY : unhappy.find(n) != unhappy.end() ? UNHAPPY : UNKNOWN;
    }
};

int prime_loop(int n)
{
    int max = (int)sqrt(n) + 1;
    for (int i = 5; i <= max; i += 6)
    {
        if (n % i == 0 || n % (i + 2) == 0) return 0;
    }
    return 1;
}

int is_prime(int n)
{
    return n < 2 ? 0 : (n < 4 ? 1 : (n % 2 == 0 || n % 3 == 0 ? 0 : (n < 25 ? 1 : prime_loop(n))));
}

int square_digit_sum(int n)
{
    int sum = 0;
    while(n)
    {
        int next = n % 10;
        sum += next * next;
        n /= 10;
    }
    return sum;
}

int is_happy(int n, feelings& f)
{
    if (n < 7) return false;
    int _status = f.status(n);
    if (_status < 0)
    {
        std::unordered_set<int> temp;
        int k = square_digit_sum(n);
        temp.insert(n);
        while (k != 1 && temp.find(k) == temp.end())
        {
            temp.insert(k);
            k = square_digit_sum(k);
        }
        if (k == 1)
        {
            f.add_happies(temp);
            return HAPPY;
        }
        else
        {
            f.add_unhappies(temp);
            return UNHAPPY;
        }
    }
    else
    {
        return _status;
    }
}

void test_case(feelings& f)
{
    int tc, n;
    scanf("%d %d",&tc,&n);
    printf("%d %d %s\n", tc, n, is_prime(n) && is_happy(n, f) ? "YES" : "NO");
}

int main()
{
    feelings f;
    int n;
    scanf("%d",&n);
    while (n--) test_case(f);
    return 0;
}