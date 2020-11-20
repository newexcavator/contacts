import pymysql

class ConMysql:

    def __init__(self):
        super().__init__()

        self.conn = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            password = '123456',
            db = 'contacts',
            charset = 'utf8'
        )

        # self.cursor = conn.cursor()


    def search_single(self, name):
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM sys_user_info WHERE name = {}".format(name)
            cursor.execute(sql)
            res = cursor.fetchone()
        return res

    def search_all(self):
        with self.conn.cursor() as cursor:
            sql = "SELECT name, addr, phone FROM sys_user_info WHERE is_delete = 'N'"
            cursor.execute(sql)
            res = cursor.fetchall()
        return res

    def insert(self, name, addr, phone):
        with self.conn.cursor() as cursor:
            sql = "INSERT INTO sys_user_info(`name`, addr, phone, is_delete) VALUES ('{}', '{}', '{}', 'N')".format(name, addr, phone)
            cursor.execute(sql)
            self.conn.commit()

    def edit(self, name, addr, phone, old_name):
        with self.conn.cursor() as cursor:
            sql = "UPDATE sys_user_info SET name = '{}', addr = '{}', phone = '{}' WHERE name = '{}'".format(name, addr, phone, old_name)
            cursor.execute(sql)
            self.conn.commit()


    def delete(self, name):
        with self.conn.cursor() as cursor:
            sql = "UPDATE sys_user_info SET IS_DELETE = 'Y' WHERE name = '{}'".format(name)
            cursor.execute(sql)
            self.conn.commit()



if __name__ == "__main__":
    conmysql = ConMysql()
    # res = conmysql.search_single('002')
    # conmysql.insert('006', 'zsj', '66666666666')
    # conmysql.edit('0051', 'zsj1', '66666666661', '005')
    # conmysql.delete('0051')
    res = conmysql.search_all()
    print(res)
