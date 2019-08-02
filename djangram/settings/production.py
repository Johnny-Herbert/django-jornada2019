from djangram.settings import base

SECRET_KEY = 'i6jltnq+u_nrd66i3#y0mts$nf0&#jsgpz-k4!)9@yy3@bdz_5'

DEBUG = False

ALLOWED_HOSTS = [] #todas as urls possiveis para acessar minha aplicação

DATABASES = {

}

#Dropbox

#Social django
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',

    #django
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '824207761985-7jpi4ui3g9pdvgq4uiipec41qt5m81af.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'tmpQTGTG_bLGiMKRopR_s5YZ'

EMAIL_HOST_USER = 'clientejosealcantara@gmail.com'
EMAIL_HOST_PASSWORD = 'cliente123'

DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DROPBOX_OAUTH2_TOKEN = config('DROPBOX_OAUTH2_TOKEN', default='')