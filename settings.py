from django.conf import settings

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'sample.db'

# outgoing mail
EMAIL_HOST = <email server>
EMAIL_HOST_USER = <username>
EMAIL_HOST_PASSWORD = <password>
UPLOAD_EMAIL_FROM = <from email address>
UPLOAD_EMAIL_SUBJECT = <email subject>
# incoming mail
IMAP_HOST = <imap server>
IMAP_USER = <username>
IMAP_PSWD = <password>
# your site's domain
SITE_URL = 'http://tenderlovingcode.com'

MEDIA_ROOT = '/path/to/public/images'
MEDIA_URL = 'http://localhost:8000/images/'

SITE_URL = 'http://localhost:8000'

ROOT_URLCONF = 'sample.urls'

INSTALLED_APPS = (
	'sample.photouploader'
)
