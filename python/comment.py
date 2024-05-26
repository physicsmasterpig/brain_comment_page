import func
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = 'https://spreadsheets.google.com/feeds'
json = 'driven-catalyst-411908-9c041a7750dd.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)
gc = gspread.authorize(credentials)
sheet_url = 'https://docs.google.com/spreadsheets/d/1-xp3axKvBFVAMDt0SpnW1oxtPH9lzlgSvEN-WZna2H0/edit#gid=0'
doc = gc.open_by_url(sheet_url)

worksheet_link = doc.worksheet('link')
worksheet_comment = doc.worksheet('comment')

days = ['월', '화', '수', '목', '금', '토', '일']


def make_lecture():
    classs = input('class?')
    cnt = 0
    for i in range(len(func.id_class)):
        if classs == func.id_class[i] and func.id_class_valid[i] == "v":
            cnt = cnt + 1
    if cnt != 1:
        return
    week = input('week?')
    perweek = func.classes[classs].perweek
    day = func.classes[classs].day
    daytime = func.classes[classs].daytime
    first = func.classes[classs].first
    if perweek > 1:
        for i in range(perweek):
            date = func.plusdate(first[0], first[1], first[2], (int(week) - 1) * 7 + day[i])
            print(str(i + 1) + '. ' + str(date[0]) + '년 ' + str(date[1]) + '월 ' + str(date[2]) + '일 (' + days[
                day[i]] + ') ' + str(
                daytime[i]) + '시')
        k = input('which day (respond by number)')
        subject = input('subject?')
        numbers = input('number of problems?')
        total = input('total score?')
        func.classes[classs].lecture(week, day[int(k) - 1], subject, total, numbers)
    else:
        subject = input('subject?')
        numbers = input('number of problems?')
        total = input('total score?')
        func.classes[classs].lecture(week, day[0], subject, total, numbers)


def comment_submit():
    student = input('student')
    week = input('week?')
    classs = func.students[student].clas
    if int(func.classes[classs].perweek) > 1:
        perweek = func.classes[classs].perweek
        day = func.classes[classs].day
        daytime = func.classes[classs].daytime
        first = func.classes[classs].first
        for i in range(perweek):
            date = func.plusdate(first[0], first[1], first[2], (int(week) - 1) * 7 + day[i])
            print(str(i + 1) + '. ' + str(date[0]) + '년 ' + str(date[1]) + '월 ' + str(date[2]) + '일 (' + days[
                day[i]] + ') ' + str(
                daytime[i]) + '시')
        k = input('which day (respond by number)')
        lecture = func.students[student].clas + '-' + week + '-' + str(func.classes[classs].day[int(k) - 1])
    else:
        lecture = func.students[student].clas + '-' + week + '-' + str(func.classes[classs].day[0])
    if lecture not in func.link_lecture:
        return
    index = func.link_lecture.index(lecture)
    numbers = int(func.link_number[index])
    for number in range(1, numbers + 1):
        print('No.' + str(number))
        problem_id = lecture + '-' + str(number)
        if problem_id not in func.link_problem:
            subject = input('subject?')
            allopoint = input('allocated points?')
            func.link_problem.append(problem_id)
            func.link_problem_subject.append(subject)
            func.link_allocatedpoints.append(allopoint)
            worksheet_link.update_cell(len(func.link_problem), 9, problem_id)
            worksheet_link.update_cell(len(func.link_problem), 10, subject)
            worksheet_link.update_cell(len(func.link_problem), 11, allopoint)
        points = input('points?')
        comments = input('comments?')
        a = 0
        for i in range(len(func.comment_problem)):
            if func.comment_problem[i] == problem_id and func.comment_student[i] == student:
                func.comment_points[i] = points
                func.comment_comment[i] = comments
                worksheet_comment.update_cell(i + 1, 3, points)
                worksheet_comment.update_cell(i + 1, 4, comments)
                a = 1
                break
        if a == 1:
            continue
        i = len(func.comment_problem)
        func.comment_problem.append(problem_id)
        func.comment_comment.append(student)
        func.comment_points.append(points)
        func.comment_comment.append(comments)
        worksheet_comment.update_cell(i + 1, 1, problem_id)
        worksheet_comment.update_cell(i + 1, 2, student)
        worksheet_comment.update_cell(i + 1, 3, points)
        worksheet_comment.update_cell(i + 1, 4, comments)


def comment_change():
    student = input('student')
    week = input('week?')
    classs = func.students[student].clas
    if int(func.classes[classs].perweek) > 1:
        perweek = func.classes[classs].perweek
        day = func.classes[classs].day
        daytime = func.classes[classs].daytime
        first = func.classes[classs].first
        for i in range(perweek):
            date = func.plusdate(first[0], first[1], first[2], (int(week) - 1) * 7 + day[i])
            print(str(i + 1) + '. ' + str(date[0]) + '년 ' + str(date[1]) + '월 ' + str(date[2]) + '일 (' + days[
                day[i]] + ') ' + str(
                daytime[i]) + '시')
        k = input('which day (respond by number)')
        lecture = func.students[student].clas + '-' + week + '-' + str(func.classes[classs].day[int(k) - 1])
    else:
        lecture = func.students[student].clas + '-' + week + '-' + str(func.classes[classs].day[0])
    if lecture not in func.link_lecture:
        return
    index = func.link_lecture.index(lecture)
    number = input('number?')
    if int(number) > int(func.link_number[index]):
        return
    problem_id = lecture + '-' + str(number)
    if problem_id not in func.link_problem:
        subject = input('subject?')
        allopoint = input('allocated points?')
        func.link_problem.append(problem_id)
        func.link_problem_subject.append(subject)
        func.link_allocatedpoints.append(allopoint)
        worksheet_link.update_cell(len(func.link_problem), 9, problem_id)
        worksheet_link.update_cell(len(func.link_problem), 10, subject)
        worksheet_link.update_cell(len(func.link_problem), 11, allopoint)
    points = input('points?')
    comments = input('comments?')
    for i in range(len(func.comment_problem)):
        if func.comment_problem[i] == problem_id and func.comment_student[i] == student:
            func.comment_points[i] = points
            func.comment_comment[i] = comments
            worksheet_comment.update_cell(i + 1, 3, points)
            worksheet_comment.update_cell(i + 1, 4, comments)
            return
    i = len(func.comment_problem)
    func.comment_problem.append(problem_id)
    func.comment_comment.append(student)
    func.comment_points.append(points)
    func.comment_comment.append(comments)
    worksheet_comment.update_cell(i + 1, 1, problem_id)
    worksheet_comment.update_cell(i + 1, 2, student)
    worksheet_comment.update_cell(i + 1, 3, points)
    worksheet_comment.update_cell(i + 1, 4, comments)
