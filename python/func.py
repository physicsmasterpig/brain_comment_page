import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = 'https://spreadsheets.google.com/feeds'
json = 'driven-catalyst-411908-9c041a7750dd.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)
gc = gspread.authorize(credentials)
sheet_url = 'https://docs.google.com/spreadsheets/d/1-xp3axKvBFVAMDt0SpnW1oxtPH9lzlgSvEN-WZna2H0/edit#gid=0'
doc = gc.open_by_url(sheet_url)
worksheet_id = doc.worksheet('ID')
worksheet_link = doc.worksheet('link')
worksheet_comment = doc.worksheet('comment')
worksheet_attendance = doc.worksheet('attendance')

id_id = worksheet_id.col_values(1)
id_name = worksheet_id.col_values(2)
id_valid = worksheet_id.col_values(3)
id_class = worksheet_id.col_values(5)
id_class_valid = worksheet_id.col_values(6)
id_perweek = worksheet_id.col_values(7)
id_day = worksheet_id.col_values(8)
id_daytime = worksheet_id.col_values(9)
id_first = worksheet_id.col_values(10)

link_student = worksheet_link.col_values(1)
link_class = worksheet_link.col_values(2)
link_lecture = worksheet_link.col_values(4)
link_subject = worksheet_link.col_values(5)
link_totalscore = worksheet_link.col_values(6)
link_number = worksheet_link.col_values(7)
link_problem = worksheet_link.col_values(9)
link_problem_subject = worksheet_link.col_values(10)
link_allocatedpoints = worksheet_link.col_values(11)
link_homework = worksheet_link.col_values(13)
link_homework_subject = worksheet_link.col_values(14)

comment_problem = worksheet_comment.col_values(1)
comment_student = worksheet_comment.col_values(2)
comment_points = worksheet_comment.col_values(3)
comment_comment = worksheet_comment.col_values(4)

attendance_lecture = worksheet_attendance.col_values(1)
attendance_student = worksheet_attendance.col_values(2)
attendance_value = worksheet_attendance.col_values(3)

classes = {}
students = {}


def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 0
            else:
                return 1

        else:
            return 1
    else:
        return 0


def numberofdate(year, month):
    if month == 2:
        if leap(year):
            return 29
        else:
            return 28
    elif month < 8:
        if month % 2 == 1:
            return 31
        else:
            return 30
    else:
        if month % 2 == 0:
            return 31
        else:
            return 30


def minusdate(year1, month1, date1, year2, month2, date2):
    result = 0
    if year2 > year1:
        for i in range(year1 + 1, year2):
            result = result + 365 + leap(i)
        result = result + minusdate(year1, month1, date1, year1, 12, 31) + minusdate(year2, 1, 1, year2, month2, date2)
    elif year2 < year1:
        result = -minusdate(year2, month2, date2, year1, month1, date1)
    else:
        if month2 > month1:
            for i in range(month1 + 1, month2):
                result = result + numberofdate(year1, i)
            result = result + numberofdate(year1, month1) - date1 + date2
        elif month2 < month1:
            result = -minusdate(year2, month2, date2, year1, month1, date1)
        else:
            result = date2 - date1
    return result


def plusdate(year1, month1, date1, date):
    if date >= 0:
        for i in range(date):
            date1 = date1 + 1
            if date1 > numberofdate(year1, month1):
                date1 = date1 - numberofdate(year1, month1)
                month1 = month1 + 1
                if month1 > 12:
                    month1 = month1 - 12
                    year1 = year1 + 1
    else:
        for i in range(-date):
            date1 = date1 - 1
            if date1 <= 0:
                date1 = date1 + numberofdate(year1, month1)
                month1 = month1 - 1
                if month1 <= 0:
                    month1 = month1 + 12
                    year1 = year1 - 1
    return [year1, month1, date1]


def whichday(year, month, date):
    return minusdate(2024, 5, 27, year, month, date) % 7


def init():
    for i in range(1, len(id_class)):
        classes[id_class[i]] = classs(id_class[i])
    for i in classes.keys():
        classes[i].valid = id_class_valid[id_class.index(i)]
        classes[i].perweek = int(id_perweek[id_class.index(i)])
        classes[i].day = list(map(int, id_day[id_class.index(i)].split("-")))
        classes[i].daytime = list(map(int, id_daytime[id_class.index(i)].split("-")))
        classes[i].first = list(map(int, id_first[id_class.index(i)].split(".")))
        classes[i].student_search()
    for i in range(1, len(id_id)):
        students[id_id[i]] = student(id_name[i], id_id[i], link_class[i])
        students[id_id[i]].valid = id_valid[i]


class classs:
    def __init__(self, id):
        self.year = int(id.split("-")[0])
        self.semester = int(id.split("-")[1])
        self.school = int(id.split("-")[2])
        self.grade = int(id.split("-")[3])
        self.time = int(id.split("-")[4])
        self.id = id
        self.valid = 'v'
        self.students = []
        self.perweek = 0
        self.day = []
        self.daytime = []
        self.first = []

    def initial(self):
        if self.id not in id_class:
            self.valid = 'v'
            classes[self.id] = self
            id_class.append(self.id)
            id_class_valid.append('v')
            worksheet_id.update_cell(len(id_class), 5, self.id)
            worksheet_id.update_cell(len(id_class), 6, self.valid)
            worksheet_id.update_cell(len(id_class), 7, self.perweek)
            day = str(self.day[0])
            daytime = str(self.daytime[0])
            first = str(self.first[0])
            for i in range(1, self.perweek):
                day = day + '-' + str(self.day[i])
                daytime = daytime + '-' + str(self.daytime[i])
            for i in range(1, 3):
                first = first + '.' + str(self.first[i])
            worksheet_id.update_cell(len(id_class), 8, day)
            worksheet_id.update_cell(len(id_class), 9, daytime)
            worksheet_id.update_cell(len(id_class), 10, first)

    def invalid(self):
        self.valid = 'i'
        id_class_valid[id_class.index(self.id)] = 'i'
        worksheet_id.update_cell(id_class.index(self.id) + 1, 6, self.valid)

    def valid(self):
        self.valid = 'v'
        id_class_valid[id_class.index(self.id)] = 'v'
        worksheet_id.update_cell(id_class.index(self.id) + 1, 6, self.valid)

    def student_search(self):
        st = []
        for i in range(len(link_student)):
            if link_class[i] == self.id and id_valid[i] == 'v':
                st.append(id_id[i])
        self.students = st

    def lecture(self, week, day, subject, total, number):
        id = self.id + '-' + str(week) + '-' + str(day)
        if id in link_lecture:
            index = link_lecture.index(id)
            link_subject[index] = subject
            link_totalscore[index] = total
            link_number[index] = number
            worksheet_link.update_cell(index + 1, 5, subject)
            worksheet_link.update_cell(index + 1, 6, total)
            worksheet_link.update_cell(index + 1, 7, number)
        else:
            index = len(link_lecture)
            link_lecture.append(id)
            link_subject.append(subject)
            link_totalscore.append(total)
            link_number.append(number)
            worksheet_link.update_cell(index + 1, 4, id)
            worksheet_link.update_cell(index + 1, 5, subject)
            worksheet_link.update_cell(index + 1, 6, total)
            worksheet_link.update_cell(index + 1, 7, number)


class student:
    def __init__(self, name, id, clas):
        self.name = name
        self.school = int(id.split("-")[0])
        self.grade = int(id.split("-")[1])
        self.student_no = int(id.split("-")[2])
        self.id = id
        self.clas = clas
        self.valid = 'v'
        self.index = 0
        self.comment = []

    def initial(self):
        if self.id not in id_id:
            self.valid = 'v'
            self.index = len(id_id)
            id_id.append(self.id)
            id_name.append(self.name)
            id_valid.append(self.valid)
            link_student.append(self.id)
            link_class.append(self.clas)
            if self.clas in classes.keys():
                classes[self.clas].student_search()
            students[self.id] = self
            worksheet_id.update_cell(self.index + 1, 1, self.id)
            worksheet_id.update_cell(self.index + 1, 2, self.name)
            worksheet_id.update_cell(self.index + 1, 3, self.valid)
            worksheet_link.update_cell(self.index + 1, 1, self.id)
            worksheet_link.update_cell(self.index + 1, 2, self.clas)
        else:
            self.index = id_id.index(self.id)
            id_valid[self.index] = self.valid
            link_class[self.index] = self.clas
            if self.clas in classes.keys():
                classes[self.clas].student_search()
            students[self.id] = self
            worksheet_id.update_cell(self.index + 1, 3, self.valid)
            worksheet_link.update_cell(self.index + 1, 2, self.clas)

    def invalid(self):
        self.valid = 'i'
        self.clas = 'i'
        id_valid[self.index] = 'i'
        link_class[self.index] = 'i'
        worksheet_id.update_cell(self.index + 1, 3, 'i')
        worksheet_link.update_cell(self.index + 1, 2, 'i')
        classes[self.clas].student_search()

    def print(self):
        print('이름: ' + self.name)
        if self.school == 1:
            print('학교: 경기북과학고')
        elif self.school == 2:
            print('학교: 광주영재학교')
        else:
            print('학교: 대전영재학교')
        print('기수: ' + str(self.grade))

    def change(self, classs):
        link_class[link_student.index(self.id)] = classs
        worksheet_link.update_cell(link_student.index(self.id)+1, 2, classs)
        classes[self.clas].student_search()
        self.clas = classs
        classes[self.clas].student_search()
