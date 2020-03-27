from django.shortcuts import render, redirect
from django.conf import settings
from KRPS.MySQLdb import MySQLDBConnect
import datetime
from datetime import datetime
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import pickle


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
	#print(request.POST)
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
	editAttendanceQuery = "DELETE FROM krps_db.attendance WHERE id_attendance = '%s';" % (id_attendance)
	DBConnect.query(connectMySQL, editAttendanceQuery)
	connectMySQL.commit()

def createEstimation(request):
	estimation = request.POST.get('mark')
	id_lesson = request.POST.get('id_lesson')
	date = request.POST.get('time_date')
	if '.' in date:
		month, day_year = date.split(".")
		day, year = day_year.split(",")
		date = datetime.strptime(month + day + year, '%b %d %Y').date()
	else:
		month_day, year = date.split(",")
		month, day = month_day.split(" ")
		day = " " + day
		date = datetime.strptime(month + day + year, '%B %d %Y').date()
	id_student = request.POST.get('id_student')
	editLessonQuery = "INSERT INTO krps_db.estimation (estimation, id_lesson, date, id_student)  VALUES ('%s', '%s', '%s', '%s');" % (estimation, id_lesson, date, id_student)
	DBConnect.query(connectMySQL, editLessonQuery)
	connectMySQL.commit()

def createAttendance(request):
	id_lesson = request.POST.get('id_lesson')
	date = request.POST.get('time_date')
	if '.' in date:
		month, day_year = date.split(".")
		day, year = day_year.split(",")
		date = datetime.strptime(month + day + year, '%b %d %Y').date()
	else:
		month_day, year = date.split(",")
		month, day = month_day.split(" ")
		day = " " + day
		date = datetime.strptime(month + day + year, '%B %d %Y').date()
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
	info = {}
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
				info['attendance'] = '0'
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
				marksStudents[stud['id_students']]['marksEstimation'].append({'id_estimation': '0', 'estimation': '0', 'id_lesson': les['id_lesson'], 'date': les['date'], 'id_student': stud['id_students'], 'attendance': '0', 'id_attendance': '0'})
	googleSheets(course_name, group_name, students, lessons, marksStudents)

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
	if request.POST.get('typeAction') == 'addRule':
		addRule(request)
	elif request.POST.get('typeAction') == 'deleteRule':
		deleteRule(request)
	groupsListQuery = "SELECT * FROM krps_db.group;"
	groups = DBConnect.query(connectMySQL, groupsListQuery)
	coursesListQuery = "SELECT * FROM krps_db.courses;"
	courses = DBConnect.query(connectMySQL, coursesListQuery)
	rulesQuery = "SELECT * FROM krps_db.rules;"
	rules = DBConnect.query(connectMySQL, rulesQuery)
	return render(request, 'cabinet/finalMark/index.html', context={'courses':courses, 'groups':groups, 'rules':rules})

def addRule(request):
	name_rule = request.POST.get('name_rule')
	kof_attendance = request.POST.get('kof_attendance')
	kof_mark = request.POST.get('kof_mark')
	addRuleQuery = "INSERT INTO krps_db.rules (name, kofMark, kofAttendance)  VALUES ('%s', '%s', '%s');" % (name_rule, kof_mark, kof_attendance)
	DBConnect.query(connectMySQL, addRuleQuery)
	connectMySQL.commit()

def deleteRule(request):
	print(request.POST)
	delRule_id = request.POST.get('delRule_id')
	deleteRulesQuery = "DELETE FROM krps_db.rules WHERE id_rules = '%s'" % delRule_id
	DBConnect.query(connectMySQL, deleteRulesQuery)
	connectMySQL.commit()
	return render(request, 'cabinet/finalMark/index.html')	

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
		finalStudents[stud['id_students']] = {'lastname_stud': stud['lastname_stud'], 'firstname_stud': stud['firstname_stud'], 'middlename_stud': stud['middlename_stud']}
		finalStudents[stud['id_students']]['finalEstimation'] = []
		finalStudents[stud['id_students']]['finalAttendance'] = []
		finalStudents[stud['id_students']]['finalVes'] = ''
		finalStudents[stud['id_students']]['total'] = ''
		for les in lessons:
			marksListQuery = "SELECT * FROM krps_db.estimation WHERE id_student = '%s' and id_lesson = '%s' and date = '%s';" % (stud['id_students'], les['id_lesson'], les['date'])
			marks = DBConnect.query(connectMySQL, marksListQuery)
			if marks == ():
				marks = [{'id_estimation': '', 'estimation': '', 'id_lesson': les['id_lesson'], 'date': les['date'], 'id_student': stud['id_students']}]
			else:
				for final in finalStudents.keys():
					if final == marks[0]['id_student']:
						info = marks[0]['estimation']
						finalStudents[stud['id_students']]['finalEstimation'].append(info)		
			for atten in attens:
				if marks == ():
					marks = [{'id_estimation': '', 'estimation': '', 'id_lesson': les['id_lesson'], 'date': les['date'], 'id_student': stud['id_students']}]
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
			markfinal = su/count_mark
		else:
			markfinal = 0

		count_atten = len(finalStudents[stud['id_students']]['finalAttendance'])
		if countall != 0:
			markfinalper = float("%.2f" % (count_atten/countall))
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
		totalMark = markfinal*float(kofMark) + int(markfinalatten)*float(kofAttendance)
		su = 0
		finalStudents[stud['id_students']]['total'] = "%.2f" % (totalMark)
		if finalStudents[stud['id_students']]['finalEstimation'] == []:
			finalStudents[stud['id_students']]['finalEstimation'] = '-'
	#print(finalStudents)
	return render(request, 'cabinet/finalMark/index.html', context={'courses':courses, 'groups':groups, 'finalStudents':finalStudents, 'rules':rules})	

def googleSheets(course_name, group_name, students, lessons, marksStudents):
	mas_date = ["ФИО"]
	for les in lessons:
		mas_date.append(str(les['date']))

	mas_stud = []
	for stud in students:
		a = str(stud['lastname_stud']) + " " + str(stud['firstname_stud']) + " " + str(stud['middlename_stud'])
		mas_stud.append(a)

	mas_marks = []
	for key, value in marksStudents.items():
		mas_nemarks = []
		for mark in value['marksEstimation']:
			b = str(mark['estimation']) + " / " + str(mark['attendance'])
			mas_nemarks.append(b)
		mas_marks.append(mas_nemarks)
	#print(mas_marks)

	name_doc = str(course_name) + "_" + str(group_name)
	row_google = len(students)+1
	colums_google = len(lessons)+3

	CREDENTIALS_FILE = 'KRPS-52052d2aee7e.json'  # имя файла с закрытым ключом
	spreadsheet_id = '1Fi8KIY8YLzx-ARKEn8PfEav_U13iOQTFy2mvCY2aoIg'

	credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
																					'https://www.googleapis.com/auth/drive'])
	httpAuth = credentials.authorize(httplib2.Http())
	service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

	service.spreadsheets().values().clear(
		spreadsheetId = spreadsheet_id,
		range = "A1:Z1000"
	).execute()
	#print(spreadsheet)

	driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth)
	shareRes = driveService.permissions().create(
		fileId = spreadsheet_id,
		body = {'type': 'anyone', 'role': 'reader'},  # доступ на чтение кому угодно
		fields = 'id'
	).execute()

	service.spreadsheets().values().batchUpdate(
		spreadsheetId = spreadsheet_id,
		body ={
			"valueInputOption": "USER_ENTERED",
			"data": [
				{"range": "A1:E1",
				"majorDimension": "ROWS",
				"values": [mas_date]},
				{"range": "A2:A"+str(row_google+1),
				"majorDimension": "COLUMNS",
				"values": [mas_stud]},
				{"range": "B2:Z"+str(colums_google+1),
				"majorDimension": "ROWS",
				"values": [thing for thing in mas_marks]}
			]
		}
	).execute()
