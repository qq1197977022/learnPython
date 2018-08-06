import pymysql


class Utilities(object):
    single = True

    def __init__(self):
        # Note: 这里单例模式未完成------------------------------------------------------
        if self.single:  # 单例模式
            self.conn = pymysql.connect(host='localhost',
                                        user='root',
                                        password='',
                                        database='python3',
                                        charset='utf8',
                                        cursorclass=pymysql.cursors.DictCursor)
            self.cursor = self.conn.cursor()
            self.single = False

    def close(self):
        self.conn.commit()    # 提交事务
        self.cursor.close()    # 释放所有剩余数据
        self.conn.close()   # 发送quit/exit, 关闭socket连接

    def curd(self, sql, sql_params=None):
        try:
            self.cursor.execute(sql, sql_params)
        except Exception as e:
            print(e)
        # finally:
            # self.close()





























