import sys
import httpx
from urllib.parse import urlparse

from django.apps import AppConfig
from django.urls import reverse
from django.conf import settings


class TelegramCoreConfig(AppConfig):
    name = 'telegram_core'
    running = False

    def ready(self):
        if not settings.DEBUG or sys.argv[1] != 'runserver':
            TelegramCoreConfig.init_webhooks(settings.BASE_URL)
            return

        if settings.USE_NGROK:
            from pyngrok import ngrok

            # Get current dev server port (default 8000 for Django)
            addrport = urlparse("htpp://{}".format(sys.argv[-1]))
            port = addrport.port if addrport.netloc and addrport.port else "8000"

            # Create ngrok tunnel to dev server
            public_url = ngrok.connect(port).public_url
            print("ngrok tunnel '{}' => 'http://127.0.0.1:{}'".format(public_url, port))

            # Update any base URLs for webhooks to use public ngrok URL
            settings.BASE_URL = public_url
            TelegramCoreConfig.init_webhooks(public_url)
        else:
            TelegramCoreConfig.init_webhooks(settings.BASE_URL)

    @staticmethod
    def init_webhooks(url):
        # Setup telegram webhooks
        tg_webhook = url + reverse('telegram_core:update')
        print('Telegram webhook url set -> {}'.format(tg_webhook))

        httpx.post(
            url='https://api.telegram.org/bot{}/setWebhook'.format(settings.TELEGRAM_BOT_TOKEN),
            json={'url': tg_webhook}
        )

        # initialize telegram bot handlers after set webhook
        from telegram_core import handlers
