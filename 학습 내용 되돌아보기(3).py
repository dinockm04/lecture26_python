class Student:
    def info(self):
        print('대학 : ' + self.univ + ' 이름 : ' + self.name)

student = Student()

student.name = '추경민'
student.univ = '폴리텍대학교'

student.info()
