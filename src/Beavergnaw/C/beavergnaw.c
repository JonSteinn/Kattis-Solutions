#include <stdio.h>
#include <math.h>

// How is this a programming problem?

/* Formulas used (volumes):
 *      Cylinder:   h * pi * r^2
 *      Cone:       h * r^2 * pi / 3
 *
 * We are looking for a d such that the large cylinder equals the two truncated cones
 * inside it and the smaller cylinder + the removed volume. We can find the volume
 * of the truncated cones by subtracting the missing part from a whole cone.
 *
 * Let A be the total volume, B the volume of a truncated cone and C the inner cylinder's
 * volume. Then we have A = V + 2B + C. Simplification in LaTeX below:
 *
\begin{align*}
&D(D/2)^2\pi = V + 2(D/2)^3\pi/3 - 2(d/2)^3\pi/3 + d(d/2)^2\pi
\Rightarrow d^3\pi/4-2(d/2)^3\pi/3 = D^3\pi/4-V-2(D/2)^3\pi/3\\
\Rightarrow &d^3\left(\pi/4-2(1/2)^3\pi/3\right) = D^3\pi/4-V-2(D/2)^3\pi/3
\Rightarrow d^3 = \frac{D^3\pi/4-V-2(D/2)^3\pi/3}{\pi/4-2(1/2)^3\pi/3} \\
\Rightarrow &d   = \sqrt[3]{\frac{D^3\pi/4-V-2(D/2)^3\pi/3}{\pi/4-2(1/2)^3\pi/3}}
                 = \sqrt[3]{\frac{D^3\pi/4-V-D^3\pi/12}{\pi/4-\pi/12}}
                 = \sqrt[3]{\frac{D^3\pi(1/4-1/12)-V}{\pi(1/4-1/12)}}
                 = \sqrt[3]{\frac{D^3\pi/6-V}{\pi/6}}
\end{align*}
 */

#define PI 3.1415926535897932384626434

int main()
{
    while (1)
    {
        int D, V;
        scanf("%d %d", &D, &V);
        if (!D && !V) break;
        printf("%.8f\n", pow((pow(D,3)*PI/6-V)/(PI/6),1.0/3));
    }
    return 0;
}