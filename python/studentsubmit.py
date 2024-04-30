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

classes = []


def class_submit():
    year = 2024
    semester = 1
    school = 1
    grade = 20
    time = 1
    class1 = initial.classs(year, semester, school, grade, time)
    classes.append(class1)


def student_submit():
    name = '이윤수'
    school = '경기북과학고'
    if school == '경기북과학고': school = 1
    grade = 20
    class1 = classes[0]
    cnt = 0
    for i in worksheet_id.col_values(1):
        if i[0:4] == str(school) + "-" + str(grade) :
            cnt = cnt + 1
    student_no = cnt + 1
    student = initial.student(name, school, grade, student_no)
    student.initial(class1)

class_submit()
student_submit()