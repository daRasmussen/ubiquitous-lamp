from enum import Enum


class Names(str, Enum):
    INDEX = "index"
    REGISTER_USER = "register_user"
    LOGIN_USER = "login_user"
    LOGOUT_USER = "logout_user"


class Titles(str, Enum):
    INDEX = "Blocket"
    REGISTER_USER = "Sign Up"
    LOGIN_USER = "Log In"


class Locations(str, Enum):
    INDEX = "main/index.html"
    REGISTER_USER = "account/register_user.html"
    LOGIN_USER = "account/login_user.html"

