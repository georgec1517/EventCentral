from django.db import models

# Create your models here.
class Venue(models.Model):
    name=  models.CharField('Venue Name', max_length=100)
    address=  models.CharField(max_length=300)
    zip_code=  models.CharField(max_length=15)
    phone=  models.CharField(max_length=25)
    web=  models.URLField('Website Address')
    email_address=  models.EmailField('Email Address')


class EventCentralUser(models.Model):
    first_name =  models.CharField(max_length=30)
    last_name =  models.CharField(max_length=30)
    email = models.EmailField('User Email')
    def __str__(self):
        return self.first_name + ' ' + self.last_name


DEPT_CHOICES = (
    ('Computer Science and Engineering','CSE'),
    ('Mechanical Engineering', 'ME'),
    ('Civil Engineering','CE'),
    ('Electrical Engineering','EEE'),
    ('Electronics and Communication','ECE'),
    ('CIDRIE','CIDRIE'),
    ('All Departments','OPEN'),
)

class Event(models.Model):
    name = models.CharField('Event Name', max_length=100)
    event_date = models.DateField('Event Date')
    description = models.TextField()
    opentodept = models.CharField(max_length=50, choices=DEPT_CHOICES)
    event_image = models.ImageField(null=True, blank=True, upload_to="images/")
    #fromdept =
    def __str__(self):
        return self.name