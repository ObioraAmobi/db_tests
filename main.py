from database.mysql import MySQLDatabase



my_db = MySQLDatabase(database_name='employees_class_example', username='root', password='-------', host='localhost')


# my_tables = my_db.get_available_tables()
# print my_tables
#
# table_columns = my_db.get_columns_for_table('titles')
# print table_columns
#
#
#
# employee = my_db.select('employees', named_tuples=True)[0]
#
# print employee


kwargs= {'where':'emp_no=10002'}

results = my_db.select('employees', ['first_name'], **kwargs)

print results

kwargs = {'where': "emp_no=1000%",
          'join':'orders ON people.id=orders.person_id',
          'order_by': 'orders.amount desc',
          'limit':2}

results2 = my_db.select('people', columns=['', ''], named_tuples=True, **kwargs)






# print results
#
# db.close()
# my_cursor.close()
# #always close cursors and other applications to stop unneccessary use of resources
#
# results = my_cursor.fetchone()
#
# db.commit() #commits the changes to actual SQL database
#
# my_cursor.execute("SELECT * FROM employees WHERE emp_no = 10001")
# my_cursor.execute("UPDATE employees SET first_name = 'BiggieSmalls' WHERE emp_no = 10001"),
#
# my_cursor = db.cursor()
#
#                     passwd='    ')
#                     user='root',
#                     host='localhost',
# db = _mysql.connect(db='employees_class_example',
#
# import MySQLdb as _mysql