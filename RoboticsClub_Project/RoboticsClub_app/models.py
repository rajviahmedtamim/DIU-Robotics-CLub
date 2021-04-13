from django.db import models
from django.forms import ModelForm, TextInput, EmailInput


class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    club = models.CharField(max_length=50)
    address = models.TextField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=50)
    smtpemail = models.CharField(blank=True, max_length=50)
    smtppassword = models.CharField(blank=True, max_length=10)
    smptport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    aboutus = models.TextField(blank=True)
    project_completed = models.IntegerField(blank=True)
    club_member = models.IntegerField(blank=True)
    award_achivement = models.IntegerField(blank=True)
    contest_participation = models.IntegerField(blank=True)
    contact = models.TextField(blank=True)
    reference = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=40)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField(max_length=1000, blank=True)
    status = models.CharField(max_length=40, choices=STATUS, default='New')
    ip = models.CharField(max_length=100, blank=True)
    Note = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets={
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Name & Sure name'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Write your email'}),
            'message': TextInput(attrs={'class': 'input', 'placeholder': 'Write your message'}),
        }


class AboutCateory(models.Model):
    title = models.CharField(max_length=80)
    details = models.CharField(max_length=500)
    who_we_are = models.TextField(blank=True)
    what_we_do = models.TextField(blank=True)

    def __str__(self):
        return self.title


class DURCGallery(models.Model):
    status = (
        ('True','True'),
        ('False','False'),
    )
    title = models.CharField(max_length=20)
    detail = models.TextField(max_length=100)
    image = models.ImageField(upload_to='DURC_Gallery/')
    status = models.CharField(max_length=20, choices=status)

    def __str__(self):
        return self.title

    def imageurl(self):
        if self.image:
            return self.image.url
        else:
            return ""