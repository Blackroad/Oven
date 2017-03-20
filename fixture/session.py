import time

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self):
        #login to main dashboard
        credentials=self.app.config['jira']
        wd = self.app.wd
        self.app.open_home_page()


    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username


    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//*[@class='pull-left name']/label").text


