class Student:
    def __init__(self, name, dept, mid, final):
        self.name = name
        self.dept = dept
        self.mid = mid
        self.final = final

    def __str__(self):
        return f'학과 : {self.dept}, 이름 : {self.name}, 중간 : {self.mid}, 기말 : {self.final}'

    def grade(self):
        avg = (self.mid + self.final) / 2

        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'


student = Student('김정철', '기계학과', 89, 90)

print(student)
print('학점 :', student.grade())
