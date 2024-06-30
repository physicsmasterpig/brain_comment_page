import func, comment
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = 'https://spreadsheets.google.com/feeds'
json = 'driven-catalyst-411908-9c041a7750dd.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)
gc = gspread.authorize(credentials)
sheet_url = 'https://docs.google.com/spreadsheets/d/1-xp3axKvBFVAMDt0SpnW1oxtPH9lzlgSvEN-WZna2H0/edit#gid=0'
doc = gc.open_by_url(sheet_url)
worksheet_attendance = doc.worksheet('attendance')

days = ['월', '화', '수', '목', '금', '토', '일']


def attendance():
    week = input('week?')
    classs = input('class?')
    cnt = 0
    for i in range(len(func.id_class)):
        if classs == func.id_class[i] and func.id_class_valid[i] == "v":
            cnt = cnt + 1
    if cnt != 1:
        return
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
        lecture = classs + '-' + week + '-' + str(func.classes[classs].day[int(k) - 1])
    else:
        lecture = classs + '-' + week + '-' + str(func.classes[classs].day[0])
    if lecture not in func.link_lecture:
        comment.make_lecture()
        return
    for i in func.classes[classs].students:
        print("")
        print(func.students[i].name + '(010-****-' + str(int(func.students[i].id.split("-")[2]) % 10000) + ')')
        print("0: 결석")
        print("1: 출석")
        print("2: 동영상")
        a = input("respond by number")
        a = int(a)
        func.attendance_lecture.append(lecture)
        func.attendance_student.append(func.students[i].id)
        func.attendance_student.append(a)
        worksheet_attendance.update_cell(len(func.attendance_lecture), 1, lecture)
        worksheet_attendance.update_cell(len(func.attendance_lecture), 2, func.students[i].id)
        worksheet_attendance.update_cell(len(func.attendance_lecture), 3, a)
