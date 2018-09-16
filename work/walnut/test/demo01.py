def demo_for():
    for i in range(2, 10):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)


def demo_while():
    n = 10
    while n >= 2:
        tmp = 2
        while tmp < n:
            if n % tmp == 0:
                break
            else:
                tmp += 1
        else:
            print(n)
        n -= 1


def main():
    # demo_for()
    demo_while()


if __name__ == '__main__':
    main()
