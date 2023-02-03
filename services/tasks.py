from celery import shared_task
from django.core.mail import EmailMessage,send_mail
from queryraiservibrance.settings import DEFAULT_FROM_EMAIL as me

@shared_task(bind=True)
def approval_mail(self,query):
    email = query.email
    subject = 'Approval Mail - {}'.format(query.title)
    content = ''' Howdy, {}! We hope that you are doing well. This email serves as confirmation that the query {} with referenced id {} submitted on {} has been resolved by our team.
We appreciate your patience.
Best Regards
VITC Events Team
    '''.format(query.user_name,query.slug,query.title,query.date_of_creation.date())
    message = EmailMessage(subject,content,me,[email])
    message.send()

@shared_task(bind=True)
def send_reference_mail(self,query):
    email = query.email
    subject = 'Reference Mail - {}'.format(query.title)
    content = ''' Howdy, {}! We hope that you are doing well. This email serves as confirmation that the query {} with referenced id {} submitted on {} has been received by our team and will be investigated further.
We appreciate your patience.
Reference Id : {}
Use this reference id for checking status.
Best Regards
VITC Events Team
    '''.format(query.user_name,query.slug,query.title,query.date_of_creation.date(),query.slug)
    message = EmailMessage(subject,content,me,[email])
    message.send()

@shared_task(bind=True)
def rejection_mail(self,query):
    email = query.email
    subject = 'Rejection Mail - {}'.format(query.title)
    content = ''' Howdy, {}! We hope that you are doing well. This email serves as confirmation that your query {} with reference id  {} submitted on {} was denied by our team due to certain charges. We will shortly contact you.
We appreciate your patience.
Best Regards
VITC Events Team
    '''.format(query.user_name,query.slug,query.title,query.date_of_creation.date())
    message = EmailMessage(subject,content,me,[email])
    message.send()