import pymysql.cursors


class Dbfixture:
    def __init__(self,host,name,user,password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)


    def get_project_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id,name from mantis_project_table")
            for row in cursor:
                (id,name)=row
                list.append()
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()