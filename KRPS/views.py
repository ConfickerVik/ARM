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
		if course['id'] == course_id:
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
	for stud in students:
		marksStudents[stud['id_students']] = {'lastname_stud': stud['lastname_stud'], 'firstname_stud': stud['firstname_stud'], 'middlename_stud': stud['middlename_stud']}
		marksStudents[stud['id_students']]['marksEstimation'] = []
		for les in lessons:
			marksListQuery = "SELECT * FROM krps_db.estimation WHERE id_student = '%s' and id_lesson = '%s' and date = '%s';" % (stud['id_students'], les['id_lesson'], les['date'])
			marks = DBConnect.query(connectMySQL, marksListQuery)
			if marks != ():
				marksStudents[stud['id_students']]['marksEstimation'].append(marks[0])
			else:
				marksStudents[stud['id_students']]['marksEstimation'].append({'id_estimation': '0', 'estimation': '0', 'id_lesson': les['id_lesson'], 'date': les['date'], 'id_student': stud['id_students']})
	#print(marksStudents)
	if request.POST:
		if request.POST.get('typeAction') == 'changeMark':
			if request.POST.get('id_estimation') != '0':
				editEstimation(request)
			else:
				createEstimation(request)
	return render(request, 'cabinet/students/index.html', context={'students':students, 'courses':courses, 'groups':groups, 'lessons':lessons, 'marksStudents': marksStudents})


	'''
	for stud in students:
		marksStudents[stud['id_students']] = {'lastname_stud': stud['lastname_stud'], 'firstname_stud': stud['firstname_stud'], 'middlename_stud': stud['middlename_stud']}
		for les in lessons:
			marksStudents[stud['id_students']]['lesDate'] = les['date']
			marksStudents[stud['id_students']]['lesType'] = les['type']
			marksStudents[stud['id_students']]['marksEstimation'] = []
			for mark in marks:
				if stud['id_students'] == mark['id_student'] and les['id_lesson'] == mark['id_lesson'] and les['date'] == mark['date']:
					marksStudents[stud['id_students']]['marksEstimation'].append(mark)
				else:
					marksStudents[stud['id_students']]['marksEstimation'].append({'id_estimation': '', 'estimation': '', 'id_lesson': les['id_lesson'], 'date': les['date'], 'id_student': stud['id_students']})
	'''

#def prepods(request):
#	prepodsQuery = "SELECT * FROM krps_db.prepods;"
#	prepods = DBConnect.query(connectMySQL, prepodsQuery)
#	return render(request, 'cabinet/navbar.html', context={'prepods':prepods})

def finalMark(request):
    return render(request, 'cabinet/finalMark/index.html')	
