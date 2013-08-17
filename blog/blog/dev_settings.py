SESSION_COOKIE_DAYS = 90
SESSION_COOKIE_AGE = 60 * 60 * 24 * SESSION_COOKIE_DAYS 

DEV_TEMPLATE_CONTEXT_PROCESSORS = (
    #'notification.context_processors.notification', 
    )

DEV_MIDDLEWARE_CLASSES = (
    )

DEV_INSTALLED_APPS = (
    #posts
    'posts',
    #tags
    'tags',
    #rest_framework
    'rest_framework',
    #south
    'south',
)

#rest framework settings
REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    )
}