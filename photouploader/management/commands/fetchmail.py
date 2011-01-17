from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from django.core.urlresolvers import reverse

from photouploader.models import Photo

UPLOAD_CONTENT_TYPES = (
    ('image/jpeg','.jpg'),
    ('image/png','.png'),
)

class Command(BaseCommand):
	help = 'fetches new photos from the mail server'
	
	def handle(self,*args,**options):
	    print 'fetching mail'
	    
	    # make sure these are in the path
	    from photouploader.utils import MailBox, extract, notify_sender
	    from photouploader.models import Photo
	    import settings
	    
	    content_types = dict(UPLOAD_CONTENT_TYPES)
	    
	    # go through inbox and save photos to disk
	    inbox = MailBox(settings.IMAP_SERVER, settings.IMAP_USER, settings.IMAP_PSWD)
	    for message in inbox:
	        
	        # extract all 'image files' from email and create an image
	        for ctype, data in extract(message,content_types.keys()):
	            photo = Photo()
	            photo.image.save(photo.receipt+content_types[ctype],ContentFile(data))
	            # send user a verification email
	            print "notifying: %s about %s" % (message['Return-Path'],photo.receipt)
	            notify_sender(recipients=message['Return-Path'],
	                          subject=settings.UPLOAD_EMAIL_SUBJECT,
            	              sender=settings.UPLOAD_EMAIL_FROM,
	                          preview_url=settings.SITE_URL+reverse('photouploader.views.preview',args=[photo.receipt]))
	    
	    del inbox
