Note, this project is now privately held [here](https://github.com/htrg).

![Logo](wibi_logo.png?raw=true)

# wibi
##### Web Interaction Based Intervention

<hr>
This application includes data models defined using django ORM. These models are revealed to the client via a REST API for consumption by an Angular Single Page Application (SPA). The SPA will reside within an in-app web browser. Some buttons will trigger certain actions within the app, such as video recording.

<hr>

### Installation
You should use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) and [pip](https://pypi.python.org/pypi/pip).

You will need [node](https://nodejs.org/) and [npm](https://www.npmjs.com/)

 1. Install backend requirements: `pip install -r requirements.txt`
 2. Make an sqlite3 database for development `./manage.py syncdb`
 3. Dive into the Angular app `cd project/static/wibi`
 4. Install frontend requirements: `npm install && bower install` (this will create `app/bower_components` and `node_modules/`)
 5. Then go up a couple directories and `./manage.py runserver`

#### Directory Layout


```
project/
├── static/                 Angular.js in here under wibi/
├── utils/                  helpful mixins, middleware etc.
└── project/
    ├── models.py           models --> REST API
    ├── serializers.py      For the django REST Framework
    ├── settings.py         Django settings
    ├── urls.py             catchall for Angular minus /api/ and /admin/
    ├── views.py            >> delivers index.html Angular app from dist/
    └── wsgi.py             server connection setup
```

#### Schema Design
![Schema](project/erd.png?raw=true)

#### Backend Docs
 - [Django REST](http://www.django-rest-framework.org/)
 - [Gunicorn](http://gunicorn.org/#docs)
 - [Python Interface to Redis](https://pypi.python.org/pypi/redis/)
 - [Markdown](http://pythonhosted.org//Markdown/)

#### Frontend Docs
 - [Angular API](https://docs.angularjs.org/api)
 - [Bootstrap](http://getbootstrap.com/)
