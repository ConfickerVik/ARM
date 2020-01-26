from django.shortcuts import render, redirect
from django.conf import settings
# from KRPS.MySQLdb import MySQLDBConnect

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
	courses = [
		{'id':1, 'name':'Командная разработка', 'group':'ПИ 1-16'},
		{'id':2, 'name':'Конструироваие ПО', 'group':'ПИ 1-15'},
	]
	return render(request, 'cabinet/course.html', context={'courses':courses})

def schedule(request):
	return render(request, 'cabinet/schedule.html')