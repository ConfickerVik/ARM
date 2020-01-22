from django.shortcuts import render


def index(request):
	title = 'АРМ организация занятий'
	return render(request, 'auth/index.html', context={'title': title})

def cabinet(request):
	lessons = ['1урок', '2урок', '3урок']
	return render(request, 'cabinet/lessons.html', context={'lessons':lessons})
