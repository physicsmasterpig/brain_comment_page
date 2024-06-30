import func
import initial_set
import comment
import open
import attendance
def operation():
    print("어떤 기능을 원하시나요?")
    print("1. 새로운 수업 만들기")
    print("2. 학생 등록하기")
    print("3. 출석 체크")
    print("4. 숙제 여부 체크")
    print("5. 코멘트 입력")
    print("6. 문자 발송")
    print("7. 학생 수업 바꾸기")
    print("0 . 종료")
    k = int(input("respond by number"))
    if k == 0:
        return
    elif k == 1:
        classs = initial_set.class_submit()
        j = input("학생들을 등록할까요?(y/n)")
        if j == 'y':
            initial_set.all_new_students(classs)
            operation()
        else:
            operation()
    elif k == 2:
        j = int(input("한 명 등록 or 다수 등록? (1/2)"))
        if j == 1:
            initial_set.student_submit(0)
        if j == 2:
            initial_set.all_new_students(0)
        operation()
    elif k == 3:
        attendance.attendance()
        operation()
    elif k == 4:
        print('아직')
        operation()
    elif k == 5:
        comment.comment_submit()
        operation()
    elif k == 6:
        open.student_week_message()
        operation()
    elif k == 7:
        j = int(input("한 명 변경 or 다수 변경? (1/2)"))
        if j == 1:
            initial_set.student_change(0,0)
        if j == 2:
            initial_set.all_change_class()
        operation()





func.init()
operation()


