from con_mysql import ConMysql

class Contacts():

    def __init__(self):
        super().__init__()
        self.contacts = [
            {'num':'1', 'name': '001', 'addr': 'zsj', 'phone': '11111111111'},
            {'num':'2', 'name': '002', 'addr': 'zsj', 'phone': '22222222222'},
            {'num':'3', 'name': '003', 'addr': 'zsj', 'phone': '33333333333'}
        ]

    def createUser(self, num, name, addr, phone):
        personInfo = {'num':num, 'name':name, 'addr':addr, 'phone':phone}
        self.contacts.append(personInfo)

    def listAll(self):
        for person in self.contacts:
            print(person)

    def queryPerson(self, name):
        for person in self.contacts:
            if name == person['name']:
                print(person)

    def deletePerson(self, name):
        for person in self.contacts:
            if name == person['name']:
                self.contacts.remove(person)

    def editPerson(self, num, name, addr, phone):
        for person in self.contacts:
            if num == person['num']:
                self.contacts[int(num) - 1]['name'] = name
                self.contacts[int(num) - 1]['addr'] = addr
                self.contacts[int(num) - 1]['phone'] = phone

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
            contacts.createUser(str(num), name, addr, phone)
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
            num = input("请输入需要编辑的人员编号（num）：")
            print("请输入修改后的人员信息")
            name = input("姓名：")
            addr = input("地址：")
            phone = input("手机号码：")
            contacts.editPerson(num, name, addr, phone)    
        elif inp == 6:
            print("------------------退出通讯录------------------")
            break
