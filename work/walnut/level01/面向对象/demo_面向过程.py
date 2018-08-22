def start(name, option):
    print(f'{name} {option}')


def wash(name, option):
    print(f'{name} {option}')


def close(name, option):
    print(f'{name} {option}')


def eat(name, option):
    print(f'{name} {option}')


def eatApple_processOriented(): # 不符合PEP8规范
    start(name='小明', option='打开水龙头')
    wash(name='小明', option='洗刷刷')
    close(name='小明', option='关闭水龙头')
    eat(name='小明', option='吃苹果')


if __name__ == '__main__':
    eatApple_processOriented()


