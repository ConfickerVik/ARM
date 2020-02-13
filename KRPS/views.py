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

def course(request, course_id):
	coursesQuery = "SELECT * FROM krps_db.courses WHERE id_course = '%s';" % course_id
	courses = DBConnect.query(connectMySQL, coursesQuery)
	lessonsQuery = "SELECT * FROM krps_db.lessons;"
	lessons = DBConnect.query(connectMySQL, lessonsQuery)
	if request.POST:
		if request.POST.get('typeAction') == 'deleteCourse':
			deleteCourse(request)
	for course in courses: 
		if course['id_course'] == course_id:
			return render(request, 'cabinet/courses/course/index.html', context={'course':course, 'lessons':lessons})
	return render(request, '404.html')

def schedule(request):
	return render(request, 'cabinet/schedule/index.html', context={'lessons':lessons})

def students(request):
	return render(request, 'cabinet/students/index.html')