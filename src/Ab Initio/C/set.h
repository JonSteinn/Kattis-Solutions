#define INT_BITS 32
#define MAX_SIZE 125
#define INIT_SET_EMPTY (IntSet){{[0 ... (MAX_SIZE-1)] = 0}}

typedef struct {
    int bits[MAX_SIZE];
} IntSet;

int set_contains(IntSet *set, int n);
void set_add(IntSet *set, int n);
void set_remove(IntSet *set, int n);
void set_complement_up_to(IntSet* set, int max);