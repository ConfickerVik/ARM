from django.shortcuts import render, redirect
from django.conf import settings
from KRPS.MySQLdb import MySQLDBConnect


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
	id_lesson = request.POST.get('id_lesson')
	name = request.POST.get('name')
	typeLesson = request.POST.get('type')
	date = request.POST.get('date')
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
	print(lessons)
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

def marks(request, course_name, group_name):
	groupsListQuery = "SELECT * FROM krps_db.group;"
	groups = DBConnect.query(connectMySQL, groupsListQuery)
	coursesListQuery = "SELECT * FROM krps_db.courses;"
	courses = DBConnect.query(connectMySQL, coursesListQuery)
	lessonsQuery = "SELECT * FROM krps_db.lessons;"
	lessons = DBConnect.query(connectMySQL, lessonsQuery)
	studentsListQuery = "SELECT * FROM krps_db.students WHERE group_stud = '%s'" % group_name
	students = DBConnect.query(connectMySQL, studentsListQuery)
	
	return render(request, 'cabinet/students/index.html', context={'students':students, 'courses':courses, 'groups':groups, 'lessons':lessons})