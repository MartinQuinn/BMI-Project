# Martin Quinn 24-01-2019
# PTA18070

SECRET_KEY = '874m7ky=7wb$l@fbyd7$g-+34to6-=2e3rk^^upj$qo&=!cx-tsecure'

ALLOWED_HOSTS = ['68.183.32.33','bmindex.info','www.bmindex.info']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bmidb',
        'USER': 'djangoadmin',
        'PASSWORD': 'Stsennevrz6r8y',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEBUG = False
