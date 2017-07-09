#include <stdio.h>
#include <stdlib.h>

struct node
{
    int value;
    struct node* next;
};

struct mem_stack
{
    struct node* memory;
    struct node* current;
};

void ms_init(struct mem_stack* mem, int max_cap)
{
    mem->memory = (struct node*)malloc(sizeof(struct node) * max_cap);
    mem->current = mem->memory;
}

void ms_destroy(struct mem_stack* mem)
{
    free(mem->memory);
}

struct node* allocate(struct mem_stack* mem, int value)
{
    mem->current->value = value;
    mem->current->next = NULL;
    return mem->current++;
}

struct list
{
    int count;
    struct node* head;
    struct node* tail;
};

void init(struct list* lst)
{
    lst->count = 0;
    lst->head = NULL;
    lst->tail = NULL;
}

void push_back(struct list* lst, struct mem_stack* mem, int value)
{
    if (lst->head == NULL)
    {
        lst->head = allocate(mem, value);
        lst->tail = lst->head;
    }
    else
    {
        lst->tail->next = allocate(mem, value);
        lst->tail = lst->tail->next;
    }
    lst->count++;
}

int rem(struct mem_stack* m, struct list* l)
{
    int total_removed = 0;
    while (l->count > 1 && (l->head->value & 1) == (l->head->next->value & 1))
    {
        l->head = l->head->next->next;
        l->count -= 2;
        total_removed += 2;
    }
    if (l->count >= 3)
    {
        struct node *prev = l->head;
        struct node *curr = l->head->next;
        struct node *next = l->head->next->next;
        while (l->count > 1 && next != NULL)
        {
            if ((curr->value & 1) == (next->value & 1))
            {
                l->count -= 2;
                total_removed += 2;
                prev->next = next->next;
                curr = prev->next;
                if (curr == NULL) break;
                next = curr->next;
            }
            else
            {
                next = next->next;
                curr = curr->next;
                prev = prev->next;
            }
        }
    }
    return total_removed;
}

int main()
{
    struct mem_stack m;
    struct list l;
    int n;
    scanf("%d",&n);
    ms_init(&m, n);
    init(&l);
    for (int i = 0; i < n; i++)
    {
        int x;
        scanf("%d",&x);
        push_back(&l, &m, x);
    }
    int removes = 0, remove = 0;
    while (l.count > 1 && (remove = rem(&m, &l))) removes += remove;
    printf("%d\n", n - removes);
    ms_destroy(&m);
    return 0;
}
