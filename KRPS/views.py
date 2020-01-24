from django.shortcuts import render, redirect
from django.conf import settings
from KRPS.MySQLdb import MySQLDBConnect

def index(request):
	title = 'АРМ организация занятий'
	login = ''
	DBConnect = MySQLDBConnect()
	cursorMySQL = DBConnect.connect()
	if request.POST:
		login = request.POST.get('login')
		password = request.POST.get('pass')
		checkDB = "SELECT * FROM krps.users_prepod WHERE login_prepod = '%s' and pass_prepod = '%s';" % (login, password)
		resQueryMySQL = DBConnect.query(cursorMySQL, checkDB)
		if resQueryMySQL != ():
			return redirect('cabinet')
	return render(request, 'auth/index.html', context={'title': title, 'login': login})
	

def cabinet(request):
	lessons = ['1урок', '2урок', '3урок']
	return render(request, 'cabinet/lessons.html', context={'lessons':lessons})
