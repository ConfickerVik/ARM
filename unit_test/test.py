from MySQLdb import MySQLDBConnect
import datetime
from datetime import datetime

DBConnect = MySQLDBConnect()
connectMySQL = DBConnect.connect()


# Авторизация
def index(request):
    title = 'АРМ организация занятий'
    login = ''
    if request:
        login = request.get('login')
        password = request.get('pass')
        checkDB = "SELECT * FROM krps_db.prepods WHERE login_prepod = '%s' and pass_prepod = '%s';" % (login, password)
        resQueryMySQL = DBConnect.query(connectMySQL, checkDB)
        # if resQueryMySQL != ():
        # print("Вход")
        # return redirect('cabinet')
    # return render(request, 'auth/index.html', context={'title': title, 'login': login})


# Добавить курс
def addCourseModal(request):
    name_dis = request.get('name_dis')  # POST.
    group_name = request.get('group_name')
    university = request.get('university')
    year_education = int(request.get('year_education'))
    addCourse = "INSERT INTO krps_db.courses (name, year_education, university, group_name) VALUES ('%s', '%d', '%s', '%s');" % (
        name_dis, year_education, university, group_name)
    DBConnect.query(connectMySQL, addCourse)
    connectMySQL.commit()


# Удалить курс
def deleteCourse(request):
    id_course = request.get('id_course')
    deleteQuery = "DELETE FROM krps_db.courses WHERE id_course = '%s'" % id_course
    DBConnect.query(connectMySQL, deleteQuery)
    connectMySQL.commit()


# Редактировать курс
def editCourseModal(request):
    id_course = request.get('id_course')
    name_dis = request.get('name_dis')
    group_name = request.get('group_name')
    university = request.get('university')
    year_education = int(request.get('year_education'))
    updateQuery = "UPDATE krps_db.courses SET name = '%s', group_name = '%s', university = '%s', year_education = '%d' WHERE id_course = '%s';" % (
        name_dis, group_name, university, year_education, id_course)
    DBConnect.query(connectMySQL, updateQuery)
    connectMySQL.commit()
    # print("Изменено")


# Вывести список курсов
def cabinet(request):
    # if request.POST:
    if request.get('typeAction') == 'addCourse':
        addCourseModal(request)
    if request.get('typeAction') == 'deleteCourse':
        deleteCourse(request)
    if request.get('typeAction') == 'editCourse':
        editCourseModal(request)
    coursesQuery = "SELECT * FROM krps_db.courses"
    courses = DBConnect.query(connectMySQL, coursesQuery)
    # return render(request, 'cabinet/courses/index.html', context={'courses':courses})


# Полное редактирование курса
def editAboutCourse(request):
    id_course = request.get('id_course')
    name_dis = request.get('name_dis')
    group_name = request.get('group_name')
    university = request.get('university')
    year_education = request.get('year_education')
    hours_eucation = request.get('hours_eucation')
    comment = request.get('comment')
    editQueryCourse = "UPDATE krps_db.courses SET name = '%s', year_education = '%s', university = '%s', group_name = '%s', hours_eucation ='%s', comment='%s' WHERE id_course = '%s'" % (
        name_dis, year_education, university, group_name, hours_eucation, comment, id_course)
    DBConnect.query(connectMySQL, editQueryCourse)
    connectMySQL.commit()


# Добавить занятие
def addLesson(request):
    id_course = request.get('id_course')
    name = request.get('name')
    typeLesson = request.get('type')
    date = request.get('date')
    addLessonQuery = "INSERT INTO krps_db.lessons (id_course, type, date, name) VALUES ('%s', '%s', '%s', '%s');" % (
        id_course, typeLesson, date, name)
    DBConnect.query(connectMySQL, addLessonQuery)
    connectMySQL.commit()


# Удалить занятие
def deleteLesson(request):
    id_lesson = request.get('delCourse_id')
    deleteLessonQuery = "DELETE FROM krps_db.lessons WHERE id_lesson = '%s'" % id_lesson
    DBConnect.query(connectMySQL, deleteLessonQuery)
    connectMySQL.commit()


# Редактировать занятие
def editLesson(request):
    id_lesson = request.get('id_lesson')
    name = request.get('name')
    typeLesson = request.get('type')
    date = request.get('date')
    day, month, year = date.split(".")
    date = datetime(int(year), int(month), int(day))
    editLessonQuery = "UPDATE krps_db.lessons SET type = '%s', date = '%s', name = '%s' WHERE id_lesson = '%s';" % (
        typeLesson, date, name, id_lesson)
    DBConnect.query(connectMySQL, editLessonQuery)
    connectMySQL.commit()


# Отобразить занятия курса
def course(request, course_id):
    coursesQuery = "SELECT * FROM krps_db.courses WHERE id_course = '%s';" % course_id
    courses = DBConnect.query(connectMySQL, coursesQuery)
    lessonsQuery = "SELECT * FROM krps_db.lessons WHERE id_course ='%s';" % course_id
    lessons = DBConnect.query(connectMySQL, lessonsQuery)
    for lesson in lessons:
        dateDict = lesson['date']
        yearDate = dateDict.year
        monthDate = dateDict.month
        dayDate = dateDict.day
        lesson['date'] = "%s.%s.%s" % (dayDate, monthDate, yearDate)
        # if request.POST:
        if request.get('typeAction') == 'deleteCourse':
            deleteCourse(request)
        if request.get('typeAction') == 'editAboutCourse':
            editAboutCourse(request)
        if request.get('typeAction') == 'deleteLesson':
            deleteLesson(request)
        if request.get('typeAction') == 'addLesson':
            addLesson(request)
        if request.get('typeAction') == 'editLesson':
            editLesson(request)
    for course in courses:
        if course['id_course'] == course_id:
            print("1")
            # return render(request, 'cabinet/courses/course/index.html', context={'course': course, 'lessons': lessons})
    # return render(request, '404.html')


# Получить все занятия Расписание
def schedule(request):
    lessonsQuery = "SELECT * FROM krps_db.lessons;"
    lessons = DBConnect.query(connectMySQL, lessonsQuery)
    # return render(request, 'cabinet/schedule/index.html', context={'lessons': lessons})


# Получить все группы и курсы
def students(request):
    groupsListQuery = "SELECT * FROM krps_db.group;"
    groups = DBConnect.query(connectMySQL, groupsListQuery)
    coursesListQuery = "SELECT * FROM krps_db.courses;"
    courses = DBConnect.query(connectMySQL, coursesListQuery)
    # return render(request, 'cabinet/students/index.html', context={'courses': courses, 'groups': groups})


# Редактировать оценку
def editEstimation(request):
    id_estimation = request.get('id_estimation')
    estimation = request.get('mark')
    editLessonQuery = "UPDATE krps_db.estimation SET estimation = '%s' WHERE id_estimation = '%s';" % (
        estimation, id_estimation)
    DBConnect.query(connectMySQL, editLessonQuery)
    connectMySQL.commit()


# Редактировать посещение есть или нет
def editAttendance(request):
    id_attendance = request.get('id_attendance')
    attendance = request.get('attendance')
    editAttendanceQuery = "DELETE FROM krps_db.attendance WHERE id_attendance = '%s';" % (id_attendance)
    DBConnect.query(connectMySQL, editAttendanceQuery)
    connectMySQL.commit()


# Добавить оценку
def createEstimation(request):
    estimation = request.get('mark')
    id_lesson = request.get('id_lesson')
    date = request.get('time_date')
    if '.' in date:
        month, day_year = date.split(".")
        day, year = day_year.split(",")
        date = datetime.strptime(month + day + year, '%b %d %Y').date()
    else:
        month_day, year = date.split(",")
        month, day = month_day.split(" ")
        day = " " + day
        date = datetime.strptime(month + day + year, '%B %d %Y').date()
    id_student = request.get('id_student')
    editLessonQuery = "INSERT INTO krps_db.estimation (estimation, id_lesson, date, id_student)  VALUES ('%s', '%s', '%s', '%s');" % (
        estimation, id_lesson, date, id_student)
    DBConnect.query(connectMySQL, editLessonQuery)
    connectMySQL.commit()


# Добавить посещение
def createAttendance(request):
    id_lesson = request.get('id_lesson')
    date = request.get('time_date')
    if '.' in date:
        month, day_year = date.split(".")
        day, year = day_year.split(",")
        date = datetime.strptime(month + day + year, '%b %d %Y').date()
    else:
        month_day, year = date.split(",")
        month, day = month_day.split(" ")
        day = " " + day
        date = datetime.strptime(month + day + year, '%B %d %Y').date()
    id_student = request.get('id_student')
    id_attendance = request.get('id_attendance')
    attendance = request.get('attendance')
    editAttendanceQuery = "INSERT INTO krps_db.attendance (attendance, id_lessons, date, id_student)  VALUES ('%s', '%s', '%s', '%s');" % (
        attendance, id_lesson, date, id_student)
    DBConnect.query(connectMySQL, editAttendanceQuery)
    connectMySQL.commit()


# Оценки
def marks(request, course_name, group_name):
    groupsListQuery = "SELECT * FROM krps_db.group;"
    groups = DBConnect.query(connectMySQL, groupsListQuery)
    coursesListQuery = "SELECT * FROM krps_db.courses;"
    courses = DBConnect.query(connectMySQL, coursesListQuery)
    lessonsQuery = "SELECT * FROM krps_db.lessons WHERE id_course = '%s';" % course_name
    lessons = DBConnect.query(connectMySQL, lessonsQuery)
    studentsListQuery = "SELECT * FROM krps_db.students WHERE group_stud = '%s';" % group_name
    students = DBConnect.query(connectMySQL, studentsListQuery)
    marksStudents = {}
    info = ''
    for stud in students:
        marksStudents[stud['id_students']] = {'lastname_stud': stud['lastname_stud'],
                                              'firstname_stud': stud['firstname_stud'],
                                              'middlename_stud': stud['middlename_stud']}
        marksStudents[stud['id_students']]['marksEstimation'] = []
        for les in lessons:
            marksListQuery = "SELECT * FROM krps_db.estimation WHERE id_student = '%s' and id_lesson = '%s' and date = '%s';" % (
                stud['id_students'], les['id_lesson'], les['date'])
            marks = DBConnect.query(connectMySQL, marksListQuery)
            attendanceListQuery = "SELECT * FROM krps_db.attendance WHERE id_student = '%s' and id_lessons = '%s' and date = '%s';" % (
                stud['id_students'], les['id_lesson'], les['date'])
            attendances = DBConnect.query(connectMySQL, attendanceListQuery)
            if marks != () and attendances != ():
                info = marks[0]
                info['attendance'] = attendances[0]['attendance']
                info['id_attendance'] = attendances[0]['id_attendance']
                marksStudents[stud['id_students']]['marksEstimation'].append(info)
            elif marks != () and attendances == ():
                info = marks[0]
                info['attendance'] = 'false'
                info['id_attendance'] = '0'
                marksStudents[stud['id_students']]['marksEstimation'].append(info)
            elif marks == () and attendances != ():
                info['id_estimation'] = '0'
                info['estimation'] = '0'
                info['id_lesson'] = les['id_lesson']
                info['date'] = les['date']
                info['id_student'] = stud['id_students']
                info['attendance'] = attendances[0]['attendance']
                info['id_attendance'] = attendances[0]['id_attendance']
                marksStudents[stud['id_students']]['marksEstimation'].append(info)
            else:
                marksStudents[stud['id_students']]['marksEstimation'].append(
                    {'id_estimation': '0', 'estimation': '0', 'id_lesson': les['id_lesson'], 'date': les['date'],
                     'id_student': stud['id_students'], 'attendance': '0', 'id_attendance': '0'})

        # if request.POST:
        if request.get('typeAction') == 'changeMark':
            if request.get('id_estimation') != '0':
                editEstimation(request)
            else:
                createEstimation(request)
        if request.get('typeAction') == 'changeAtten':
            if request.get('id_attendance') != '0':
                editAttendance(request)
            else:
                createAttendance(request)
    # return render(request, 'cabinet/students/index.html',
    # context={'students': students, 'courses': courses, 'groups': groups, 'lessons': lessons,
    # 'marksStudents': marksStudents})


# Итоговые оценки
def finalMark(request):
    if request.get('typeAction') == 'addRule':
        addRule(request)
    elif request.get('typeAction') == 'deleteRule':
        deleteRule(request)
    groupsListQuery = "SELECT * FROM krps_db.group;"
    groups = DBConnect.query(connectMySQL, groupsListQuery)
    coursesListQuery = "SELECT * FROM krps_db.courses;"
    courses = DBConnect.query(connectMySQL, coursesListQuery)
    rulesQuery = "SELECT * FROM krps_db.rules;"
    rules = DBConnect.query(connectMySQL, rulesQuery)
    # return render(request, 'cabinet/finalMark/index.html',
    # context={'courses': courses, 'groups': groups, 'rules': rules})


# Добавить правило
def addRule(request):
    name_rule = request.POST.get('name_rule')
    kof_attendance = request.POST.get('kof_attendance')
    kof_mark = request.POST.get('kof_mark')
    addRuleQuery = "INSERT INTO krps_db.rules (name, kofMark, kofAttendance)  VALUES ('%s', '%s', '%s');" % (
        name_rule, kof_mark, kof_attendance)
    DBConnect.query(connectMySQL, addRuleQuery)
    connectMySQL.commit()


# Удалить правило
def deleteRule(request):
    # print(request.POST)
    delRule_id = request.POST.get('delRule_id')
    deleteRulesQuery = "DELETE FROM krps_db.rules WHERE id_rules = '%s'" % delRule_id
    DBConnect.query(connectMySQL, deleteRulesQuery)
    connectMySQL.commit()
    # return render(request, 'cabinet/finalMark/index.html')


# Получить итоговые оценки конкретного курса, группы и правила
def finalMarkStudent(request, course_id, group_name, kofMark, kofAttendance):
    if request.POST.get('typeAction') == 'addRule':
        addRule(request)
    elif request.POST.get('typeAction') == 'deleteRule':
        deleteRule(request)
    rulesQuery = "SELECT * FROM krps_db.rules;"
    rules = DBConnect.query(connectMySQL, rulesQuery)
    groupsListQuery = "SELECT * FROM krps_db.group;"
    groups = DBConnect.query(connectMySQL, groupsListQuery)
    coursesListQuery = "SELECT * FROM krps_db.courses;"
    courses = DBConnect.query(connectMySQL, coursesListQuery)
    lessonsQuery = "SELECT * FROM krps_db.lessons WHERE id_course = '%s';" % course_id
    lessons = DBConnect.query(connectMySQL, lessonsQuery)
    attensQuery = "SELECT * FROM krps_db.attendance"
    attens = DBConnect.query(connectMySQL, attensQuery)
    studentsListQuery = "SELECT * FROM krps_db.students WHERE group_stud = '%s';" % group_name
    students = DBConnect.query(connectMySQL, studentsListQuery)

    finalStudents = {}
    mas_attendence = []
    for stud in students:
        finalStudents[stud['id_students']] = {'lastname_stud': stud['lastname_stud'],
                                              'firstname_stud': stud['firstname_stud'],
                                              'middlename_stud': stud['middlename_stud']}
        finalStudents[stud['id_students']]['finalEstimation'] = []
        finalStudents[stud['id_students']]['finalAttendance'] = []
        finalStudents[stud['id_students']]['finalVes'] = ''
        finalStudents[stud['id_students']]['total'] = ''
        for les in lessons:
            marksListQuery = "SELECT * FROM krps_db.estimation WHERE id_student = '%s' and id_lesson = '%s' and date = '%s';" % (
            stud['id_students'], les['id_lesson'], les['date'])
            marks = DBConnect.query(connectMySQL, marksListQuery)
            if marks == ():
                marks = [{'id_estimation': '', 'estimation': '', 'id_lesson': les['id_lesson'], 'date': les['date'],
                          'id_student': stud['id_students']}]
            else:
                for final in finalStudents.keys():
                    if final == marks[0]['id_student']:
                        info = marks[0]['estimation']
                        finalStudents[stud['id_students']]['finalEstimation'].append(info)
            for atten in attens:
                if marks == ():
                    marks = [{'id_estimation': '', 'estimation': '', 'id_lesson': les['id_lesson'], 'date': les['date'],
                              'id_student': stud['id_students']}]
                elif atten.get('id_student') == marks[0]['id_student']:
                    inf = atten.get('attendance')
                    finalStudents[stud['id_students']]['finalAttendance'].append(inf)

        su = 0
        markfinal = 0
        countall = 0
        for les in lessons:
            if course_id == les['id_course']:
                countall += course_id
        count_mark = len(finalStudents[stud['id_students']]['finalEstimation'])
        for i in finalStudents[stud['id_students']]['finalEstimation']:
            su += int(i)
        # Ср. арифм
        if count_mark != 0:
            markfinal = su / count_mark
        else:
            markfinal = 0

        count_atten = len(finalStudents[stud['id_students']]['finalAttendance'])
        if countall != 0:
            markfinalper = float("%.2f" % (count_atten / countall))
        else:
            markfinalper = 0
        if markfinalper >= 0.9:
            markfinalatten = "5"
        elif markfinalper < 0.9 and markfinalper >= 0.70:
            markfinalatten = "4"
        elif markfinalper < 0.70 and markfinalper >= 0.55:
            markfinalatten = "3"
        elif markfinalper < 0.55 and markfinalper >= 0.3:
            markfinalatten = "2"
        elif markfinalper < 0.3 and markfinalper > 0.0:
            markfinalatten = "1"
        elif markfinalper == 0.0:
            markfinalatten = "0"
        # % оценка за посещаемость
        finalStudents[stud['id_students']]['finalVes'] = markfinalatten
        totalMark = markfinal * float(kofMark) + int(markfinalatten) * float(kofAttendance)
        su = 0
        finalStudents[stud['id_students']]['total'] = "%.2f" % (totalMark)
        if finalStudents[stud['id_students']]['finalEstimation'] == []:
            finalStudents[stud['id_students']]['finalEstimation'] = '-'
    # print(finalStudents)
    #return render(request, 'cabinet/finalMark/index.html',
                  #context={'courses': courses, 'groups': groups, 'finalStudents': finalStudents, 'rules': rules})
