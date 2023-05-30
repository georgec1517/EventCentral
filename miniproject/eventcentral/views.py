from django.shortcuts import render,redirect
from .models import Event
from .forms import EventForm
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    event_list = Event.objects.all().order_by('opentodept')
    return render(request, 'eventcentral/home.html', {'event_list': event_list,} )




def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'eventcentral/event_list.html', {'event_list' : event_list})

def add_event (request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'eventcentral/add_event.html', {'form':form, 'submitted' : submitted})


def update_event(request, event_id):
    event=Event.objects.get(pk=event_id)
    form=EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    return render(request,'eventcentral/update_event.html',
                  {'event': event,
                   'form': form})