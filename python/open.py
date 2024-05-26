import func
import math


def mean(x):
    return sum(x) / len(x)


def sd(x):
    return math.sqrt(mean([k ** 2 for k in x]) - (mean(x)) ** 2)


days = ['월', '화', '수', '목', '금', '토', '일']


def student_week_message():
    student_id = input('student?')
    week = input('week?')
    classs = func.students[student_id].clas
    perweek = func.classes[classs].perweek
    day = func.classes[classs].day
    daytime = func.classes[classs].daytime
    first = func.classes[classs].first
    if int(func.classes[classs].perweek) > 1:
        for i in range(perweek):
            date = func.plusdate(first[0], first[1], first[2], (int(week) - 1) * 7 + day[i])
            print(str(i + 1) + '. ' + str(date[0]) + '년 ' + str(date[1]) + '월 ' + str(date[2]) + '일 (' + days[
                day[i]] + ') ' + str(
                daytime[i]) + '시')
        k = int(input('which day (respond by number)'))
    else:
        k = 1
    student = func.students[student_id]
    lecture = student.clas + '-' + week + '-' + str(day[k - 1])
    students = func.classes[student.clas].students
    points = []
    for i in students:
        a = student_point(i, week, str(day[k - 1]))
        if a != -1.0:
            points.append(a)
    if len(points) == 0:
        print('no lecture')
        return
    index = func.link_lecture.index(lecture)
    m = mean(points)
    s = sd(points)
    M = max(points)
    p = student_point(student_id, week, str(day[k - 1]))
    if p == -1.0:
        print("결석함")
        return
    print("")
    print("안녕하세요. 물리 신영수 선생님입니다.")
    date = func.plusdate(first[0], first[1], first[2], (int(week) - 1) * 7 + day[k])
    print(str(date[0]) + '년 ' + str(date[1]) + '월 ' + str(date[2]) + '일 (' + days[
        day[k]] + ') ' + str(daytime[k]) + '시 강의에 대한 시험 결과입니다.')
    print(student.name + " 학생의 경우 테스트 결과는 " + str(p) + '/' + func.link_totalscore[index] + '입니다')
    print("평균 점수는 " + str(m) + "점, 표준편차는 " + str(s) + "점, 최고점은 " + str(M) + "점입니다.")
    print("테스트 피드백은 다음과 같습니다.")
    print(student_comment(student_id, week, str(day[k - 1])))
    print("이 문자는 성적 발신 전용 입니다. 상담을 원하시는 부모님은 제 개인 연락처 010-6636-3002로 카톡 남겨주세요.")


def student_point(id, week, day):
    student = func.students[id]
    lecture = student.clas + '-' + week + '-' + day
    if lecture not in func.link_lecture:
        return -1.0
    index = func.link_lecture.index(lecture)
    numbers = int(func.link_number[index])
    index1 = 0
    for i in range(len(func.comment_problem)):
        if func.comment_problem[i] == lecture + '-1' and func.comment_student[i] == id:
            index1 = i
            break
    if index1 == 0:
        return -1.0
    points = 0.0
    for i in range(int(numbers)):
        points = points + float(func.comment_points[index1 + i])
    return points


def student_comment(id, week, day):
    student = func.students[id]
    lecture = student.clas + '-' + week + '-' + day
    if lecture not in func.link_lecture:
        return ""
    index = func.link_lecture.index(lecture)
    numbers = int(func.link_number[index])
    index1 = 0
    for i in range(len(func.comment_problem)):
        if func.comment_problem[i] == lecture + '-1' and func.comment_student[i] == id:
            index1 = i
            break
    if index1 == 0:
        return ""
    index2 = 0
    for i in range(len(func.link_problem)):
        if func.link_problem[i] == lecture + '-1':
            index2 = i
            break
    comment = ""
    for i in range(int(numbers)):
        comment = comment + "\n" + func.comment_comment[index1 + i] + '(' + func.comment_points[index1 + i] + '/' + \
                  func.link_allocatedpoints[index2 + i] + ")"
    return comment
