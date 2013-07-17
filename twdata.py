import MySQLdb

db = MySQLdb.connect("dev.haydle.com","remote","","twitter")
cursor = db.cursor()
sql_query = """SELECT text  FROM `statuses` WHERE `text` LIKE '%:(%' LIMIT 5000"""
cursor.execute(sql_query)
rows = cursor.fetchall()
print "Fetched!"

for row in rows:
    print row[0]