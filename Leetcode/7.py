x = 1230
x = -12300000

def main():
    output = int(str(x if x > 0 else str(-x) + "-")[::-1])
    return output

print(main())