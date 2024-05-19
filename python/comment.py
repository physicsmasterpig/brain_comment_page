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

classes = worksheet_id.col_values(5)
classes_valid = worksheet_id.col_values(6)
id = worksheet_id.col_values(1)
lecture = worksheet_link.col_values(4)
subject_lecture = worksheet_link.col_values(5)
problem = worksheet_link.col_values(9)


def lecture_subject():
    classs = input('class?')
    cnt = 0
    for i in range(len(classes)):
        if classs == classes[i] and classes_valid[i] == "v":
            cnt = cnt + 1
    if cnt != 1:
        return
    week = input('week?')
    subject = input('subject?')
    numbers = input('number of problems?')
    total = input('total score?')
    lecture_id = str(classs) + '-' + str(week)
    for i in range(len(lecture)):
        if lecture_id == lecture[i]:
            worksheet_link.update_cell(i + 1, 4, lecture_id)
            worksheet_link.update_cell(i + 1, 5, subject)
            worksheet_link.update_cell(i + 1, 6, total)
            worksheet_link.update_cell(i + 1, 7, numbers)
            return
    if not lecture_id in lecture:
        lecture.append(lecture_id)
        subject_lecture.append(subject)
        worksheet_link.update_cell(len(lecture), 4, lecture_id)
        worksheet_link.update_cell(len(lecture), 5, subject)
        worksheet_link.update_cell(len(lecture), 6, total)
        worksheet_link.update_cell(len(lecture), 7, numbers)


def comment_submit():
    classs = input('class?')
    week = input('week?')
    lecture = worksheet_link.col_values(4)
    cnt = 0
    index = 0
    for i in lecture:
        if i == str(classs) + '-' + str(week):
            cnt += 1
            index = lecture.index(i)
    if cnt != 1:
        return
    student = input('student')
    for i in range(len(id)):
        if id[i] == student:
            if worksheet_id.cell(id.index(student), 3) == 'i':
                return
    numbers = int(worksheet_link.cell(index + 1, 7).value)
    print(numbers)
    for number in range(1, numbers + 1):
        print('No.' + str(number))
        problem_id = str(classs) + '-' + str(week) + '-' + str(number)
        if not problem_id in problem:
            subject = input('subject?')
            allopoint = input('allocated points?')
            problem.append(problem_id)
            worksheet_link.update_cell(len(problem), 9, problem_id)
            worksheet_link.update_cell(len(problem), 10, subject)
            worksheet_link.update_cell(len(problem), 11, allopoint)
        points = input('points?')
        comments = input('comments?')
        a = 0
        for i in range(len(worksheet_comment.col_values(1))):
            if worksheet_comment.col_values(1)[i] == problem_id and worksheet_comment.col_values(2)[i] == student:
                worksheet_comment.update_cell(i + 1, 2, student)
                worksheet_comment.update_cell(i + 1, 3, points)
                worksheet_comment.update_cell(i + 1, 4, comments)
                a = 1
                break
        if a == 1:
            continue
        worksheet_comment.update_cell(len(worksheet_comment.col_values(1)) + 1, 1, problem_id)
        worksheet_comment.update_cell(len(worksheet_comment.col_values(1)), 2, student)
        worksheet_comment.update_cell(len(worksheet_comment.col_values(1)), 3, points)
        worksheet_comment.update_cell(len(worksheet_comment.col_values(1)), 4, comments)


def comment_change():
    classs = input('class?')
    week = input('week?')
    lecture = worksheet_link.col_values(4)
    cnt = 0
    for i in lecture:
        if i == str(classs) + '-' + str(week):
            cnt += 1
    if cnt != 1:
        return
    number = input('number?')
    problem_id = str(classs) + '-' + str(week) + '-' + str(number)
    if not problem_id in problem:
        subject = input('subject?')
        allopoint = input('allocated points?')
        problem.append(problem_id)
        worksheet_link.update_cell(len(problem), 9, problem_id)
        worksheet_link.update_cell(len(problem), 10, subject)
        worksheet_link.update_cell(len(problem), 11, allopoint)
    student = input('student')
    for i in range(len(id)):
        if id[i] == student:
            if worksheet_id.cell(id.index(student), 3) == "i":
                return
    points = input('points?')
    comments = input('comments?')
    for i in range(len(worksheet_comment.col_values(1))):
        if worksheet_comment.col_values(1)[i] == problem_id and worksheet_comment.col_values(2)[i] == student:
            worksheet_comment.update_cell(i + 1, 2, student)
            worksheet_comment.update_cell(i + 1, 3, points)
            worksheet_comment.update_cell(i + 1, 4, comments)
            return
    worksheet_comment.update_cell(len(worksheet_comment.col_values(1)) + 1, 1, problem_id)
    worksheet_comment.update_cell(len(worksheet_comment.col_values(1)), 2, student)
    worksheet_comment.update_cell(len(worksheet_comment.col_values(1)), 3, points)
    worksheet_comment.update_cell(len(worksheet_comment.col_values(1)), 4, comments)
