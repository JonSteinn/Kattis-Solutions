"""
Suppose we have two shafts a and b, where a<b, then the points 
between them where its equally good to go both ways is 
(b*(1+r)+a*(1-r))/2 where r = h/w.

Given values a and b (a<b) of shaft positions, the cost of bringing 
the dirt up is
    (m-a+r*a)^2/2 + (b-m+r*b)^2/2
where m = (b*(1+r)+a*(1-r))/2. Note however when we are summing over
all such regions (defined by a and b), we are counting the vertical
distance of each shaft twice and thus, the cost of each shaft's
vertical distance must be subtracted from the rest.

Take three consecutive shafts a,b and c and suppose a and c are fixed.
How can we pick b to minimize cost? In the total cost function, all 
terms that invovle b are in these two regions as well as the subtracting
height of the shaft to accommodate the double counting. Let m1 and m2
be the cost balancing point of each region, then we have a total cost
of everything going through b's shaft as:
    cost(b) = (m1-a+r*a)^2/2 +(b-tm+r*b)^2/2 + (m2-b+r*b)^2/2 + (c-m2+r*c)^2/2 - (r*b)^2/2
Note that both m1 and m2 are functions of b. Now that we have everything
involving b, with regards to the total cost, we can find an extreme point
by solving the derivative of cost(b) w.r.t. b being equal to 0. This yiels
b = (a+c)*(1-r^2)/2

Let z = (1-r^2)/2. We now have a system of equations
x1 = x2*z
x2 = (x1+x3)*z
...
xn = (x_[n-1] + W)*z

If we start solving iteratively for x_n, we find a pattern as a continued fraction.
I did this with Sage using the following code:
    c,w=var('c,w')
    def solve_n(n):
        mat = [[1,-c] + [0]*(n-2)]
        for i in range(n-2):
            mat.append([0]*i + [-c,1,-c] + [0]*(n-3-i))
        mat.append([0]*(n-2) + [-c,1])
        return matrix(mat).solve_right(matrix([[0]*(n-1)+[w*c]]).transpose())[n-1][0]
    for i in range(2,10):
        solve_n(i)
which yielded the following results:
    -c*w/(c^2 - 1)
    c*w/(c^2/(c^2 - 1) + 1)
    -c*w/(c^2/(c^2/(c^2 - 1) + 1) - 1)
    c*w/(c^2/(c^2/(c^2/(c^2 - 1) + 1) - 1) + 1)
    -c*w/(c^2/(c^2/(c^2/(c^2/(c^2 - 1) + 1) - 1) + 1) - 1)
    c*w/(c^2/(c^2/(c^2/(c^2/(c^2/(c^2 - 1) + 1) - 1) + 1) - 1) + 1)
    -c*w/(c^2/(c^2/(c^2/(c^2/(c^2/(c^2/(c^2 - 1) + 1) - 1) + 1) - 1) + 1) - 1)
    c*w/(c^2/(c^2/(c^2/(c^2/(c^2/(c^2/(c^2/(c^2 - 1) + 1) - 1) + 1) - 1) + 1) - 1) + 1)

Knowing the last coordinates, we can then find the second to last and so on,
using our system of equations. This way we fill all x coordinates and finally
calculate the cost.
"""

def get_last(w,n,r,z):
    zsq = z**2
    total = 1.0
    for i in range(n-1):
        total = zsq/total + (1 if i&1 else -1)
    return abs(w*z/total)

def cost(x1,x2,r):
    split = (x2*(1+r)+x1*(1-r))/2
    return ((x2 - split + r*x2)**2 + (split - x1 + r*x1)**2)/2

def get_xs(n,w,r):
    z = (1.0-r**2)/2.0
    xs = [0]*(n+2)
    xs[-1] = w
    xs[-2] = get_last(w,n,r,z)
    for i in range(n-1,0,-1):
        xs[i] = xs[i+1]/z - xs[i+2]
    return xs

def get_cost(n,r,xs):
    c = 0.0
    for i in range(n+1):
        c += cost(xs[i],xs[i+1],r)
    for i in range(1,n+1):
        c -= (r*xs[i])**2/2
    return c

def print_xs(xs):
    if len(xs) > 12:
        for i in range(1,11):
            print('%.4f' % xs[i])
    else:
        for x in xs[1:-1]:
            print('%.4f' % x)

def main():
    w,h,n = map(int,input().split())
    r = h/w
    xs = get_xs(n,w,r)
    print('%.4f' % get_cost(n,r,xs))
    print_xs(xs)

if __name__ == "__main__":
    main()