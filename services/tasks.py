from celery import shared_task
from django.core.mail import EmailMessage,send_mail
from queryraiservibrance.settings import DEFAULT_FROM_EMAIL as me

@shared_task(bind=True)
def approval_mail(self,query):
    email = query.email
    subject = 'Ticket Reference - {ticket} - Query Approval'.format(ticket = query.slug)
    content = ''' Dear {name},

I hope this email finds you well. This is regarding the query that you raised with the Vibrance technical team, which was assigned the ticket number {ticket}.

I am pleased to inform you that your query has been reviewed and approved for resolution. Our team is working on resolving the issue and we will provide you with an update on its progress as soon as possible.

If you require any further assistance or have additional questions, please do not hesitate to reach out to us.

Thank you for your understanding and cooperation.

Best regards,

Vibrance Technical Team
    '''.format(name = query.user_name,ticket = query.slug)
    message = EmailMessage(subject,content,me,[email])
    message.send()

@shared_task(bind=True)
def send_reference_mail(self,query):
    email = query.email
    subject = 'Ticket Reference - {ticket} - Query Update'.format(ticket = query.slug)
    content = '''Dear {name},

I hope this email finds you well. This is regarding the query that you raised with the Vibrance technical team. I am pleased to inform you that your query has been assigned the ticket number {ticket}.

We have received your query and our team is currently working on it. Our team will provide you with an update on the status of your query as soon as possible.

If you require any further assistance or have additional questions, please do not hesitate to reach out to us.

Thank you for your patience and understanding.

Reference Id = {ticket}

Kindly Use this reference Id to check the status of your query.

Best regards,

Vibrance Technical Team
    '''.format(name = query.user_name,ticket = query.slug)
    message = EmailMessage(subject,content,me,[email])
    message.send()

@shared_task(bind=True)
def rejection_mail(self,query):
    email = query.email
    subject = 'Ticket Reference - {ticket} - Query Rejection'.format(ticket = query.slug)
    content = '''Dear {},

I hope this email finds you well. This is regarding the query that you raised with the Vibrance technical team, which was assigned the ticket number {}.

I regret to inform you that your query has been reviewed and rejected due to inconsistent information. Our team has determined that the issue cannot be resolved within the scope of our technical support services.

However, we would be happy to assist you with any alternative solutions that may be available. Please let us know if you would like us to explore any other options for you.

We apologize for any inconvenience this may have caused and appreciate your understanding.

Best regards,

Vibrance Technical Team
    '''.format(name = query.user_name,ticket = query.slug)
    message = EmailMessage(subject,content,me,[email])
    message.send()