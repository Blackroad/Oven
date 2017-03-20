import pymssql


class Dbfixture:
    def __init__(self,host='phxm1bappd48',user="ENT" + "\\" +"velycv1", password='Drul12131415',database='AAEC_pianyv2'):
        self.host = host
        self.user = user
        self.database = database
        self.password = password
        self.connection = pymssql.connect(host=host, database=database, user=user, password=password)
        self.connection.autocommit(True)


    def get_project_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select NotificationName , NotificationDistributionList from cfg.Notification")
            for row in cursor:
                list.append(row)
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def element_printer(self):
        self.get_project_list()
        print(list)




