import pymysql


class MySQLDBConnect:
	def connect(self):
		connection = pymysql.connect(host='127.0.0.1',
			user='root',
			password='VPuRS*lodx854321',
			db='krps',
			cursorclass=pymysql.cursors.DictCursor)
		cursor = connection.cursor()
		return cursor

	def query(self, cursor, querydb):
		cursor.execute(querydb)
		resQuary = cursor.fetchall()
		return resQuary
