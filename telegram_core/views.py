import json

from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.http import Http404
from django.http.response import JsonResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.conf import settings
from telebot.types import Update

from telegram_core.telegram import TgProvider


@method_decorator(csrf_exempt, name='dispatch')
class TelegramUpdateView(View):
    """"""
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        update: Update = Update.de_json(json.loads(request.body))
        TgProvider.dispatch(update)
        return JsonResponse({}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class TelegramWebappView(TemplateView):
    http_method_names = ['get']
    template_name = 'webapp.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ManualSetWebhookView(TemplateView):
    """"""
    http_method_names = ['get']
    template_name = 'webhook.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            raise Http404
        
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = {}
        context.update({
            'token': settings.TELEGRAM_BOT_TOKEN,
            'base_url': settings.BASE_URL
        })
        return context


class CheckWebhook(View):
    http_method_names = ['get']

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            raise Http404

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(
            'https://api.telegram.org/bot{token}/getWebhookInfo'.format(
                token=settings.TELEGRAM_BOT_TOKEN
            )
        )
