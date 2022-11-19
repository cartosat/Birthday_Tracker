# Birthday Tracker 
Birthday Tracker is a full-fledged web application developed using Python's popular web framework Django. I have tried to understand Django's `Model View Template (MVT)` architecture and user authentication using email. I also overrided the generic username authentication in Django and used email instead. I have used a third-party module called "phonenumber_field" to save phone numbers.


# Technology Stack
- Python
- Django
- SQLite
- HTML
- CSS 
- Javascript

## Features of Birthday Tracker :-
- User registration with email.`(without username)`
- User login with email & password.
- User specific dashboarder of friend's birthday.
- Confetti on profile on birthday.
- Beautiful date picker.
- Add new friend and edit their data.
- Strong search bar with Multi-Field search.
- Countdown for birthday at friend's profile section.
- Each friend card is clickable.

## Third party libraries :-
1. [MC Datepicker](https://mcdatepicker.netlify.app/).
2. [Confetti](https://www.cssscript.com/confetti-falling-animation/).
3. [phonenumber_field](https://github.com/stefanfoulis/django-phonenumber-field).
4. Birthday Countdown (Not library, But used Javascript code).

# How to start web application
- Clone Repo [https://github.com/cartosat/Birthday_Tracker](https://github.com/cartosat/Birthday_Tracker).
- Navigate to Birthday Tracker folder and install modules with.
 - `pip install -r requirement.txt` - on windows
 - `pip3 install -r requirement.txt` - on Mac/Linux
 
- In same folder use below command to start Django server
 - execute `python manage.py runserver` - on windows
 - execute `python3 manage.py runserver` - on Mac/Linux
 
- Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser in your browser.

- Now you you can register yourself and login with registered user credentials.
- You can see some default friends on dashboard, those can be disabled from profile section.

