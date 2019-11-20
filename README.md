======================
django-adlh-contact
======================

Just a reusable contact form with a captcha field and support for EN/DE

Quick start
-----------

1) Add app to settings.py:
```python
# setting.py
INSTALLED_APPS = (
    ...
    'contact',
)
```


2) Use the built-in templates (bootstrap 3) or replace with your own.

3) Include the urls:
```python
path(r'contakt/', include('contact.urls')),
```

4) Run the migrations with `python manage.py migrate`.

5) That's it! 
