from enum import Enum


class Names(str, Enum):
    INDEX = "index"
    REGISTER_USER = "register_user"
    PROFILE = "profile"


class Titles(str, Enum):
    INDEX = "Blocket"
    REGISTER_USER = "Sign Up"


class Locations(str, Enum):
    INDEX = "main/index.html",
    REGISTER_USER = "account/register_user.html",

