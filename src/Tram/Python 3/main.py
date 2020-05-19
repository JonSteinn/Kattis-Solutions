"""
We are minimizing the sum of distances to a line L: x-y+a=0.

Given a point P_i = (x_i,y_i), its distance to L is
    d(P_i,L) = abs(x_i-y_i+a) / sqrt(2)
and the total cost is sum(d(P_i,L), i = 1,...,n). We want
to minimize this cost function. Minimizing a distace is
the same as minimizing its square, that is
    d(P_i,L)^2 = (x_i-y_i+a)^2 / 2
and we have the cost function for our set of points,
    C(a) = (x_1-y_1+a)^2 / 2 + (x_2-y_2+a)^2 / 2 + ... + (x_n-y_n+a)^2 / 2.

This function is unimodal so the zero of its derivative w.r.t. a will give
a global optimum, that is
   diff(C(a),a) = (x_1-y_1+a)+(x_2-y_2+a)+...+(x_n-y_n+a) = sum(x_i-y_i,i=1...n) + n*a = 0
=> n*a = -sum(x_i-y_i,i=1...n) = sum(y_i-x_i,i=1...n)
=> a = sum(y_i-x_i,i=1...n)/n
"""

def main():
    n = int(input())
    s = 0
    for _ in range(n):
        x,y = map(int,input().split())
        s += y-x
    print('%.3f' % (s/n))
    
if __name__ == "__main__":
    main()