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


class classs:
    def __init__(self, year, semester, school, grade, time):
        self.year = year
        self.semester = semester
        self.school = school
        self.grade = grade
        self.time = time
        self.id = str(year) + "-" + str(semester) + "-" + str(school) + "-" + str(grade) + "-" + str(time)

    def initial(self, classes):
        for i in range(len(classes)):
            worksheet_id.update_cell(i + 1, 5, classes[i])


class student:
    def __init__(self, name, school, grade, student_no):
        self.name = name
        self.school = school
        self.grade = grade
        self.id = str(school) + "-" + str(grade) + "-" + str(student_no)

    def initial(self, clas):
        length1 = len(worksheet_id.col_values(1))
        length2 = len(worksheet_link.col_values(1))
        worksheet_id.update_cell(length1 + 1, 1, self.id)
        worksheet_id.update_cell(length1 + 1, 2, self.name)
        worksheet_id.update_cell(length1 + 1, 3, 1)
        worksheet_link.update_cell(length2 + 1, 1, self.id)
        worksheet_link.update_cell(length2 + 1, 2, clas)
