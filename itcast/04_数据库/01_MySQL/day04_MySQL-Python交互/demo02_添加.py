import pymysql
# from mysql import connector


def query(sql, cursor):
    sid = input('查\tsid: ')
    cursor.execute(sql, (sid,))
    result = cursor.fetchone()
    return result


def main_pymysql():  # 测试pymysql
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           database='python3',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)  # 指定Cursor类
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO students (id, name, birthday) VALUES (0, %s, '2017-3-2')"  # 增, 预处理SQL语句, 占位符%s
            name = input('增\t姓名: ')
            cursor.execute(sql, (name,))

            r_sql = "SELECT * FROM students WHERE id = %s"  # 查
            result = query(r_sql, cursor)
            print(f'\t\t{result}')

            sql = "UPDATE students SET name = '加油!' WHERE id = %s"   # 改
            sid = input('改\tsid: ')
            cursor.execute(sql, (sid,))
            result = query(r_sql, cursor)
            print(f'\t\t{result}')

            sql = 'DELETE FROM students WHERE id = %s'   # 删
            sid = input('删\tsid: ')
            cursor.execute(sql, (sid,))

            # conn.commit()   # 提交事务
            conn.rollback()
    finally:
        conn.close()


# def main_mysql():   # 测试mysql
#     conn = connector.connect(host='localhost',
#                              user='root',
#                              password='',
#                              database='python3')
#     conn.close()  # 发送quit/exit, 并关闭socket


if __name__ == '__main__':
    main_pymysql()

    print('='*60)
    # main_mysql()


# 驱动
#   1.第三方
#     1.MySQLdb 不支持3.X
#     2.PyMySQL 支持各种版本Python ~ MySQLdb替代者
#       1.默认开启事务
#   2.MySQL官方
#     1.MySQL Connector/Python




























































