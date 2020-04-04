def carry_eq_len(a,b):
    carry = 0
    carry_counter = 0
    for a,b in zip(a,b):
        z = carry+int(a)+int(b)
        if z > 9:
            carry = z // 10
            carry_counter += 1
        else:
            carry = 0
    return carry_counter

def carry(a,b):
    if len(a) < len(b):
        x = carry_eq_len(reversed(b), reversed('0' * (len(b)-len(a)) + a))
    elif len(b) < len(a):
        x = carry_eq_len(reversed(a), reversed('0' * (len(a)-len(b)) + b))
    else:
        x = carry_eq_len(reversed(a),reversed(b))
    if x == 0:
        return 'No carry operation.'
    elif x == 1:
        return '1 carry operation.'
    else:
        return f'{x} carry operations.'


def main():
    while True:
        a,b = input().split()
        if a == '0' and b == '0':
            break
        print(carry(a,b))

if __name__ == "__main__":
    main()