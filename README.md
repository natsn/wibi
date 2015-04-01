# wibi
Web Interaction Based Intervention

This application includes data models defined using django ORM. These models are revealed to the client via a REST API for consumption by an Ember SPA.

# Directory Layout

```
project/
├── static/                 emberjs
├── apps/
│   ├── main/               url --> view --> emberjs
│   ├── hv_curriculum/      models --> REST API
│   ├── pals_curriculum/    models --> REST API
│   ├── userdata/           models --> REST API
│   └── video/              models --> redis --> REST API
└── project/
    ├── settings.py
    └── ...
```

# Documentation

## Backend
 - [Django REST](http://www.django-rest-framework.org/)
 - [Gunicorn](http://gunicorn.org/#docs)
 - [Python Interface to Redis](https://pypi.python.org/pypi/redis/)
 - [Markdown](http://pythonhosted.org//Markdown/)

## Frontend
 - [Ember API](http://emberjs.com/api/)
 - [Bootstrap](http://getbootstrap.com/)


