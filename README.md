# Birthday Tracker 
Birthday Tracker is a full-fledged web application developed using Python's popular web framework Django. I have tried to understand Django's `Model View Template (MVT)` architecture and user authentication using email. I also overrided the generic username authentication in Django and used email instead. I have used a third-party module called "phonenumber_field" to save phone numbers.


# Technology Stack
- Python
- Django
- SQLite
- HTML
- CSS 
- Javascript

# Application Preview Video :-
https://user-images.githubusercontent.com/34335127/202908310-4810d2ee-6277-4845-8571-529fac356b33.mp4

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

## Screen Shots of Application :-
1) User DashBoard :-
<img width="1435" alt="Screenshot 2022-11-20 at 7 53 09 PM" src="https://user-images.githubusercontent.com/34335127/202908143-50df2429-31bb-4165-bf91-43a0bbe01c59.png">

2) Register Page :-
<img width="1428" alt="Screenshot 2022-11-20 at 7 52 49 PM" src="https://user-images.githubusercontent.com/34335127/202908163-6ac51510-c5d9-4d4c-974d-c9c76c1cfc92.png">

3) Login Page
<img width="1433" alt="Screenshot 2022-11-20 at 7 52 34 PM" src="https://user-images.githubusercontent.com/34335127/202908177-06d3f1a5-3bb8-49bb-a927-fa218070b156.png">


4) User Profile
<img width="1427" alt="Screenshot 2022-11-20 at 7 55 30 PM" src="https://user-images.githubusercontent.com/34335127/202908106-6fd815e0-5e0c-4a27-8953-40586c5ef552.png">

5) Add Friend :-
<img width="1433" alt="Screenshot 2022-11-20 at 7 55 08 PM" src="https://user-images.githubusercontent.com/34335127/202908119-8cfb3cec-cb23-49e2-8267-a7d0e9e97b14.png">

6) Search Bar :-
 <img width="588" alt="Screenshot 2022-11-20 at 7 53 58 PM" src="https://user-images.githubusercontent.com/34335127/202908129-d33a3f9e-775f-4203-89c4-c5f6b13fc9c6.png">

7) Dashboard and Footer :-
<img width="1434" alt="Screenshot 2022-11-20 at 7 53 29 PM" src="https://user-images.githubusercontent.com/34335127/202908133-0a54e04d-7132-47f9-8988-4a305122a53c.png">

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

