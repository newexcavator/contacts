import pymysql

class Contacts():

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

    def createUser(self, name, addr, phone):
        with self.conn.cursor() as cursor:
            sql = "INSERT INTO sys_user_info(`name`, addr, phone, is_delete) VALUES ('{}', '{}', '{}', 'N')".format(name, addr, phone)
            cursor.execute(sql)
            self.conn.commit()

    def listAll(self):
        with self.conn.cursor() as cursor:
            sql = "SELECT name, addr, phone FROM sys_user_info WHERE is_delete = 'N'"
            cursor.execute(sql)
            res = cursor.fetchall()
        
        for person in res:
            print(person)

    def queryPerson(self, name):
        with self.conn.cursor() as cursor:
            sql = "SELECT name, addr, phone  FROM sys_user_info WHERE name = {}".format(name)
            cursor.execute(sql)
            res = cursor.fetchone()
        print(res)

    def deletePerson(self, name):
        with self.conn.cursor() as cursor:
            sql = "UPDATE sys_user_info SET IS_DELETE = 'Y' WHERE name = '{}'".format(name)
            cursor.execute(sql)
            self.conn.commit()

    def editPerson(self, name, addr, phone, old_name):
        with self.conn.cursor() as cursor:
            sql = "UPDATE sys_user_info SET name = '{}', addr = '{}', phone = '{}' WHERE name = '{}'".format(name, addr, phone, old_name)
            cursor.execute(sql)
            self.conn.commit()

if __name__ == "__main__":

    contacts = Contacts()

    num = 4

    while True:

        print (
            """
                1. create person
                2. list all persons
                3. query person
                4. delete person
                5. edit person
                6. quit
            """
        )

        inp = int(input("Enter a number(1-6):"))
        
        if inp == 1:
            print("------------------请输入用户信息------------------")
            name = input("姓名：")
            addr = input("地址：")
            phone = input("手机号码：")
            contacts.createUser(name, addr, phone)
            print("添加成功!")
            contacts.listAll()
            num = num + 1
        elif inp == 2:
            print("------------------通讯录总揽------------------")
            contacts.listAll()
        elif inp == 3:
            print("------------------查询人员信息------------------")
            name = input("请输入人员姓名进行查询：")
            contacts.queryPerson(name)
        elif inp == 4:
            print("------------------删除人员------------------")
            name = input("请输入需要删除的人员姓名：")
            contacts.deletePerson(name)
        elif inp == 5:
            print("------------------编辑人员------------------")
            print("通讯录总揽")
            old_name = input("请输入需要编辑的人员姓名：")
            print("请输入修改后的人员信息")
            name = input("姓名：")
            addr = input("地址：")
            phone = input("手机号码：")
            contacts.editPerson(name, addr, phone, old_name)    
        elif inp == 6:
            print("------------------退出通讯录------------------")
            break
