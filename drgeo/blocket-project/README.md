#blocket-project
This is a copy of the famous blocket.se site.

#Dependencies
- Python 3.10.0.
- Virtualenv hosted with pyenv.
- Django version (git clone, so latest 4.x)

To activate python virtual env.
```
source venv/bin/activate
```

#blocket
Includes settings for the site.
Created with:
``` 
    python manage.py startproject blocket
    mv blocket blocket-project
```
blocket folder holds settings for projects.

#main
Folder holds main webapp for running blocket. 
Created with:
```
    python manage.py startapp main
```

#Tests and Coverage 
Run specific tests with coverage
```
    coverage run --source "main, account" manage.py test -v 2 && coverage report
```
