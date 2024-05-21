import gspread
import func
from oauth2client.service_account import ServiceAccountCredentials

scope = 'https://spreadsheets.google.com/feeds'
json = 'C:/Users/mark/PycharmProjects/brain_comment_page/driven-catalyst-411908-9c041a7750dd.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)
gc = gspread.authorize(credentials)
sheet_url = 'https://docs.google.com/spreadsheets/d/1-xp3axKvBFVAMDt0SpnW1oxtPH9lzlgSvEN-WZna2H0/edit#gid=0'
doc = gc.open_by_url(sheet_url)
worksheet_id = doc.worksheet('ID')
worksheet_link = doc.worksheet('link')
worksheet_comment = doc.worksheet('comment')

students = worksheet_id.col_values(1)
student_name = worksheet_id.col_values(2)
student_valid = worksheet_id.col_values(3)

student_link = worksheet_link.col_values(1)
student_class = worksheet_link.col_values(2)


def student_data():
    student = input("student?")
    name = ''
    for i in range(len(students)):
        if students[i] == student:
            name = student_name[i]
    data = student.split("-")
    stu = func.student(name, int(data[0]), int(data[1]), int(data[2]))
    stu.print()
    week = input("week?")
    classs = ''
    for i in range(len(student_link)):
        if student_link[i] == student:
            classs = student_class[i]
    classs
