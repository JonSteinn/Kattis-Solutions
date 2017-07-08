#include <stdio.h>

void recipe(int ingredients, double scale)
{
    char names[ingredients][21];
    double percentage[ingredients];
    double migs = -1; // main-ingredient-grams-scaled
    for (int i = 0; i < ingredients; i++)
    {
        double g;
        scanf("%s %lf %lf", names[i], &g, percentage + i);
        if (percentage[i] == 100.0) migs = g * scale;
        percentage[i] /= 100.0;
    }
    for (int i = 0; i < ingredients; i++) printf("%s %.1lf\n", names[i], migs * percentage[i]);
}

int main()
{
    int n;
    scanf("%d",&n);
    for (int i = 0; i < n; i++)
    {
        int r,p,d;
        scanf("%d %d %d", &r, &p, &d);
        printf("Recipe # %d\n", i + 1);
        recipe(r, d / (double)p);
        printf("----------------------------------------\n");
    }
    return 0;
}