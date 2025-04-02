from django.urls import re_path

from telegram_core import views

app_name = 'telegram_core'

urlpatterns = [
    re_path(
        r'^update/$',
        views.TelegramUpdateView.as_view(),
        name='update'
    ),
    re_path(
        r'^set_webhook/$',
        views.ManualSetWebhookView.as_view()
    )
]
