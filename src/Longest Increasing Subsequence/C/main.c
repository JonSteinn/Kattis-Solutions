#include stdio.h

void sequence(int arr, int n)
{
    int P[n],M[n+1];
    int len = 0;
    for (int i = 0; i  n; i++)
    {
        int lo = 1;
        int hi = len;
        while (lo = hi)
        {
            int mid = (lo+hi)1;
            if (arr[M[mid]]  arr[i]) lo = mid+1;
            else hi = mid-1;
        }
        P[i] = M[lo-1];
        M[lo] = i;
        if (lo  len) len = lo;
    }
    int indices[len];
    int next_index = M[len];
    for (int i = len-1; i = 0; i--)
    {
        indices[i] = next_index;
        next_index = P[next_index];
    }
    printf(%dn, len);
    for (int i = 0; i  len - 1; i++) printf(%d , indices[i]);
    printf(%dn, indices[len-1]);

}

int main()
{
    int n;
    while (scanf(%d,&n) == 1)
    {
        int arr[n];
        for (int i = 0; i  n; i++) scanf(%d,arr+i);
        sequence(arr, n);
    }
    return 0;
}