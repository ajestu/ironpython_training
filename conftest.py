import pytest
import os.path
from fixture.application import Opplication
import importlib
import json


fixture = None
target= None

@pytest.fixture
def app(request):
    global fixture
    link = load_config(request.config.getoption("--target"))
    if fixture is None or not fixture.is_valid():
        fixture =  Opplication(link)
    return fixture

@pytest.fixture()
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--target", action="store",  default="target.json")
    parser.addoption("--check_ui", action="store_true")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata=load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
       # elif fixture.startswith("json_"):
       #     testdata=load_from_json(fixture[5:])
       #     metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s"% module).testdata

'''def load_from_json(file):
  with open( os.path.join(os.path.dirname(os.path.abspath(__file__)), "data\\%s.json"%file)) as f:
      return jsonpickle.decode(f.read())
'''

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


