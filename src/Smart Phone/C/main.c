#include <stdio.h>
#include <string.h>

struct string
{
    char str[26];
    size_t len;
};

struct state
{
    struct string goal;
    struct string current;
    struct string suggestions[3];
};

int change_to(struct string* s1, struct string* s2)
{
    int counter = 0;
    if (s1->len > s2->len)
    {
        counter += (s1->len - s2->len);
        s1->str[s2->len] = '\0';
        s1->len = s2->len;
    }
    while (s1->len >= 0 && strncmp(s1->str, s2->str, s1->len))
    {
        s1->len--;
        s1->str[s1->len] = '\0';
        counter++;
    }
    return (int)(counter + (s2->len - s1->len));
}

int min(int a, int b)
{
    return a < b ? a : b;
}

int test_case(struct state* s)
{
    int steps = change_to(&s->current, &s->goal);
    for (int i = 0; i < 3; i++) steps = min(steps, 1 + change_to(&s->suggestions[i], &s->goal));
    return steps;
}

int main()
{
    struct state s;
    int n;
    scanf("%d",&n);
    while(n--)
    {
        scanf("%s", s.goal.str);
        s.goal.len = strlen(s.goal.str);

        scanf("%s", s.current.str);
        s.current.len = strlen(s.current.str);

        for (int i = 0; i < 3; i++)
        {
            scanf("%s", s.suggestions[i].str);
            s.suggestions[i].len = strlen(s.suggestions[i].str);
        }

        printf("%d\n", test_case(&s));
    }
    return 0;
}