from django.shortcuts import render, redirect
from django.conf import settings
from KRPS.MySQLdb import MySQLDBConnect


DBConnect = MySQLDBConnect()
connectMySQL = DBConnect.connect()

def index(request):
	title = 'АРМ организация занятий'
	login = ''
	password = ''
	# DBConnect = MySQLDBConnect()
	# cursorMySQL = DBConnect.connect()
	if request.POST:
		login = request.POST.get('login')
		password = request.POST.get('pass')
		# checkDB = "SELECT * FROM krps.users_prepod WHERE login_prepod = '%s' and pass_prepod = '%s';" % (login, password)
		# resQueryMySQL = DBConnect.query(cursorMySQL, checkDB)
		if login == request.POST.get('login') and password == request.POST.get('login'):
			return redirect('cabinet')
	return render(request, 'auth/index.html', context={'title': title, 'login': login})
	

#def addCourseModal(request):
	

def deleteCourseModal(request):
	DBConnect = MySQLDBConnect()
	cursorMySQL = DBConnect.connect()
	if request.POST:
		id_courses = int(request.POST.get('sys.courses.id_course'))
		checkDB = "DELETE FROM sys.courses WHERE id_courses = %d" % id_courses
		DBConnect.query(connectMySQL, checkDB)
		connectMySQL.commit()
	return redirect('cabinet')
	
	
def cabinet(request):
	coursesQuery = "SELECT * FROM sys.courses;"
	courses = DBConnect.query(connectMySQL, coursesQuery)
	if request.POST:
		if len(request.POST) == 5:
			print(request.POST)
			print(request.GET)
			name_dis = request.POST.get('name_dis')
			group_name = request.POST.get('group_name')
			univer = request.POST.get('univer')
			year_ed = int(request.POST.get('year_ed'))
			checkDB = "INSERT INTO sys.courses (name, year_education, university, group_name)  VALUES ('%s', '%d', '%s', '%s');" % (name_dis, year_ed, univer, group_name)
			DBConnect.query(connectMySQL, checkDB)
			connectMySQL.commit()
			return redirect('cabinet')
		else:
			print(request.POST)
			print()
			#id_courses = int(request.POST.get('sys.courses.id_course'))
			#checkDB = "DELETE FROM sys.courses WHERE id_courses = %d" % id_courses
			#DBConnect.query(connectMySQL, checkDB)
			#connectMySQL.commit()
			#return redirect('cabinet')
			
	return render(request, 'cabinet/courses/index.html', context={'courses':courses})

def course(request, course_id):
	for course in courses: 
		if course['id'] == course_id:
			return render(request, 'cabinet/courses/course/index.html', context={'course':course, 'lessons':lessons})
	return render(request, '404.html')

def schedule(request):
	return render(request, 'cabinet/schedule/index.html', context={'lessons':lessons})

def students(request):
	return render(request, 'cabinet/students/index.html')