from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .utils import send_email, create_message, SCOPES
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


from .models import reminderBase
from .forms import reminderForm

from django.contrib.auth.mixins import LoginRequiredMixin

class index(LoginRequiredMixin, generic.ListView):
    template_name = 'reminders/index.html'
    context_object_name = "latestReminderList"

    def get_queryset(self):
        # Get sort parameter from the request, default is by 'reminderDueDateEnd'
        sort_by = self.request.GET.get('sort', 'reminderDueDateEnd')
        # Return reminders for the logged-in user sorted by the selected field
        return reminderBase.objects.filter(
            user=self.request.user,
            reminderCompletion=False
        ).order_by(sort_by)


class completedReminders(LoginRequiredMixin, generic.ListView):
    template_name = 'reminders/index.html'
    context_object_name = "latestReminderList"

    def get_queryset(self):
        # Get sort parameter from the request, default is by 'reminderDueDateEnd'
        sort_by = self.request.GET.get('sort', 'reminderDueDateEnd')
        # Return reminders for the logged-in user sorted by the selected field
        return reminderBase.objects.filter(
            user=self.request.user,
            reminderCompletion=True
        ).order_by(sort_by)


def reminder(request, reminders_id):
    return HttpResponse("You're looking at reminder %s." % reminders_id)
def detail(request, reminders_id):
    try:
        reminder = reminderBase.objects.get(pk=reminders_id)
    except reminderBase.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "reminders/detail.html", {"reminder": reminder})

def createReminder(request):
    if request.method == 'POST':
        form = reminderForm(request.POST)
        if form.is_valid():
            new_reminder = form.save(commit=False)
            new_reminder.user = request.user  # Set the user to the current user
            new_reminder.save()
            return redirect('reminders:index')
    else:
        form = reminderForm()
    return render(request, 'reminders/createReminder.html', {'form': form})

def toggleCompletion(request, reminder_id):
    reminder = get_object_or_404(reminderBase, pk=reminder_id)
    if reminder.reminderCompletion == True:
        reminder.reminderCompletion = False
        reminder.save()
        return HttpResponseRedirect(reverse('reminders:completedReminders'))  # Redirect back to the index
    else:
        reminder.reminderCompletion = True
        reminder.save()
        return HttpResponseRedirect(reverse('reminders:index'))  # Redirect back to the index

def editReminder(request, reminder_id):
    reminder = get_object_or_404(reminderBase, pk=reminder_id)
    if request.method == 'POST':
        form = reminderForm(request.POST, instance=reminder)
        if form.is_valid():
            editedReminder = form.save(commit=False)  # Save the form to the model but don't commit to the database yet
            editedReminder.reminderCompletion = False  # Reset the completion status to False
            editedReminder.save()
            return redirect('reminders:index')  # Redirect to the index where only incomplete reminders are listed
    else:
        form = reminderForm(instance=reminder)
    return render(request, 'reminders/editReminder.html', {'form': form})

def deleteReminder(request, reminder_id):
    reminder = get_object_or_404(reminderBase, pk=reminder_id)
    if request.method == 'POST':
        reminder.delete()
        return HttpResponseRedirect(reverse('reminders:completedReminders'))
    return HttpResponse("Method not allowed", status=405)


@login_required
def sendReminderEmail(request):
    user_email = request.user.email
    reminders = reminderBase.objects.filter(user=request.user, reminderCompletion=False)
    email_body = "Here is your requested reminder:\n\n"
    for reminder in reminders:
        email_body += f"Title: {reminder.reminderDescription}\n"
        email_body += f"Details: {reminder.reminderDetails}\n"
        email_body += f"Start: {reminder.reminderDueDateStart} - End: {reminder.reminderDueDateEnd}\n"
        email_body += f"Importance: {reminder.reminderImportance}\n\n"

    subject = "Your TaskFlows Reminders"

    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('gmail', 'v1', credentials=creds)
    message = create_message(user_email, user_email, subject, email_body)
    send_email(service, 'me', message)

    return HttpResponseRedirect('/reminders/?email_sent=true')

