class Member:
    def __init__(self, no, user_id, password, name, phone, address):
        self.no = no
        self.user_id = user_id
        self.password = password
        self.name = name
        self.phone = phone
        self.address = address

    def __str__(self):
        return f'{self.no}\t{self.user_id}\t{self.name}\t{self.phone}\t{self.address}'


class MemberService:
    def __init__(self):
        self.member_list = []

    def join(self, member):
        self.member_list.append(member)

    def list_member(self):
        return self.member_list

    def detail_member(self, user_id):
        for member in self.member_list:
            if member.user_id == user_id:
                return member
        return None

    def update_member(self, user_id, phone, address):
        member = self.detail_member(user_id)

        if member is not None:
            member.phone = phone
            member.address = address
            return True

        return False

    def delete_member(self, user_id):
        member = self.detail_member(user_id)

        if member is not None:
            self.member_list.remove(member)
            return True

        return False


def select_menu():
    print('================================================')
    print('1.회원가입 2.회원목록 3.회원상세 4.정보수정 5.회원탈퇴 0.종료')
    print('================================================')
    return int(input('>> 메뉴 선택 : '))


service = MemberService()

while True:
    menu = select_menu()

    if menu == 0:
        break

    elif menu == 1:
        print('------------ 회원가입 ------------')

        no = input('회원번호 : ')
        user_id = input('아이디 : ')
        password = input('비밀번호 : ')
        name = input('이름 : ')
        phone = input('전화번호 : ')
        address = input('주소 : ')

        member = Member(no, user_id, password, name, phone, address)

        service.join(member)

        print('회원가입 완료')

    elif menu == 2:
        print('------------ 회원목록 ------------')

        member_list = service.list_member()

        for member in member_list:
            print(member)

    elif menu == 3:
        print('------------ 회원상세 ------------')

        user_id = input('아이디 입력 : ')

        member = service.detail_member(user_id)

        if member is not None:
            print(member)
        else:
            print('회원이 존재하지 않습니다.')

    elif menu == 4:
        print('------------ 정보수정 ------------')

        user_id = input('아이디 입력 : ')
        phone = input('새 전화번호 : ')
        address = input('새 주소 : ')

        if service.update_member(user_id, phone, address):
            print('회원정보 수정 완료')
        else:
            print('회원이 존재하지 않습니다.')

    elif menu == 5:
        print('------------ 회원탈퇴 ------------')

        user_id = input('아이디 입력 : ')

        if service.delete_member(user_id):
            print('회원탈퇴 완료')
        else:
            print('회원이 존재하지 않습니다.')

print('프로그램 종료')
