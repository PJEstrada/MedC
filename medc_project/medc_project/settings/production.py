from django.conf import settings


DEBUG = False
TEMPLATE_DEBUG = True


DATABASES = settings.DATABASES

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Enable Connection Pooling
DATABASES['default']['ENGINE'] = 'django_postgrespool'

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/static/'
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
