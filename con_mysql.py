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

        self.cursor = conn.cursor()


    def search_single(self, name):
        sql = "SELECT * FROM sys_user_info WHERE name = {}".format(name)
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        return res

    def search_clus(self):
        sql = "SELECT * FROM sys_user_info"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def insert(self, name, addr, phone):
        sql = "INSERT INTO sys_user_info(`name`, addr, phone, is_delete) VALUES ({}, {}, {}, 'N')".format(name, addr, phone)
        self.cursor.execute(sql)

    def update(self, name, addr, phone, old_name):
        sql = "UPDATE sys_user_info SET name = {}, addr = {}, phone = {} WHERE name = {}})".format(name, addr, phone, old_name)
        self.cursor.execute(sql)

    def delete(self, name):
        sql = "UPDATE sys_user_info SET IS_DELETE = 'Y' WHERE name = {}})".format(name)
        self.cursor.execute(sql)

    def cloes_conn(self):
        cursor.close()
        conn.commit()
        conn.close()

if __name__ == "__main__":
    conmysql = ConMysql()
