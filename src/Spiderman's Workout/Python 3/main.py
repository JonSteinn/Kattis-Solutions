def climb(i, h, heights, memory):
    # Base case
    # Only valid if ends with D => least significant bit set => odd
    if i == len(heights)-1:
        if h - heights[i] == 0:
            return 0, 1
        else:
            return 0, 0

    if (h,i) not in memory:
        # Dive
        up_max_h, up_bits = climb(i+1,h+heights[i],heights,memory)
        down_max_h, down_bits = up_max_h+1, 0
        if h >= heights[i]:
            down_max_h, down_bits = climb(i+1,h-heights[i],heights,memory)

        # Check which are valid
        if up_bits&1 and down_bits&1:
            if up_max_h < down_max_h: 
                memory[(h,i)] = max(h, up_max_h), up_bits 
            else:
                memory[(h,i)] = max(h, down_max_h), down_bits | (1 << (len(heights)-1-i))
        elif up_bits&1:
            memory[(h,i)] = max(h, up_max_h), up_bits 
        elif down_bits&1:
            memory[(h,i)] = max(h, down_max_h), down_bits | (1 << (len(heights)-1-i))
        else:
            memory[(h,i)] = 0,0


    return memory[(h,i)]

def test_case(n, heights):
    _,z = climb(0, 0, heights,{})
    if z&1:
        print(''.join('U' if b == '0' else 'D' for b in (lambda bstr: f"{'0'*(len(heights)-len(bstr))}{bstr}")(bin(z)[2:])))
    else:
        print('IMPOSSIBLE')

def main():
    for _ in range(int(input())):
        test_case(int(input()), list(map(int,input().split())))

if __name__ == "__main__":
    main()