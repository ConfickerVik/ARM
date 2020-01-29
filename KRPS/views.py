from django.shortcuts import render, redirect
from django.conf import settings
# from KRPS.MySQLdb import MySQLDBConnect

courses = [
		{'id':1,
		 'name':'Командная разработка',
		 'yearEducation':"'19-'20",
		 'university':'ИрГУПС',
		 'group':'ПИ-16',
		 'countSrudents':'24',
		 'hoursEducation':"120",
		 'comment':'Делаем компилятор'
		},
		{'id':2,
		 'name':'Конструироваие ПО',
		 'yearEducation':"'19-'20",
		 'university':'ИрГУПС',
		 'group':'ПИ-15',
		 'countSrudents':'24',
		 'hoursEducation':"120",
		 'comment':'Делаем компилятор'
		},
	]
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
	

	
def cabinet(request):
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