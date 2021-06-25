from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    code: int = Field(...)
    type: str = Field(...)
    message: str = Field(...)


class User(BaseModel):
    id: int = Field(None)
    username: str = Field(...)
    firstName: str = Field(...)
    lastName: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    phone: str = Field(...)
    userStatus: int = Field(...)


class Urls:
    URL_LOGIN = 'https://petstore.swagger.io/v2/user/login'
    URL_LOGOUT = 'https://petstore.swagger.io/v2/user/logout'
    BASE_URL = 'https://petstore.swagger.io/v2/user/'
    CREATE_WITH_LIST_URL = 'https://petstore.swagger.io/v2/user/createWithList'
    CREATE_WITH_ARRAY_URL = 'https://petstore.swagger.io/v2/user/createWithArray'

