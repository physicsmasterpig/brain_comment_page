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
    for i in func.id_class:
        if (str(year) + "-" + str(semester) + "-" + str(school) + "-" + str(grade) + "-") in i:
            time = time + 1
    perweek = 2
    day = [5, 6]
    daytime = [13, 19]
    first = [2024, 5, 26]
    class1 = func.classs(str(year) + "-" + str(semester) + "-" + str(school) + "-" + str(grade) + "-" + str(time))
    class1.perweek = perweek
    class1.day = day
    class1.daytime = daytime
    class1.first = func.plusdate(first[0], first[1], first[2], -func.whichday(first[0], first[1], first[2]))
    class1.initial()
    return class1.id


def student_submit(class1):
    name = input('name?')
    if name == '0':
        return 1
    student_no = input('phone number?(without -)')
    student_no = student_no.replace('010', '')
    if class1 == 0:
        class1 = input('class?')
    if class1 not in func.classes.keys():
        print("invalid class")
        return
    else:
        if func.classes[class1].valid == "i":
            print("invalid class")
            return
    student = func.student(name, str(func.classes[class1].school) + "-" + str(func.classes[class1].grade) + "-" + str(
        student_no), class1)
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


def student_change(student, classs):
    if student == 0:
        student = input('student?')
    if classs == 0:
        classs = input('class?')
    if student not in func.students.keys():
        print("invalid student")
        return
    else:
        if func.students[student].valid == 'i':
            print("invalid student")
            return
    if classs not in func.classes.keys():
        print("invalid class")
        return
    else:
        if func.classes[classs].valid == "i":
            print("invalid class")
            return
    func.students[student].change(classs)


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


def all_new_students(classs):
    if classs == 0:
        classs = input('class?')
    if classs in func.classes.keys():
        if func.classes[classs].valid == 'i':
            print('invalid class')
            return
    else:
        print('invalid class')
        return
    a = 0
    print("if you want to stop, input 0 at name")
    while (a != 1):
        a = student_submit(classs)


def all_change_class():
    initclass = input('initial class?')
    classs = input('final class?')
    if classs in func.classes.keys():
        if func.classes[classs].valid == 'i':
            print('invalid class')
            return
    else:
        print('invalid class')
        return
    if initclass in func.classes.keys():
        if func.classes[initclass].valid == 'i':
            print('invalid class')
            return
    else:
        print('invalid class')
        return
    students = func.classes[initclass].students
    for i in students:
        student_change(i, classs)
