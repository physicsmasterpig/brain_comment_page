import gspread
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

id = worksheet_id.col_values(1)
lecture = worksheet_link.col_values(4)
subject_lecture = worksheet_link.col_values(5)
problem = worksheet_link.col_values(7)


def lecture_subject():
    classs = input('class?')
    week = input('week?')
    subject = input('subject?')
    lecture_id = str(classs) + '-' + str(week)
    if not lecture_id in lecture:
        lecture.append(lecture_id)
        subject_lecture.append(subject)
        worksheet_link.update_cell(len(lecture), 4, lecture_id)
        worksheet_link.update_cell(len(lecture), 5, subject)


def comment_submit():
    classs = input('class?')
    week = input('week?')
    number = input('number?')
    problem_id = str(classs) + '-' + str(week) + '-' + str(number)
    if not problem_id in problem:
        subject = input('subject?')
        worksheet_link.update_cell(len(problem) + 1, 7, problem_id)
        worksheet_link.update_cell(len(problem) + 1, 8, subject)
    student = input('student')
    for i in range(len(id)):
        if id[i] == student:
            if worksheet_id.cell(id.index(student), 3) == 0:
                return
    points = input('points?')
    comments = input('comments?')
    worksheet_comment.update_cell(len(worksheet_comment.col_values(1)) + 1, 1, problem_id)
    worksheet_comment.update_cell(len(worksheet_comment.col_values(1)), 2, student)
    worksheet_comment.update_cell(len(worksheet_comment.col_values(1)), 3, points)
    worksheet_comment.update_cell(len(worksheet_comment.col_values(1)), 4, comments)
