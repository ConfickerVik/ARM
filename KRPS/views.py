from django.shortcuts import render, redirect
from django.conf import settings
from KRPS.MySQLdb import MySQLDBConnect

DBConnect = MySQLDBConnect()
connectMySQL = DBConnect.connect()
lessons = [
	{'id':1,
	 'id_test':1,
	 'type':'Лекция',
	 'date':'2001.09.11',
	 'name':'Как правильно летать'
	},
	{'id':2,
	 'id_test':1,
	 'type':'Практика',
	 'date':'2001.09.11',
	 'name':'Гном ест борщ'
	}
	]

def index(request):
	title = 'АРМ организация занятий'
	login = ''
	#password = ''
	if request.POST:
		login = request.POST.get('login')
		password = request.POST.get('pass')
		checkDB = "SELECT * FROM krps_db.prepods WHERE login_prepod = '%s' and pass_prepod = '%s';" % (login, password)
		resQueryMySQL = DBConnect.query(connectMySQL, checkDB)
		#if login == request.POST.get('login') and password == request.POST.get('login'):
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

def cabinet(request):
	if request.POST:
		addCourseModal(request)
		return redirect('cabinet')
	coursesQuery = "SELECT * FROM krps_db.courses"
	courses = DBConnect.query(connectMySQL, coursesQuery)
	return render(request, 'cabinet/courses/index.html', context={'courses':courses})

def course(request, course_id):
	coursesQuery = "SELECT * FROM krps_db.courses WHERE id_course = '%s';" % course_id
	courses = DBConnect.query(connectMySQL, coursesQuery)
	lessonsQuery = "SELECT * FROM krps_db.lessons;"
	lessons = DBConnect.query(connectMySQL, lessonsQuery)
	for course in courses: 
		if course['id_course'] == course_id:
			return render(request, 'cabinet/courses/course/index.html', context={'course':course, 'lessons':lessons})
	return render(request, '404.html')

def deleteCourse(request, id_course):
	print(id_course)
	return redirect('cabinet')

def schedule(request):
	return render(request, 'cabinet/schedule/index.html', context={'lessons':lessons})

def students(request):
	return render(request, 'cabinet/students/index.html')