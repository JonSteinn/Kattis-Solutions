from math import ceil

def main():
    n=int(input())
    init = ceil(n**(1/3))
    if init**3 > n:
        init -= 1
    found = set()
    largest = -1

    for i in range(1,init+1):
        for j in range(i,init+1):
            cube_sum = i**3 + j**3
            if cube_sum <= n:
                if cube_sum in found:
                    if cube_sum > largest:
                        largest = cube_sum
                else:
                    found.add(cube_sum)
            else:
                break
    print('none' if largest == -1 else largest)


if __name__ == "__main__":
    main()