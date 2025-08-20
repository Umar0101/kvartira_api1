from decouple import config
from celery import shared_task # декоратор , чтоб селери понимал , что наша функуия таск
from django.core.mail import send_mail



HOST = config('HOST_FOR_SEND_MAIL')

@shared_task
def send_activation_email(email, activation_code):
    activation_url = f'{HOST}/account/activate/?u={activation_code}'
    message = ""
    html = f"""
<h1> для активации нажмите на кнопку </h1>
<a href="{activation_url}">
<button>Activate</button>
</a>
"""
    send_mail(
        subject='Активация аккаунта',
        message=message,
        from_email="a@gmail.com",
        recipient_list=[email],
        html_message=html
    )


# def send_reset_password(user):
#     code = user.activation_code
#     to_email = user.email 
#     send_mail(
#         subject='Востановление пароля',
#         message=f'Код для востанавления пароля {code}',
#         from_email='a@gmail.com',
#         recipient_list=[to_email],
#         fail_silently=False
#     )