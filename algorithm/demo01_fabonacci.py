def recursion(n):
    if n < 2:
        return n
    else:
        return recursion(n-1) + recursion(n-2)


def no_recursion(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x+y
    return x


def main():
    for i in range(10):
        # print(no_recursion(i))
        print(recursion(i))


if __name__ == '__main__':
    main()
