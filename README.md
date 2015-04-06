# wibi
##### Web Interaction Based Intervention

<hr>
This application includes data models defined using django ORM. These models are revealed to the client via a REST API for consumption by an Ember Single Page Application (SPA). The SPA will reside within an in-app web browser. Some buttons will trigger certain actions within the app, such as video recording.

<hr>

### Installation
You should use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) and [pip](https://pypi.python.org/pypi/pip).

You will need [node](https://nodejs.org/) to install ember-cli.

 1. pip install -r requirements.txt
 2. ./manage.py syncdb
 3. ./manage.py migrate
 4. npm install -g ember-cli
 5. cd project/static/wibi && ember build
 6. ./manage.py runserver

#### Directory Layout

```
project/
├── static/                 emberjs in here under wibi/
├── apps/
│   ├── hv_curriculum/      models --> REST API
│   ├── pals_curriculum/    models --> REST API
│   ├── userdata/           models --> REST API
│   └── videoplay/          models --> redis --> REST API
└── project/
    ├── settings.py
    ├── ...
    └── views.py            >> delivers index.html ember app from dist/
```

#### Backend Docs
 - [Django REST](http://www.django-rest-framework.org/)
 - [Gunicorn](http://gunicorn.org/#docs)
 - [Python Interface to Redis](https://pypi.python.org/pypi/redis/)
 - [Markdown](http://pythonhosted.org//Markdown/)

#### Frontend Docs
 - [Ember API](http://emberjs.com/api/)
 - [Bootstrap](http://getbootstrap.com/)


