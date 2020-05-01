"""
Combinatorics:
How many binary strings of length n are palindrome?

Remark:
The problem regards a single 0 as an invalid number because they disregard leading zeros. Generally,
I would make an exceptino for a single 0. Also, the empty binary string is a palindrome. Taking that
into account, I'd say 1 is the third binary string palindrome. The problem maps 1 to 1 so we will
disregard the first two as well.

Let pb(n) be the number of palindrome binary strings of length n. A palindrome binary string (not
including 0 end the empty string) is either 1, 11 or starts and end with 1 (and they being two different
positions of the string) and has some elements between them. Suppose b = b_1b_2...b_n for some n>2, then
b_1 = b_n = 1 and half (including the odd element in an odd case) of the remaining can take any value,
with the remainign needing to mirror them. If n is even, there are (n-2)/2 elements free to take any value
and if n is odd, then (n-1)/2 elements can take any possible value. Therefore
pb(n) = {
    1 if n == 1 or n == 1
    (n-2)/2 if n % 2 == 0
    (n-1)/2 if n % 2 == 1 [otherwise]
}

Now we can find how many palindrome strings have length less than or equal to n with the sum
spb(n) = sum_{i=1}^n pb(i). Suppose we are looking for the r-th palindrome and k is the first
value such that spb(k) exceeds or equals r, then we know that the binary string must be of
length k. Further more, we can use those accumulated sum to find the j-th palindrome of length
k rather then the n-th of any length.

Odd case:
1 b_2 b_3 ... b_{c-1} b_c b_{c+1} ... b_{k-1} 1
Suppose we need the j-th palindrome of length k, then we can turn b_2 b_3 ... b_c into the
binary representation of j and left pad it, then reverse it to fill the right half (not including b_c).

Even case:
Same but no b_c and the reversing take all of the left half.
"""

class BinaryPalindrome:
    @staticmethod
    def length_kth(n):
        accumulated_counts = [1]
        while n > accumulated_counts[-1]:
            accumulated_counts.append(accumulated_counts[-1] + (lambda l: 2**((l-1)//2 if l%2 else (l-2)//2))(len(accumulated_counts)+1))
        return len(accumulated_counts), 0 if n == 1 else n-accumulated_counts[-2]-1

    @staticmethod
    def nth_bin_palindrome(n):
        if n < 3:
            return int('1'*n, base=2)
        l,k = BinaryPalindrome.length_kth(n)
        if l % 2 == 0:
            return (lambda _b: int(f'1{_b}{_b[::-1]}1', base=2))((lambda b: ((l-2)//2 - len(b)) * '0' + b)(bin(k)[2:]))
        else:
            return (lambda _b: int(f'1{_b}{_b[:-1][::-1]}1', base=2))((lambda b: ((l-1)//2 - len(b)) * '0' + b)(bin(k)[2:]))

print(BinaryPalindrome.nth_bin_palindrome(int(input())))