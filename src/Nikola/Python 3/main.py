class State(tuple):
    def __new__(cls, last, square):
        return tuple.__new__(cls, (last,square))

    def transition(self,n):
        l,s = self
        if s+l+1 <= n:
            yield State(l+1,s+l+1)
        if l > 0 and s-l > 0:
            yield State(l, s-l)

def travel(state, data):
    memory, n, cost = data
    if state[1] == n:
        return 0
    if state not in memory:
        c = 2147483647
        for t_state in state.transition(n):
            c = min(c, cost[t_state[1]-1] + travel(t_state, data))
        memory[state] = c
    return memory[state]

def main():
    n = int(input())
    cost = [int(input()) for _ in range(n)]
    print(travel(State(0,1), ({}, n, cost)))

if __name__ == "__main__":
    main()