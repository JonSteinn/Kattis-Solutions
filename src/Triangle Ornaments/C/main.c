// Explanation below...

#include <stdio.h>
#include <math.h>

typedef unsigned long long ull;

int main( ) {
    int n, a, c, b, tmp;
    ull asq, bsq, csq, x;
    scanf("%d",&n);
    
    double sum = 0;
    while(n--) {
        scanf("%d %d %d", &a, &b, &c);
        if (a == b) {
            sum += c;
        } else {
            if (a<b) a^=b^=a^=b;
            asq = a*a, bsq = b*b, csq = c*c;
            x = asq-bsq;
            sum += sqrt(csq-x*x/(double)(2*asq+2*bsq-csq));
        }
    }

    printf("%.4lf\n", sum);
}

// LaTeX explanation:

/*

\documentclass[11pt,a4paper,notitlepage]{article}
\usepackage[margin = 1.5cm]{geometry}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[T1]{fontenc} 
\usepackage{microtype}
\usepackage{inconsolata}
\usepackage[english]{babel}
\selectlanguage{english}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{tikz}
\usetikzlibrary{calc}
\begin{document}
Let $P_C$ and $C$ be the vertex and angle, respectively, opposite of the side $c$. Define the same for $a$ and $b$. Let $M$ be the center of mass, then that should be the balancing point, meaning the vector from $P_C$ to $M$ can be written as $s\begin{bmatrix}0\\-1\end{bmatrix}$ for some $s\in\mathbb{R}^+$. As $M$ is derived by splitting each side in two and drawing a line segment from center to the opposite point, we know that on either side of the mass we have half of $c$ and now this is just a question of how long it is when projected on to the $x$-axis.\\

If $a=b$, then $c$ is already projected on to the axis. Suppose that $a$ is the left side and is larger (if not, we can always rotate to reach this setup). In the following figure we are looking for $x$ and for each triangle, we need to extend our length by $2x$.
\begin{center}\begin{tikzpicture}[scale=.85, every node/.style={scale=1}]
\coordinate  (A) at (14,4);
\coordinate  (B) at (0,0);
\coordinate  (C) at (7,10);
\coordinate (MC) at (7,2);
\coordinate (M1) at (7,4);
\coordinate (M2) at (7,0);
\draw (B) -- (C) -- (A) -- (B); % Triange
\draw (A) node [below right] {$P_A$};
\draw (B) node [below left] {$P_B$};
\draw (C) node [above] {$P_C$};
\draw (C) -- (MC);
\draw [thick,dotted] (A) -- (M1) -- (MC) -- (A);
\draw [thick,dotted] (B) -- (M2) -- (MC) -- (B);
\draw ($ (A) !.5! (C) $) node[above right] {$b$};
\draw ($ (B) !.5! (C) $) node[above left] {$a$};
\draw ($ (B) !.5! (MC) $) node[above] {$c/2$};
\draw ($ (A) !.5! (MC) $) node[below] {$c/2$};
\draw ($ (A) !.5! (M1) $) node[above] {$x$};
\draw ($ (B) !.5! (M2) $) node[below] {$x$};
\draw ($ (C) !.5! (M1) $) node[left] {$y_1$};
\draw ($ (MC) !.5! (M1) $) node[left] {$y_2$};
\draw ($ (MC) !.5! (M2) $) node[right] {$y_2$};
% atan(diff_y/diff_x for A and B) is the angle where B starts...)
% ends with that + angle of b, needs cos rule for that
% Not to bothered to do this with formulas... for this explanation...
\draw (B)+({cos(15.9453959)},{sin(15.9453959)}) arc (15.9453959:55.5:1) node[right] {$B$};
\end{tikzpicture}\end{center}
By the law of cosine we have $b^2 = a^2+c^2 - 2ac\cos(B) \Rightarrow 2ac\cos(B) = a^2+c^2-b^2$ for the entire triangle and for the 'upper left sub-triangle' we have 
\begin{align*}
    (y_1+y_2)^2 = a^2+(c/2)^2 - 2ac\cos(B) = a^2+(c/2)^2 - (a^2+c^2-b^2) \Rightarrow y_1 + y_2 = \frac{\sqrt{2a^2+2b^2-c^2}}{2}.
\end{align*}
Using Pythagoras' theorem on the two 'right sub-triangles', we have $y_1^2 + x^2 = b^2$ and $y_2^2 + x^2 = (c/2)^2$ and thus
\begin{align*}
    b^2 - y_1^2 = (c/2)^2 - y_2^2 \Rightarrow y_1^2-y_2^2 = b^2-(c/2)^2 \Rightarrow y_1 = \sqrt{y_2^2 + b^2 - (c/2)^2}.
\end{align*}
By joining the two equations of $y_1$ and $y_2$ we get
\begin{align*}
    &y_1 + y_ 2 = \frac{\sqrt{2a^2+2b^2-c^2}}{2} \Rightarrow \sqrt{y_2^2 + b^2 - (c/2)^2} + y_2 = \frac{\sqrt{2a^2+2b^2-c^2}}{2} \\
    \Rightarrow &\sqrt{y_2^2 + b^2 - (c/2)^2} = \frac{\sqrt{2a^2+2b^2-c^2}}{2} - y_2 \Rightarrow y_2^2 + b^2 - (c/2)^2 = \left(\frac{\sqrt{2a^2+2b^2-c^2}}{2} - y_2\right)^2 \\
    \Rightarrow &b^2-(c/2)^2 = \frac{2a^2+2b^2-c^2}{4}-y_2\sqrt{2a^2+2b^2-c^2} \Rightarrow y_2 = \frac{\frac{2a^2+2b^2-c^2}{4}-b^2+(c/2)^2}{\sqrt{2a^2+2b^2-c^2}} \\
    \Rightarrow &y_2 = \frac{a^2-b^2}{2\sqrt{2a^2+2b^2-c^2}} \Rightarrow y_2^2 = \frac{(a^2-b^2)^2}{4(2a^2+2b^2-c^2)}
\end{align*}
and finally
\begin{align*}
    x^2+y_2^2 = (c/2)^2 \Rightarrow 2x = 2\sqrt{(c/2)^2-y_2^2} = \sqrt{c^{2} - \frac{(a^2-b^2)^2}{2a^2+2b^2-c^2}}.
\end{align*}
\end{document}

*/