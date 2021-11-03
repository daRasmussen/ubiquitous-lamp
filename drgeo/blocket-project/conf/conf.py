from enum import Enum


class Names(str, Enum):
    INDEX = "index"
    REGISTER_USER = "register_user"
    LOGIN_USER = "login_user"
    LOGOUT_USER = "logout_user"
    USER_PROFILE = "profile"


class Titles(str, Enum):
    INDEX = "Blocket"
    REGISTER_USER = "Sign Up"
    LOGIN_USER = "Log In"
    USER_PROFILE = "Profile"


class Locations(str, Enum):
    INDEX = "main/index.html"
    REGISTER_USER = "account/register_user.html"
    LOGIN_USER = "account/login_user.html"
    USER_PROFILE = "user_profile/index.html"

