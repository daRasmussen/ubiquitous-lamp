from enum import Enum


class Names(str, Enum):
    INDEX = "index"
    REGISTER_USER = "register_user"
    PROFILE = "profile"


class Titles(str, Enum):
    INDEX = "Blocket"
    REGISTER_USER = "Sign Up"
    PROFILE = "My Profile"


class Locations(str, Enum):
    INDEX = "main/index.html",
    REGISTER_USER = "main/register_user.html",
    PROFILE = "main/profile.html"

