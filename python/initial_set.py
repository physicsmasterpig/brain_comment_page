# ui구현은 나중에 하고 일단 콘솔로 입력하는 방식을 사용

import class_set

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
    class1 = class_set.classs(str(year) + "-" + str(semester) + "-" + str(school) + "-" + str(grade) + "-" + str(time))
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
    class1 = class_set.classes[0]
    cnt = 1
    for i in class_set.id_id:
        if "-" in i:
            j = i.split("-")[0]+'-'+i.split("-")[0]
            if j == str(school) + '-' + str(grade):
                cnt = cnt + 1
    student_no = cnt
    student = class_set.student(name, str(school) + "-" + str(grade) + "-" + str(student_no),class1)
    student.initial()


def student_delete():
    name = '이윤수'
    school = '경기북과학고'
    if school == '경기북과학고':
        school = 1
    elif school == '광주영재학교':
        school = 2
    else:
        school = 3
    grade = 20
    for i in range(len(students_name)):
        if students_name[i] == name and str(school) + "-" + str(grade) + "-" in students[i]:
            valid[i] = "i"
            break
    for i in range(len(students_name)):
        worksheet_id.update_cell(i + 1, 3, valid[i])


def student_valid():
    name = '이윤수'
    school = '경기북과학고'
    if school == '경기북과학고':
        school = 1
    elif school == '광주영재학교':
        school = 2
    else:
        school = 3
    grade = 20
    for i in range(len(students_name)):
        if students_name[i] == name and str(school) + "-" + str(grade) + "-" in students[i]:
            valid[i] = "v"
            break
    for i in range(len(students_name)):
        worksheet_id.update_cell(i + 1, 3, valid[i])


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
    class1 = class_set.classs(str(year) + "-" + str(semester) + "-" + str(school) + "-" + str(grade) + "-" + str(time),
                              'i')
    for i in range(len(students_name)):
        if classes_valid == class1.id:
            classes_valid[i] = "i"
            break
    for i in range(len(students_name)):
        worksheet_id.update_cell(i + 1, 6, classes_valid[i])


def link_stu_class(stu_id, class_id):
    a = 0
    for i in range(len(classes)):
        if classes[i] == class_id and classes_valid[i] == 0:
            return
        if classes[i] == class_id and classes_valid[i] == 1:
            a = a + 1
    if a != 1:
        return
    for i in range(len(students_link)):
        if students_link[i] == stu_id:
            worksheet_link.update_cell(i + 1, 2, class_id)
