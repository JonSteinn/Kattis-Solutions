"""
Let _ determine an arbitrary value in our q-binary string. 
Suppose we have a q-binary string q1q2...q_n and we arrive
at a 1, while traversing the string in reverse order.
    <some string> 1 <some string with a zeros and b question marks>
Foreach zero to its right, there is an inversion for every binary
string generated (each for one question mark) so the inversions here
are a * 2**b. For the question mark, there are (b choose i) with i
zeros and for each of them we have i inversions, a total of
sum((b choose i) * i, i in {1,2,...,n}) = b * 2**(b-1) (exception
being when there are no question marks, then this value is 0).
Now this single 1 has counted for a*2**b + b*2**(b-1) inversion
for all strings generated but for any question marks to its left,
we have to count all these again which is what we do if we arrive
at a question mark. We first multiply the current total with 2
since the new question mark produces two new strings for every
existing string counted, all with those old inversions. Then we
treat the question mark as a one and repeat the process we already
did. Along the traversing way, we count the 0 to produce those
values and at each step, apply the modulus to prevent the total
becoming to large.
"""


MOD = 10**9+7
MEM = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

def mod_pow2(n):
    while n >= len(MEM):
        MEM.append((MEM[-1] * 2) % MOD)
    return MEM[n]

def inversions(bstr):
    total, zeros, questions = (0,)*3
    for x in reversed(bstr):
        if x == '1':
            z = zeros * mod_pow2(questions)
            q = 0 if questions == 0 else questions * mod_pow2(questions-1)
            total = (total + z + q) % MOD
        elif x == '0':
            zeros += 1
        else:
            total *= 2
            z = zeros * mod_pow2(questions)
            q = 0 if questions == 0 else questions * mod_pow2(questions-1)
            total = (total + z + q) % MOD
            questions += 1
            
    return total

def main():
    print(inversions(input()))

if __name__ == "__main__":
    main()

    




    

