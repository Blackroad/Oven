from fixture.db import Dbfixture

db=Dbfixture()

try:
    element = db.get_project_list()
    for e in element:
        print ('row = %s' % (e,))
finally:
    pass

