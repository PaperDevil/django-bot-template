import json

from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.http import Http404
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from telebot.types import Update

from telegram_core.telegram import TgProvider


@method_decorator(csrf_exempt, name='dispatch')
class TelegramUpdateView(View):
    """

    """
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        update: Update = Update.de_json(json.loads(request.body))
        TgProvider.dispatch(update)
        return JsonResponse({}, status=200)


class ManualSetWebhookView(TemplateView):
    """"""
    http_method_names = ['get']
    template_name = ''

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            raise Http404

    def get_context_data(self, **kwargs):...
