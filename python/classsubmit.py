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
    class1.initial()

class_submit()
