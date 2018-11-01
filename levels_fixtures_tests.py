import pytest

"""
Уровень фикстуры может принимать следующие возможные значения:
 “function”, 
 “cls”, 
 “module”, 
 “session”. 
Значение по умолчанию = “function”.

function – фикстура запускается для каждого теста
cls – фикстура запускается для каждого класса
module – фикстура запускается для каждого модуля
session – фикстура запускается для каждой сессии (то есть фактически один раз)

"""

@pytest.fixture(scope="function")
def resource_setup(request):
    print("\nconnect to db")
    db = {"Red": 1, "Blue": 2, "Green": 3}

    def resource_teardown():
        print("\ndisconnect")

    request.addfinalizer(resource_teardown)
    return db


def test_db(resource_setup):
    for k in resource_setup.keys():
        print("color {0} has id {1}".format(k, resource_setup[k]))


def test_red(resource_setup):
    assert resource_setup["Red"] == 1


def test_blue(resource_setup):
    assert resource_setup["Blue"] != 1
