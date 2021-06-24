import random
import requests
from datetime import datetime
from config import BaseResponse, User, Urls


def test_get_login():
    response = requests.get(Urls.URL_LOGIN, params={"login": "Vasiliy", "password": "qwerty"}).text
    message: BaseResponse = BaseResponse.parse_raw(response)
    assert message.code == 200
    assert message.type == "unknown"
    assert message.message.startswith('logged in user session:')


def test_get_logout():
    response = requests.get(Urls.URL_LOGOUT).text
    message: BaseResponse = BaseResponse.parse_raw(response)
    assert message.code == 200
    assert message.type == "unknown"
    assert message.message == "ok"


def test_get_user_not_found():
    response = requests.get(f'{Urls.BASE_URL}some_name').text
    message: BaseResponse = BaseResponse.parse_raw(response)
    assert message.code == 1
    assert message.type == "error"
    assert message.message == 'User not found'


def test_delete_user_not_found():
    response = requests.delete(f'{Urls.BASE_URL}some_name{datetime.now()}')
    assert response.status_code == 404


def test_post_createWithList():
    time = datetime.now().time()
    status = random.randint(1, 10000)
    body = User(
        username=f"python{time}",
        firstName="Ivan",
        lastName="Ivanov",
        email="ivan.ivanov@gmail.com",
        password="top_secret",
        phone="+375440001122",
        userStatus=status
    )

    response = requests.post(Urls.CREATE_WITH_LIST_URL, json=[body.dict()]).text
    message: BaseResponse = BaseResponse.parse_raw(response)
    assert message.code == 200
    assert message.type == 'unknown'
    assert message.message == 'ok'

    response2 = requests.get(f'{Urls.BASE_URL}{body.username}').text
    message2: User = User.parse_raw(response2)
    assert type(message2.id) == int
    assert message2.username == body.username
    assert message2.firstName == body.firstName
    assert message2.lastName == body.lastName
    assert message2.email == body.email
    assert message2.password == body.password
    assert message2.phone == body.phone
    assert message2.userStatus == body.userStatus


def test_post_createWithArray():
    time = datetime.now().time()
    status = random.randint(1, 10000)
    body = User(
        username=f"user{time}",
        firstName="Vladimir",
        lastName="Wrutin",
        email="fair.vova@gmail.com",
        password="1111",
        phone="+375296660033",
        userStatus=status
    )

    response = requests.post(Urls.CREATE_WITH_ARRAY_URL, json=[body.dict()]).text
    message: BaseResponse = BaseResponse.parse_raw(response)
    assert message.code == 200
    assert message.type == 'unknown'
    assert message.message == 'ok'

    response2 = requests.get(f'{Urls.BASE_URL}{body.username}').text
    message2: User = User.parse_raw(response2)
    assert type(message2.id) == int
    assert message2.username == body.username
    assert message2.firstName == body.firstName
    assert message2.lastName == body.lastName
    assert message2.email == body.email
    assert message2.password == body.password
    assert message2.phone == body.phone
    assert message2.userStatus == body.userStatus


def test_create_delete_user():
    time = datetime.now().time()
    status = random.randint(1, 10000)
    body = User(
        username=f"new{time}",
        firstName="Alex",
        lastName="Martin",
        email="alex.alex@gmail.com",
        password="30541alex",
        phone="+375334567890",
        userStatus=status
    )

    response = requests.post(Urls.BASE_URL, json=body.dict()).text
    message: BaseResponse = BaseResponse.parse_raw(response)
    assert message.code == 200
    assert message.type == 'unknown'
    assert type(message.message) == str

    response2 = requests.get(f'{Urls.BASE_URL}{body.username}').text
    message2: User = User.parse_raw(response2)
    assert type(message2.id) == int
    assert message2.username == body.username
    assert message2.firstName == body.firstName
    assert message2.lastName == body.lastName
    assert message2.email == body.email
    assert message2.password == body.password
    assert message2.phone == body.phone
    assert message2.userStatus == body.userStatus

    response3 = requests.delete(f'{Urls.BASE_URL}{body.username}').text
    message3: BaseResponse = BaseResponse.parse_raw(response3)
    assert message3.code == 200
    assert message3.type == 'unknown'
    assert message3.message == body.username

    response4 = requests.get(f'{Urls.BASE_URL}{body.username}')
    message4: BaseResponse = BaseResponse.parse_raw(response4)
    assert message4.code == 1
    assert message4.type == 'error'
    assert message4.message == "User not found"
