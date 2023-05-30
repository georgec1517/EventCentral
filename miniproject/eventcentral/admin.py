from django.contrib import admin
from .models import Venue
from .models import EventCentralUser
from .models import Event

# Register your models here.
admin.site.register(Venue)
admin.site.register(EventCentralUser)
admin.site.register(Event)