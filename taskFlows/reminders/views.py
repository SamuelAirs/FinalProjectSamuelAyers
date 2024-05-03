from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse


from .models import reminderBase
from .forms import reminderForm

class index(generic.ListView):
    template_name = 'reminders/index.html'
    context_object_name = "latestReminderList"

    def get_queryset(self):
        # Filter to show only reminders that have not been marked as complete
        return reminderBase.objects.filter(reminderCompletion=False).order_by("reminderCreationTime")

class completedReminders(generic.ListView):
    template_name = 'reminders/index.html'
    context_object_name = "latestReminderList"

    def get_queryset(self):
        # Filter to show only reminders that have not been marked as complete
        return reminderBase.objects.filter(reminderCompletion=True).order_by("reminderCreationTime")


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