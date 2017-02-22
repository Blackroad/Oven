import pymysql.cursors
from fixture.db import Dbfixture
#from Model.projectmodel import Project


db = Dbfixture(host='127.0.0.1', name='bugtracker', user='root', password='')

try:
    l = db.get_project_list()
    for item in l:
        print(item)
    print (len(l))
finally:
    pass