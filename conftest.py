import json
import os.path
import pytest
from fixture.db import Dbfixture



fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),file)
        with open(config_file) as opened_file:
            target = json.load(opened_file)
    return target


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))



# @pytest.fixture()
# def app(request, config):
#     global fixture
#     browser = request.config.getoption("--browser")
#     if fixture is None or not fixture.is_valid():
#         fixture = Application(browser= browser, config = config)
#     fixture.session.ensure_login(username=config['web']["username"],password=config['web']["password"])
#
#     return fixture


@pytest.fixture(scope="session")
def db(request, config):
    dbfixture = Dbfixture(host=config['db']['host'],name=config['db']['name'],user=config['db']['user'],password = config['db']['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture



@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


# def pytest_addoption(parser):
#     parser.addoption ("--browser", action='store', default='firefox')
#     parser.addoption("--target", action='store', default='target.json')

