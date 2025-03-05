import os

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Add these lines if not already present
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
