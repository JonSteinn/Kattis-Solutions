def print_order(count):
    for i,c in enumerate(count):
        print(f'Make {c} digit {i}')
    total = sum(count)
    end = '' if total == 1 else 's'
    print(f'In total {total} digit{end}')

def order(street):
    if street is None:
        street = input()
    print(street)
    print(input())
    count = [0]*10
    while True:
        try:
            order = input()
            if len(order) >= 2 and order[0] == '+' and order[1] == ' ':                
                for d in range(*(lambda z: (int(z[1]), int(z[2])+1, int(z[3])))(order.split())):
                    for c in str(d):
                        count[int(c)] += 1
            elif order.isdigit():
                for c in order:
                    count[int(c)] += 1
            else:
                print_order(count)
                return order
        except EOFError:
            print_order(count)
            return None


def main():
    input()
    next_order = None
    while True:
        next_order = order(next_order)
        if next_order is None:
            break

if __name__ == "__main__":
    main()