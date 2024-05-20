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

id_id = worksheet_id.col_values(1)
id_name = worksheet_id.col_values(2)
id_valid = worksheet_id.col_values(3)
id_class = worksheet_id.col_values(5)
id_class_valid = worksheet_id.col_values(6)

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

classes = []


def init():
    for i in range(len(id_class)):
        classes.append(classs(id_class[i]))
    for i in range(len(classes)):
        classes[i].valid = id_class_valid[i]
        for j in range(len(link_class)):
            if link_class[j] == classes[i].id:
                classes[i].students.append(student(id_name[j], id_id[j], classes[i]))
                classes[i].students[len(classes[i].students) - 1].initial()


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
        classes.append(self)

    def initial(self):
        if self.id not in id_class:
            self.valid = 'v'
            id_class.append(self.id)
            id_class_valid.append('v')
            worksheet_id.update_cell(len(id_class) + 1, 1, self.id)
            worksheet_id.update_cell(len(id_class) + 1, 2, self.valid)

    def invalid(self):
        self.valid = 'i'
        id_class_valid[id_class.index(self.id)] = 'i'
        worksheet_id.update_cell(id_class.index(self.id) + 1, 2, self.valid)

    def valid(self):
        self.valid = 'v'
        id_class_valid[id_class.index(self.id)] = 'v'
        worksheet_id.update_cell(id_class.index(self.id) + 1, 2, self.valid)


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
            link_class.append(self.clas.id)
            self.clas.students.append(self)
            worksheet_id.update_cell(self.index + 1, 1, self.id)
            worksheet_id.update_cell(self.index + 1, 2, self.name)
            worksheet_id.update_cell(self.index + 1, 3, self.valid)
            worksheet_link.update_cell(self.index + 1, 1, self.id)
            worksheet_link.update_cell(self.index + 1, 2, self.clas.id)
        else:
            self.index = id_id.index(self.id)
            self.valid = id_valid[self.index]

    def invalid(self):
        self.valid = 'i'
        id_valid[self.index] = 'i'
        link_class[self.index] = 'i'
        worksheet_id.update_cell(self.index + 1, 3, 'i')
        worksheet_link.update_cell(self.index, 2, 'i')
        self.clas.students.delete(self)

    def result_open(self, comment):
        for i in range(len(comment)):
            if comment[i] == self.id:
                self.comment.append(i)

    def print(self):
        print('이름: ' + self.name)
        if self.school == 1:
            print('학교: 경기북과학고')
        elif self.school == 2:
            print('학교: 광주영재학교')
        else:
            print('학교: 대전영재학교')
        print('기수: ' + str(self.grade))
