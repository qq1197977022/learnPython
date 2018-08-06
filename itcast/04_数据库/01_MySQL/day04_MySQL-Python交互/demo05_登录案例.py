from demo04_Utilities import Utilities
import hashlib


def get():
    name = input('name: ')
    password = input('password: ')
    return name, password


def register(utils):
    print(f'{"注册":-^60}')
    name, password = get()

    sha1 = hashlib.new('sha1')      # 密文存储
    sha1.update(password.encode())
    password = sha1.hexdigest()

    sql = 'INSERT INTO user (id, name, pwd) VALUES (0, %s, %s)'
    sql_params = (name, password)
    utils.curd(sql, sql_params)


def login(utils):
    print(f'{"登录":-^60}')
    name, password = get()

    sha1 = hashlib.new('sha1')  # 密文对比
    sha1.update(password.encode())
    password = sha1.hexdigest()

    sql = 'SELECT pwd FROM user WHERE name = %s'
    utils.curd(sql, (name,))
    row = utils.cursor.fetchone()
    if row is None:
        print(f'{"用户名错误":->60}')
        return
    pwd = row['pwd']
    if password != pwd:
        print(f'{"密码错误":*^60}')
    else:
        print(f'{"登录成功":=^60}')


def main():
    utils = Utilities()

    # register(utils)     # 注册
    login(utils)        # 登录
    utils.close()


if __name__ == '__main__':
    main()


