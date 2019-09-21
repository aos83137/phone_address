
#연락처 프로그램
class Contact:
    # 이름, 전화번호, 이메일, 주소
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Addr: ", self.addr)

def get_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def print_menu():
    print("1, 연락처 입력")
    print("2, 연락처 출력")
    print("3, 연락처 삭제")
    print("4, 종료")
    menu = input("메뉴선택: ")
    return int(menu)

def set_contact():
    name=input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("addr: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact

def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

def store_contact(contact_list):
    f = open("contact_db.txt", "wt")
    for contact in contact_list:
        f.write(contact.name+'\n')
        f.write(contact.phone_number+'\n')
        f.write(contact.e_mail+'\n')
        f.write(contact.addr+'\n')
    f.close()

def run():
    kim = Contact('전용석', '010-7224-9221', 'aos31323@naver.com', 'Seoul')
    kim.print_info()
    contact_list = []
    # set_contact()
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            get_contact(contact_list)
        elif menu == 3:
            name = input("삭제할 이름을 입력하세요: ")
            delete_contact(contact_list, name)
        elif menu == 4:
            print("프로그램을 종료합니다.")
            store_contact(contact_list)
            break;

if __name__ == "__main__":
    run()