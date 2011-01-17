#!/usr/bin/env python

import email
import imaplib

class MailBox(object):
    """ wrapper for an imap mailbox """
    
    imap  = None # reference to imap server
    index = []   # message index
    
    def __init__(self,server,user,pswd,fetchall=False):
        self.imap = imaplib.IMAP4(server)
    	self.imap.login(user,pswd)
    	self.imap.select()
    	
    	status, data = self.imap.search(None,fetchall and 'ALL' or 'UNSEEN')
    	self.index = data[0].split()
    
    def __del__(self):
        self.imap.logout()
    
    def __iter__(self):
        """ iterate through messages in mailbox """
        for message in self.index:
            status, data = self.imap.fetch(message, '(RFC822)')
            yield email.message_from_string(data[0][1])

def extract(email,content_types=[]):
    """ extracts content with the given content-type from a multi-part email """
    content = []
    for part in email.walk():
        if part.get_content_type() in content_types:
            content.append( (part.get_content_type(),part.get_payload(decode=1)) )
    
    return content


from django.core.mail import EmailMultiAlternatives
from django.template import loader, Context

def notify_sender(recipients,subject,sender,preview_url):
	""" sends email to recipient with a link to a page to review photos """
	
	context = Context({'url':preview_url})
	
	text_part    = loader.get_template('email.txt').render(context)
	html_part    = loader.get_template('email.html').render(context)
	subject_part = loader.get_template_from_string(subject).render(context)
		
	if type(recipients) != list:
		recipients = [recipients,]
		
	msg = EmailMultiAlternatives(subject_part, text_part, sender, recipients)
	msg.attach_alternative(html_part, "text/html")
	return msg.send(False)
