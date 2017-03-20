import json
import os.path
import pytest
from fixture.application import Application
from fixture.db import Dbfixture



fixture = None
target = None
db_config = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),file)
        with open(config_file) as opened_file:
            target = json.load(opened_file)
    return target

def load_db_config(file):
    global db_config
    if db_config is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),file)
        with open(config_file) as opened_file:
            db_config = json.load(opened_file)
    return db_config


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target")), load_db_config(request.config.getoption("--db_config"))



@pytest.fixture()
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None:
        fixture = Application(browser= browser, config = config)
    return fixture


@pytest.fixture(scope="session")
def db(request, load_db_config):
    dbfixture = Dbfixture(host=load_db_config['dbc']['db_server'],user=load_db_config['dbc']['username'],
                          database=load_db_config['dbc']['db_name'],
                          password = load_db_config['dbc']['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture



@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


# def pytest_addoption(parser):
#     parser.addoption ("--browser", action='store', default='firefox')
#     parser.addoption("--target", action='store', default='target.json')

