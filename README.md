# CREATE AND HOST A GET API ENDPOINT USING PYTHON, DJANGO, AND HEROKU

To ensure a successful completion of this project, here are some prerequisites:
- Have VS Code and some of it's extensions installed.
- Install python (v3.8, v3.9, or 3.10) and virtualenv 
- Create a GitHub account and create a personal access token (PAT)
- Create OpenSSH key pair in your local system and use the public key to create SSH key in GitHub

Below are the steps I followed to implement a MERN STACK for a Todo application that uses a RESTful API.

### 1. Build the Django API Endpoint
I followed the steps below to create the Django Api Endpoint

- Create a Django Project
To create a django project, we first create a directory and virtual environment, install django and other tools needed.
```
# create a directory to house the project
mkdir hngi9-project1

# create a virtual environment
python -m venv .venv && source .venv/Scripts/activate

# install django and djangorestframework
pip install django djangorestframework

# create the requirements.txt file
pip freeze > requirements.txt 

# create a django project in the root directoory
django-admin startproject apiproject .

# create a django app "api" in the root project directory
django-admin startapp api

# sync the database 
python manage.py migrate
```

- Create a superuser to login and manage the database
```
python manage.py createsuperuser --email admin@example.com --username admin
```

- Confirm the superuser can access the database
```
# start the server
python manage.py runserver
```

***To test if the superuser can login and manage the database, open a web browser and enter the address: `http://localhost:8000/admin` or `http://127.0.0.1:8000/admin`. Then use the username and password of the superuser to login.***

- Create a model called "SlackUsers"
To create a model, modify the models.py file in the django app folder "api" as follows:
```
# change to the 'api' directory and open the models.py file
cd api && vi models.py

# copy and paste the code below to the models.py file. Then savee and close the file.
from django.db import models

class SlackUsers(models.Model):
    slackUsername = models.CharField(max_length= 15)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.CharField(max_length= 600)
    
    def __str__(self):
        return self.slackUsername
```

- Modify the admin.py file in the app folder
```
# open the file and add the below code to it
from .models import SlackUsers

admin.site.register(SlackUsers)
```

- Modify the installed_apps section of the settings.py file in the django project folder "apiproject" to look like below
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # My Created Apps
    'api',
]
```

- Sync the changes to the database
```
# Save the changes
python manage.py makemigrations

# sync the changes to the database
python manage.py migrate
```

- Confirm that the models were created and visible in the UI by starting the server using `python manange.py runserver`. Then visit the address: `http://127.0.0.1:8000/admin`.

- Add a test user to the database SlackUser model (table).
There are two ways to achieve that: via code in the terminal or in the admin UI. To add user via code in the terminal, I used the command below:
```
# activate shell for command 
python manage.py shell

# import the model as the terminal is not part of the app
from  api.models import SlackUsers

# add a role to the SlackUsers model (table)
slackuser = SlackUsers(slackUsername="GodChosen", backend=1, age=35, bio="A focused and goal-getting Junior Backend/DevOps Engineer")
```

***Screenshot***
<br />
![Slack Users Added to Database Table](screenshots/slack-users-added.PNG)

## 2. Build the API Endpoint
To build the API endpoint, we would use the Django REST Framework and Serializer that help to convert SQL to JSON. Earlier, we installed `djangorestframework`. Now, we would proceed to define the the serializer.

- Create a module `serializers.py` in the app folder 'api'
```
# change to the 'api' directory and create the file 'serializers.py'
cd api && touch serializers.py

# copy and paste the code below into the file and save it
from api.models import SlackUsers
from rest_framework import serializers

class SlackUsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SlackUsers
        fields = ["url", "slackUsername", "backend", "age", "bio"]
```

***Note that we're using hyperlinked relations in this case with HyperlinkedModelSerializer. You can also use primary key and various other relationships, but hyperlinking is good RESTful design.***

- Modify the module `views.py` in the app folder 'api'
We will define our viewsets in order to send our data from our backend to the browser
```
# copy and paste the code below into the file and save it
from api.models import SlackUsers
from rest_framework import viewsets

From .serializers import SlackUsersSerializer
class SlackUsersViewSet(viewsets.ModelViewSet):
    # API endpoint that allows slack users to be viewed or edited.
    
    queryset = SlackUsers.objects.all().order_by('-slackUsername')
    serializer_class = SlackUsersSerializer
```

***Django Rest Framework gives us these viewsets for standard CRUD operations on a SQL database. The viewsets accept and handle GET, POST, PUT and DELETE requests, as well as allow for a single endpoint to handle requests for list views of objects in the database and for individual object instances***

- Modify the module `urls.py` in the project folder 'apiproject'
To tell Django what views to return given a particular route, we will import `include` and `path` from the `django.urls` module, as well as routers from Django Rest Framework. To do so, we will modify the `urls.py` by including the following code
```
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'slackusers', views.SlackUsersViewSet)
# Setup automatic URL routing
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

- Modify the file `settings.py` in the project folder 'apiproject'
Add the code below to the file to allow us to control how many objects per page are returned.
```
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5
}
```

- Still modifying the file `settings.py` in the project folder 'apiproject', add the code to the installed apps section.
```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

***Postman API Test***
<br />
![Postman API Test](screenshots/postman-api-test.PNG)

***Browser API Test***
<br />
![Browser API Test](screenshots/browser-api-test.PNG)

