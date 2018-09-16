# lst = [1, 2]
#
#
# def main():
#     print(lst)
#
#
# if __name__ == '__main__':
#     main()

# print('\a')

# import turtle as t
#
# t.color('#0F0', '#F0F')
# t.begin_fill()
# while True:
#     t.forward(150)
#     t.left(230)
#     if abs(t.pos()) < 1:
#         break
# t.end_fill()
# t.done()


for i in range(20):
    for j in range(20):
        # 反斜杠
        # if i == j:
        #     print('*', end='')
        # elif i > j:
        #     print('-', end='')
        # else:
        #     print('^', end='')

        # 正斜杠
        # if i+j == 20:
        #     print('*', end='')
        # else:
        #     print(' ', end='')

        # 正反斜杠
        # if i == j or i + j == 19:
        #     print('¶', end='')
        #     print('¶', end='')
        #     print('¶', end='')
        #     print('¶', end='')
        # else:
        #     print(' ', end='')

        # ........
        if i == j*6 or i+j == 19:
            print('*', end='')
        else:
            print(' ', end='')
    print()


