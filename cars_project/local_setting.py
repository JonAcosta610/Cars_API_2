# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gw!#gj_r6b#@gs=y*sqy5fk86sig$m_()ne)k&5y=2(f9i$+)x'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'jonjon87',
    }
}
