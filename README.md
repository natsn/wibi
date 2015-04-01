# wibi
##### Web Interaction Based Intervention

<hr>
This application includes data models defined using django ORM. These models are revealed to the client via a REST API for consumption by an Ember Single Page Application (SPA). The SPA will reside within an in-app web browser. Some buttons will trigger certain actions within the app, such as video recording.

<hr>

#### Directory Layout

```
project/
├── static/                 emberjs
├── apps/
│   ├── main/               url --> view --> emberjs
│   ├── hv_curriculum/      models --> REST API
│   ├── pals_curriculum/    models --> REST API
│   ├── userdata/           models --> REST API
│   └── videoplay/          models --> redis --> REST API
└── project/
    ├── settings.py
    └── ...
```

#### Backend Docs
 - [Django REST](http://www.django-rest-framework.org/)
 - [Gunicorn](http://gunicorn.org/#docs)
 - [Python Interface to Redis](https://pypi.python.org/pypi/redis/)
 - [Markdown](http://pythonhosted.org//Markdown/)

#### Frontend Docs
 - [Ember API](http://emberjs.com/api/)
 - [Bootstrap](http://getbootstrap.com/)


