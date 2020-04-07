from itertools import chain 

class Ambiguous(Exception):
    pass

def solution_to_gen(solution):
    return (i for i in chain(*([i+1]*x for i,x in enumerate(solution))))

def find(costs, i, n, order, solutions, mem, curr):
    # Order found 
    if order == 0:
        if not solutions:
            solutions.append(curr.copy())
            return
        else:
            raise Ambiguous()

    # Last item on menu
    if i == n-1:
        if costs[i] <= order and order % costs[i] == 0:
            if not solutions:
                curr.append(order // costs[i])
                solutions.append(curr.copy())
                curr.pop()
            else:
                raise Ambiguous()
        return

    # Known dead end
    if (i,order) in mem:
        return

    # Search recursively
    before=len(solutions)
    for count in range(order//costs[i] + 1):
        curr.append(count)
        find(costs, i+1, n, order - count*costs[i], solutions, mem, curr)
        curr.pop()
    after=len(solutions)

    # Didn't find a solution
    if before == after:
        mem.add((i,order))

def find_items(costs, n, order, memory):
    try:
        solutions = []
        find(costs, 0, n, order, solutions, memory, list())
        if not solutions:
            return ('Impossible',)
        else:
            return solution_to_gen(solutions[0])
    except Ambiguous:
        return ('Ambiguous',)

def main():
    n = int(input())
    costs = list(map(int,input().split()))
    _ = input()
    memory = set()
    for i in map(int, input().split()):
        print(*find_items(costs, n, i, memory))

if __name__ == "__main__":
    main()