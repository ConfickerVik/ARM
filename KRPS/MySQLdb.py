import pymysql
from django.conf import settings


class MySQLDBConnect:
	def connect(self):
                connection = pymysql.connect(host=settings.DATABASES['default']['HOST'],
			user=settings.DATABASES['default']['USER'],
			password=settings.DATABASES['default']['PASSWORD'],
			database=settings.DATABASES['default']['NAME'],
			cursorclass=pymysql.cursors.DictCursor)
	        return connection

	def query(self, connection, querydb):
		cursor = connection.cursor()
		cursor.execute(querydb)
		resQuary = cursor.fetchall()
		return resQuary
