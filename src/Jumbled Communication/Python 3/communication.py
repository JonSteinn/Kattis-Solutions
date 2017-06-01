def convert(byte):
    converted_byte = 0
    for i in range(0, 8):
        converted_byte |= ((byte ^ converted_byte) & 2 ** i) * 2
    return converted_byte // 2

input()  # dump
inp = input().split()
for b in inp[0:-1]:
    print(convert(int(b)), end=' ')
print(convert(int(inp[-1])))