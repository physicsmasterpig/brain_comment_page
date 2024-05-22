# ui구현은 나중에 하고 일단 콘솔로 입력하는 방식을 사용

import func


def class_submit():
    year = 2024
    semester = 1
    school = '경기북과학고'
    if school == '경기북과학고':
        school = 1
    elif school == '광주영재학교':
        school = 2
    else:
        school = 3
    grade = 20
    time = 1
    class1 = func.classs(str(year) + "-" + str(semester) + "-" + str(school) + "-" + str(grade) + "-" + str(time))
    class1.initial()


def student_submit():
    name = '이윤수'
    school = '경기북과학고'
    if school == '경기북과학고':
        school = 1
    elif school == '광주영재학교':
        school = 2
    else:
        school = 3
    grade = 20
    class1 = func.classes[list(func.classes.keys())[0]].id
    student_no = 12345687
    student = func.student(name, str(school) + "-" + str(grade) + "-" + str(student_no), class1)
    student.initial()


def student_delete():
    school = '경기북과학고'
    if school == '경기북과학고':
        school = 1
    elif school == '광주영재학교':
        school = 2
    else:
        school = 3
    grade = 20
    student_no = 12345678
    id = str(school) + "-" + str(grade) + "-" + str(student_no)
    func.students[id].invalid()


def class_delete():
    year = 2024
    semester = 1
    school = '경기북과학고'
    if school == '경기북과학고':
        school = 1
    elif school == '광주영재학교':
        school = 2
    else:
        school = 3
    grade = 20
    time = 1
    id = str(year) + "-" + str(semester) + "-" + str(school) + "-" + str(grade) + "-" + str(time)
    if len(func.classes[id].students) == 0:
        func.classes[id].invalid()
    else:
        print("ERROR: Student in class")
