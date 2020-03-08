"""
Suppose we are looking at a node X with a left children and b right
children, a total of a+b children. All the a left children are smaller
than X while the b right children are larger. For a specific left child,
it does not matter when it is inserted relative to any of the right
children since they won't affect each oter. All that matters is that
the left children are inserted in the same order relative to each other
and the same for the right ones. We can now think of the order of
insertions as a binary string of length a+b with a 1s, where a 1 means
that the next left child is inserted next and 0 means the next right
child is inserted next. For example, 11010 gives the insertion order
LLRLR with 3 elements to the left of X and two to the right. How many
binary strings of length a+b have a 1s? binom(a+b,a)
"""

binom_mem = [[0 for k in range(n+1)] for n in range(101)]
for n in range(101):
    for k in range(n+1):
        if k == 0 or n == k:
            binom_mem[n][k] = 1
        else:
            binom_mem[n][k] = binom_mem[n-1][k-1] + binom_mem[n-1][k]

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.children = 0

class BST:
    def __init__(self):
        self.root = None

    def insert(self, x):
        self.root = self.__insert(self.root, x)

    def __insert(self, node, x):
        if node is None:
            return Node(x)
        node.children += 1
        if x < node.value:
            node.left = self.__insert(node.left, x)
        else:
            node.right = self.__insert(node.right, x)
        return node

    def count(self):
        return self.__count(self.root)

    def __count(self, node):
        return 1 if node is None else (lambda a,b: binom_mem[a+b][b])((0 if node.right is None else node.right.children + 1), (0 if node.left is None else node.left.children + 1)) * self.__count(node.left) * self.__count(node.right)

def test_case(insertion):
    bst = BST()
    for x in insertion:
        bst.insert(x)
    print(bst.count())

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        test_case(map(int, input().split()))

if __name__ == "__main__":
    main()