import pymysql


class MySQLDBConnect:
	def connect(self):
		connection = pymysql.connect(
			host='127.0.0.1',
			user='root',
			password='qwerty90',
			db='krps_db',
			cursorclass=pymysql.cursors.DictCursor)
		return connection

	def query(self, connection, querydb):
		cursor = connection.cursor()
		cursor.execute(querydb)
		resQuary = cursor.fetchall()
		return resQuary
