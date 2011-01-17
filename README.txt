=====================
Django photo uploader
=====================
An application for uploading photos via email using the Django Framework. Provides functions to connect to an IMAP server and parse photos out of multipart email messages. Also notifies user via email of receipt and provides a link to a web page where the geo-coordinates of user can be obtained using the web browser's geolocation API.

Intended for use with mobile phones equipped with camera, email client, and web browser.

For more information see: http://tenderlovingcode.com/blog/web-apps/django-photo-uploader

Run the included sample project by executing the following command in the directory "sample": python manager.py runserver

To Install:
 1:- Add the photouploader directory to your django project

 2:- Add the photouploader app to your INSTALLED_APPS in settings.py
     INSTALLED_APPS = (,
        ...
		'<project-name>.photouploader',
	  )
 3:- Add the photouploader urls import to urls.py for your project
     urlpatterns = patterns('',
        ...
     	(r'^upload/', include('photouploader.urls')),
     )

 4:- Update the EMAIL and IMAP config settings in your settings.py, namely:
		EMAIL_HOST				email hostname (outgoing)
		EMAIL_HOST_USER 		email username
		EMAIL_HOST_PASSWORD		email password

		IMAP_SERVER				imap server hostname (incoming)
		IMAP_USER				imap username
		IMAP_PSWD				imap password

		UPLOAD_EMAIL_FROM = "upload@willperkins.com"
		UPLOAD_EMAIL_SUBJECT = "your uploaded photo"
		

To Test:
 1:- After installing, email a photo to your pickup email address

 2:- Run the command: python manager.py fetchmail

 3:- Start your web server by running the command: python manager.py runserver

 4:- In the email reply that you received from the app, click the hyperlink to geo-tag your image.
