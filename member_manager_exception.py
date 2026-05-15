class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

member_list = []

while True:
    try:
        menu = int(input('1.추가 2.조회 3.삭제 0.종료 : '))

        if menu == 1:
            name = input('이름 : ')

            try:
                age = int(input('나이 : '))
            except ValueError:
                print('나이는 숫자로 입력하세요.')
                continue

            member = Member(name, age)
            member_list.append(member)
            print('회원 추가 완료')

        elif menu == 2:
            if len(member_list) == 0:
                print('회원 정보가 없습니다.')
            else:
                for m in member_list:
                    print(m.name, m.age)

        elif menu == 3:
            name = input('삭제할 이름 : ')
            found = False

            for m in member_list:
                if m.name == name:
                    member_list.remove(m)
                    found = True
                    print('삭제 완료')
                    break

            if not found:
                print('해당 회원이 없습니다.')

        elif menu == 0:
            print('프로그램 종료')
            break

        else:
            print('메뉴를 다시 입력하세요.')

    except ValueError:
        print('숫자를 입력하세요.')