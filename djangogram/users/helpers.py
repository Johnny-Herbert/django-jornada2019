#django send email
from django.conf import settings
from templated_email import send_templated_mail

def send_confirm_user_signup_email(user):
    kwargs = dict(
        template_name='signup_user',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        context={
            'user':user,
        }
    )
    import ipdb; ipdb.set_trace()
    return send_templated_mail(**kwargs)