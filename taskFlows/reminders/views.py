from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render

from .models import reminderBase
from .models import reminderDetails


def index(request):
    latestReminderList = reminderBase.objects.order_by("reminderCreationTime")[:5]
    template = loader.get_template("reminders/index.html")
    context = {"latestReminderList": latestReminderList,}
    return HttpResponse(template.render(context,request))

def reminder(request, reminders_id):
    return HttpResponse("You're looking at reminder %s." % reminders_id)
def detail(request, reminders_id):
    try:
        reminder = reminderBase.objects.get(pk=reminders_id)
        reminderD = reminderDetails.objects.get(pk=reminders_id)
    except reminderBase.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "reminders/detail.html", {"reminder": reminder, "reminderD": reminderD})



