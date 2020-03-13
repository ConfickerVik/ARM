from django.shortcuts import render, redirect
from django.conf import settings
from KRPS.MySQLdb import MySQLDBConnect
import datetime
from datetime import datetime


DBConnect = MySQLDBConnect()
connectMySQL = DBConnect.connect()

def index(request):
	title = 'АРМ организация занятий'
	login = ''
	if request.POST:
		login = request.POST.get('login')
		password = request.POST.get('pass')
		checkDB = "SELECT * FROM krps_db.prepods WHERE login_prepod = '%s' and pass_prepod = '%s';" % (login, password)
		resQueryMySQL = DBConnect.query(connectMySQL, checkDB)
		if resQueryMySQL != ():
			return redirect('cabinet')
	return render(request, 'auth/index.html', context={'title': title, 'login': login})
	
def addCourseModal(request):
	name_dis = request.POST.get('name_dis')
	group_name = request.POST.get('group_name')
	university = request.POST.get('university')
	year_education = int(request.POST.get('year_education'))
	addCourse = "INSERT INTO krps_db.courses (name, year_education, university, group_name) VALUES ('%s', '%d', '%s', '%s');" % (name_dis, year_education, university, group_name)
	DBConnect.query(connectMySQL, addCourse)
	connectMySQL.commit()

def deleteCourse(request):
	id_course = request.POST.get('delCourse_id')
	deleteQuery = "DELETE FROM krps_db.courses WHERE id_course = '%s'" % id_course
	DBConnect.query(connectMySQL, deleteQuery)
	connectMySQL.commit()

def editCourseModal(request):
	id_course = request.POST.get('id_course')
	name_dis = request.POST.get('name_dis')
	group_name = request.POST.get('group_name')
	university = request.POST.get('university')
	year_education = int(request.POST.get('year_education'))
	updateQuery = "UPDATE krps_db.courses SET name = '%s', group_name = '%s', university = '%s', year_education = '%d' WHERE id_course = '%s';" % (name_dis, group_name, university, year_education, id_course)
	DBConnect.query(connectMySQL, updateQuery)
	connectMySQL.commit()

def cabinet(request):
	courses = {}
	print(request.POST)
	if request.POST:
		if request.POST.get('typeAction') == 'addCourse':
			addCourseModal(request)
		if request.POST.get('typeAction') == 'deleteCourse':
			deleteCourse(request)
		if request.POST.get('typeAction') == 'editCourse':
			editCourseModal(request)
	coursesQuery = "SELECT * FROM krps_db.courses"
	courses = DBConnect.query(connectMySQL, coursesQuery)
	return render(request, 'cabinet/courses/index.html', context={'courses':courses})

def editAboutCourse(request):
	id_course = request.POST.get('id_course')
	name_dis = request.POST.get('name_dis')
	group_name = request.POST.get('group_name')
	university = request.POST.get('university')
	year_education = request.POST.get('year_education')
	hours_eucation = request.POST.get('hours_eucation')
	comment = request.POST.get('comment')
	editQueryCourse = "UPDATE krps_db.courses SET name = '%s', year_education = '%s', university = '%s', group_name = '%s', hours_eucation ='%s', comment='%s' WHERE id_course = '%s'" % (name_dis, year_education, university, group_name, hours_eucation, comment, id_course)
	DBConnect.query(connectMySQL, editQueryCourse)
	connectMySQL.commit()

def deleteLesson(request):
	id_lesson = request.POST.get('delCourse_id')
	deleteLessonQuery = "DELETE FROM krps_db.lessons WHERE id_lesson = '%s'" % id_lesson
	DBConnect.query(connectMySQL, deleteLessonQuery)
	connectMySQL.commit()

def addLesson(request):
	id_course = request.POST.get('id_course')
	name = request.POST.get('name')
	typeLesson = request.POST.get('type')
	date = request.POST.get('date')
	addLessonQuery = "INSERT INTO krps_db.lessons (id_course, type, date, name) VALUES ('%s', '%s', '%s', '%s');" % (id_course, typeLesson, date, name)
	DBConnect.query(connectMySQL, addLessonQuery)
	connectMySQL.commit() 

def editLesson(request):
	print(request.POST)
	id_lesson = request.POST.get('id_lesson')
	name = request.POST.get('name')
	typeLesson = request.POST.get('type')
	date = request.POST.get('date')
	day, month, year = date.split(".")
	date = datetime.datetime(int(year), int(month),int(day))
	editLessonQuery = "UPDATE krps_db.lessons SET type = '%s', date = '%s', name = '%s' WHERE id_lesson = '%s';" % (typeLesson, date, name, id_lesson)
	DBConnect.query(connectMySQL, editLessonQuery)
	connectMySQL.commit() 

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
	if request.POST:
		if request.POST.get('typeAction') == 'deleteCourse':
			deleteCourse(request)
		if request.POST.get('typeAction') == 'editAboutCourse':
			editAboutCourse(request)
		if request.POST.get('typeAction') == 'deleteLesson':
			deleteLesson(request)
		if request.POST.get('typeAction') == 'addLesson':
			addLesson(request)
		if request.POST.get('typeAction') == 'editLesson':
			editLesson(request)
	for course in courses: 
		if course['id_course'] == course_id:
			return render(request, 'cabinet/courses/course/index.html', context={'course':course, 'lessons':lessons})
	return render(request, '404.html')

def schedule(request):
	lessonsQuery = "SELECT * FROM krps_db.lessons;"
	lessons = DBConnect.query(connectMySQL, lessonsQuery)
	return render(request, 'cabinet/schedule/index.html', context={'lessons':lessons})

def students(request):
	groupsListQuery = "SELECT * FROM krps_db.group;"
	groups = DBConnect.query(connectMySQL, groupsListQuery)
	coursesListQuery = "SELECT * FROM krps_db.courses;"
	courses = DBConnect.query(connectMySQL, coursesListQuery)
	return render(request, 'cabinet/students/index.html', context={'courses':courses, 'groups':groups})

def editEstimation(request):
	id_estimation = request.POST.get('id_estimation')
	estimation = request.POST.get('mark')
	editLessonQuery = "UPDATE krps_db.estimation SET estimation = '%s' WHERE id_estimation = '%s';" % (estimation, id_estimation)
	DBConnect.query(connectMySQL, editLessonQuery)
	connectMySQL.commit()

def editAttendance(request):
	id_attendance = request.POST.get('id_attendance')
	attendance = request.POST.get('attendance')
	#editAttendanceQuery = "UPDATE krps_db.attendance SET attendance = '%s' WHERE id_attendance = '%s';" % (attendance, id_attendance)
	editAttendanceQuery = "DELETE FROM krps_db.attendance WHERE id_attendance = '%s';" % (id_attendance)
	DBConnect.query(connectMySQL, editAttendanceQuery)
	connectMySQL.commit()

def createEstimation(request):
	estimation = request.POST.get('mark')
	id_lesson = request.POST.get('id_lesson')
	date = request.POST.get('time_date')
	month, day_year = date.split(".")
	day, year = day_year.split(",")
	date = datetime.strptime(month + day + year, '%b %d %Y').date()
	id_student = request.POST.get('id_student')
	editLessonQuery = "INSERT INTO krps_db.estimation (estimation, id_lesson, date, id_student)  VALUES ('%s', '%s', '%s', '%s');" % (estimation, id_lesson, date, id_student)
	DBConnect.query(connectMySQL, editLessonQuery)
	connectMySQL.commit()

def createAttendance(request):
	id_lesson = request.POST.get('id_lesson')
	date = request.POST.get('time_date')
	month, day_year = date.split(".")
	day, year = day_year.split(",")
	date = datetime.strptime(month + day + year, '%b %d %Y').date()
	id_student = request.POST.get('id_student')
	id_attendance = request.POST.get('id_attendance')
	attendance = request.POST.get('attendance')
	editAttendanceQuery = "INSERT INTO krps_db.attendance (attendance, id_lessons, date, id_student)  VALUES ('%s', '%s', '%s', '%s');" % (attendance, id_lesson, date, id_student)
	DBConnect.query(connectMySQL, editAttendanceQuery)
	connectMySQL.commit()

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
		marksStudents[stud['id_students']] = {'lastname_stud': stud['lastname_stud'], 'firstname_stud': stud['firstname_stud'], 'middlename_stud': stud['middlename_stud']}
		marksStudents[stud['id_students']]['marksEstimation'] = []
		for les in lessons:
			marksListQuery = "SELECT * FROM krps_db.estimation WHERE id_student = '%s' and id_lesson = '%s' and date = '%s';" % (stud['id_students'], les['id_lesson'], les['date'])
			marks = DBConnect.query(connectMySQL, marksListQuery)
			attendanceListQuery = "SELECT * FROM krps_db.attendance WHERE id_student = '%s' and id_lessons = '%s' and date = '%s';" % (stud['id_students'], les['id_lesson'], les['date'])
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
			#elif marks == () and attendances != ():
			#	info = {}
			#	info['attendance'] = attendances[0]['attendance']
			#	info['id_attendance'] = attendances[0]['attendance']
			#	info['id_estimation'] = '0'
			#	info['estimation'] = '0'
			#	info['id_lesson'] = les['id_lesson']
			#	info['date'] = les['date']
			#	info['id_student'] = stud['id_students']
			#	marksStudents[stud['id_students']]['marksEstimation'].append(info)
			else:
				marksStudents[stud['id_students']]['marksEstimation'].append({'id_estimation': '0', 'estimation': '0', 'id_lesson': les['id_lesson'], 'date': les['date'], 'id_student': stud['id_students'], 'attendance': '0', 'id_attendance': '0'})

	if request.POST:
		if request.POST.get('typeAction') == 'changeMark':
			if request.POST.get('id_estimation') != '0':
				editEstimation(request)
			else:
				createEstimation(request)
		if request.POST.get('typeAction') == 'changeAtten':
			if request.POST.get('id_attendance') != '0':
				editAttendance(request)
			else:
				createAttendance(request)
	return render(request, 'cabinet/students/index.html', context={'students':students, 'courses':courses, 'groups':groups, 'lessons':lessons, 'marksStudents': marksStudents})

def finalMark(request):
	groupsListQuery = "SELECT * FROM krps_db.group;"
	groups = DBConnect.query(connectMySQL, groupsListQuery)
	coursesListQuery = "SELECT * FROM krps_db.courses;"
	courses = DBConnect.query(connectMySQL, coursesListQuery)
	return render(request, 'cabinet/finalMark/index.html', context={'courses':courses, 'groups':groups})

def finalMarkStudent(request, course_id, group_name, rule):
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
	for stud in students:
		finalStudents[stud['id_students']] = {'lastname_stud': stud['lastname_stud'], 'firstname_stud': stud['firstname_stud'], 'middlename_stud': stud['middlename_stud']}
		finalStudents[stud['id_students']]['finalEstimation'] = []
		finalStudents[stud['id_students']]['finalAttendance'] = []
		for les in lessons:
			marksListQuery = "SELECT * FROM krps_db.estimation WHERE id_student = '%s' and id_lesson = '%s' and date = '%s';" % (stud['id_students'], les['id_lesson'], les['date'])
			marks = DBConnect.query(connectMySQL, marksListQuery)
			for final in finalStudents.keys():
				if final == marks[0]['id_student']:
					info = marks[0]['estimation']
					finalStudents[stud['id_students']]['finalEstimation'].append(info)
		for atten in attens:
			if atten.get('id_student') == marks[0]['id_student']:
				inf = atten.get('attendance')
				#print(atten.get('id_student'), end="---")
				#print(inf)
				#print("______")
				finalStudents[stud['id_students']]['finalAttendance'].append(inf)
	#print(finalStudents)

	if rule == "mark":
		su = 0
		markfinal = 0
		mfinal = {}
		for stud in students:
			mfinal[stud['id_students']] = {'lastname_stud': stud['lastname_stud'], 'firstname_stud': stud['firstname_stud'], 'middlename_stud': stud['middlename_stud']}
			count_mark = len(finalStudents[stud['id_students']]['finalEstimation'])
			for i in finalStudents[stud['id_students']]['finalEstimation']:
				su += int(i)
			markfinal = "%.2f" % (su/count_mark)
			su = 0
			mfinal[stud['id_students']]['fin'] = markfinal
	elif rule == "attend":
		countall = 0
		for les in lessons:
				#print(les['id_course'])
				if course_id == les['id_course']:
					countall += course_id
		mfinal = {}
		for stud in students:
			mfinal[stud['id_students']] = {'lastname_stud': stud['lastname_stud'], 'firstname_stud': stud['firstname_stud'], 'middlename_stud': stud['middlename_stud']}
			count_atten = len(finalStudents[stud['id_students']]['finalAttendance'])
			markfinalper = float("%.2f" % (count_atten/countall))
			if markfinalper >= 0.9:
					markfinal = "5"
			elif markfinalper < 0.9 and markfinalper >= 0.70:
				markfinal = "4"
			elif markfinalper < 0.70 and markfinalper >= 0.55:
				markfinal = "3"
			elif markfinalper < 0.55 and markfinalper >= 0.3:
				markfinal = "2"
			elif markfinalper < 0.3 and markfinalper >= 0.0:
				markfinal = "1"
			mfinal[stud['id_students']]['fin'] = markfinal
	elif rule == "mark+attend":
		countall = 0
		for les in lessons:
				#print(les['id_course'])
				if course_id == les['id_course']:
					countall += course_id
		su = 0
		markfinal = 0
		mfinal = {}
		for stud in students:
			mfinal[stud['id_students']] = {'lastname_stud': stud['lastname_stud'], 'firstname_stud': stud['firstname_stud'], 'middlename_stud': stud['middlename_stud']}
			count_mark = len(finalStudents[stud['id_students']]['finalEstimation'])
			count_atten = len(finalStudents[stud['id_students']]['finalAttendance'])
			markfinalper = float("%.2f" % (count_atten/countall))
			for i in finalStudents[stud['id_students']]['finalEstimation']:
				su += int(i)
			markfinaler = "%.2f" % (su/count_mark)
			markfinal = float(markfinalper) + float(markfinaler)
			if markfinal > 5.0:
				markfinal = 5.0
			su = 0
			mfinal[stud['id_students']]['fin'] = markfinal
	return render(request, 'cabinet/finalMark/index.html', context={'courses':courses, 'groups':groups, 'final':mfinal})	
