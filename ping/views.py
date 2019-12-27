from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import django_rq
from .tasks import *


@csrf_exempt
def t001(request):
    """ a function-based view"""
    try:
        task_id = django_rq.enqueue(sleep_10)
        return HttpResponse("Enqueued %s" % task_id)
    except Exception as e:
        return HttpResponse(e)
