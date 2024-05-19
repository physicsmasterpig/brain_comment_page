# ui구현은 나중에 하고 일단 콘솔로 입력하는 방식을 사용

import gspread
import initial
from oauth2client.service_account import ServiceAccountCredentials

scope = 'https://spreadsheets.google.com/feeds'
json = 'python\driven-catalyst-411908-9c041a7750dd.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)
gc = gspread.authorize(credentials)
sheet_url = 'https://docs.google.com/spreadsheets/d/1-xp3axKvBFVAMDt0SpnW1oxtPH9lzlgSvEN-WZna2H0/edit#gid=0'
doc = gc.open_by_url(sheet_url)
worksheet_id = doc.worksheet('ID')
worksheet_link = doc.worksheet('link')

students = worksheet_id.col_values(1)
students_link = worksheet_link.col_values(1)
students_name = worksheet_id.col_values(2)
valid = worksheet_id.col_values(3)
classes = worksheet_id.col_values(5)
classes_valid = worksheet_id.col_values(6)


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
    class1 = initial.classs(year, semester, school, grade, time)
    for i in classes:
        if i == class1.id:
            return
    classes.append(class1.id)
    classes_valid.append(1)
    class1.initial(classes, classes_valid)


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
    class1 = classes[1]
    cnt = 1
    for i in worksheet_id.col_values(1):
        if "-" in i:
            j = i.split("-")[1]
            k = i.split("-")[0]+"-"+j.split("-")[0]
            if k == str(school)+'-'+str(grade):
                cnt = cnt + 1
    student_no = cnt
    student = initial.student(name, school, grade, student_no)
    student.initial(class1)


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
            valid[i] = 0
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
            valid[i] = 1
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
    class1 = initial.classs(year, semester, school, grade, time)
    for i in range(len(students_name)):
        if classes_valid == class1.id:
            classes_valid[i] = 0
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
