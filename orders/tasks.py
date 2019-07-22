from celery import task
from django.core.mail import send_mail
from .models import Order
@task
def order_created(order_id):
    """
    Отправка сообщения о создании покупки
    """
    order = Order.objects.get(id=order_id)
    subject = 'Заказ с номером {}'.format(order.id)
    message = 'Дорогой, {}, вы успешно сделали заказ.\
              Номер вашего заказа {}'.format(order.first_name, order_id)
    mail_send = send_mail(subject, message, 'admin@myproject.com', [order.email])
    return mail_send
