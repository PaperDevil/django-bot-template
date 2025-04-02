from django.conf import settings


def vite_enabled(request):
    return {
        'vite_enabled': settings.DEBUG
    }
