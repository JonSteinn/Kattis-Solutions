# from wiki (https://en.wikipedia.org/wiki/Maximum_subarray_problem)
def max_sub_array(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


p = int(input().split()[1])
print(max_sub_array(list(map(lambda z: int(z) - p, input().split()))))
