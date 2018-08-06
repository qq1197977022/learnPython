from demo04_Utilities import Utilities


def ins(utils):
    sql = "INSERT INTO students (id, name, birthday) VALUES (%s, %s, '2017-3-2')"
    sid = input('sid: ')
    name = input('name: ')
    sql_params = (sid, name)
    utils.curd(sql, sql_params)


def fetchone(utils):
    # sql = 'SELECT * FROM students WHERE gender = %s AND id = %s'
    # sid = input('sid: ')
    # gender = input('gender: ')
    # sql_params = (gender, sid)
    # utils.curd(sql, sql_params)

    sql = 'SELECT * FROM students WHERE id = 15'
    utils.curd(sql)
    row = utils.cursor.fetchone()
    print(row)
    print(row['id'])
    print(row['name'])
    print(row['gender'])
    print(row['birthday'])
    print(row['isDel'])


def fetchall(utils):
    sql = 'SELECT * FROM students'
    utils.curd(sql)
    row_lst = utils.cursor.fetchall()
    for row in row_lst:
        print(row)


def main():
    utils = Utilities()
    # ins(utils)
    fetchone(utils)
    # fetchall(utils)

    # utils.close()


if __name__ == '__main__':
    main()










































