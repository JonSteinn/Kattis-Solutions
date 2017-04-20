#include <stdio.h>
#include <stdlib.h>
#include "string.h"

#define MAX_LINE 81

struct node
{
    short data;
    struct node* next;
};

struct node* create_node(short value)
{
    struct node* n = (struct node*)malloc(sizeof(struct node));
    n->data = value;
    return n;
}

int main()
{
    struct node* head = NULL;
    struct node* current = NULL;
    char buffer[MAX_LINE];

    fgets(buffer, MAX_LINE, stdin);
    short max = (short)strlen(buffer);
    max--;
    head = create_node(max);
    current = head;

    while (fgets(buffer, MAX_LINE, stdin))
    {
        short len = (short)strlen(buffer);
        len--;
        if (len > max) max = len;
        current->next = create_node(len);
        current = current->next;
    }
    current->next = NULL;
    int rag = 0;
    struct node* temp;
    while (head != NULL)
    {
        if (head->next != NULL)
        {
            int root_rag = max - head->data;
            rag += root_rag * root_rag;
        }
        temp = head;
        head = head->next;
        free(temp);
    }

    printf("%d\n", rag);
    return 0;
}