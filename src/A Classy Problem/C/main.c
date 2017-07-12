#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define NAME_LEN 32
#define CLASS_LEN 11
#define CLASS_STR_LEN 70
#define DUMP_LEN 6
#define MAX_PPL 100

struct person
{
    char name[NAME_LEN];
    char class[CLASS_LEN];
};

int comparator(const void* a, const void* b)
{
    struct person* lhs = (struct person*)a;
    struct person* rhs = (struct person*)b;
    int n = strncmp(lhs->class, rhs->class, 10);
    return n ? n : strcmp(lhs->name, rhs->name);
}

int skips(char c)
{
    return c == 'm' ? 7 : 6;
}

char value_char(char c)
{
    if (c == 'u') return '0';
    if (c == 'm') return '1';
    return '2';
}

void reverse(char* str, int from, int to)
{
    while(++from < --to) str[from]^=str[to]^=str[from]^=str[to];
}

void fill(char* class, char* buffer, size_t buffer_len)
{
    int from_index = 0;
    int to_index = 0;
    while(from_index < buffer_len)
    {
        class[to_index++] = value_char(buffer[from_index]);
        from_index += skips(buffer[from_index]);
    }
    reverse(class, -1, to_index);
    while (to_index < 10) class[to_index++] = '1';
    class[to_index] = '\0';
}

void test_case(struct person* arr, int people)
{
    for (int i = 0; i < people; i++)
    {
        scanf("%s", arr[i].name);
        arr[i].name[strlen(arr[i].name) - 1] = '\0';
        char buffer[CLASS_STR_LEN], buffer2[DUMP_LEN];
        scanf("%s %s", buffer, buffer2);
        fill(arr[i].class, buffer, strlen(buffer));
    }
    qsort(arr, (size_t)people, sizeof(struct person), comparator);
    for (int i = 0; i < people; i++) printf("%s\n", arr[i].name);
    printf("==============================\n");
}

int main()
{
    int n;
    scanf("%d",&n);
    struct person arr[MAX_PPL];
    while(n--)
    {
        int k;
        scanf("%d", &k);
        test_case(arr, k);
    }
    return 0;
}