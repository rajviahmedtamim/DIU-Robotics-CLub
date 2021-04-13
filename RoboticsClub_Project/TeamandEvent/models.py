from django.db import models

# Create your models here.
class Event(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='services')
    details = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS)
    date = models.DateTimeField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def imageurl(self):
        if self.image:
            return self.image.url
        else:
            return ""


class DURCPanel(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )
    name= models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    facebook_url = models.CharField(max_length=200,blank=True,null=True)
    github_url = models.CharField(max_length=200,blank=True,null=True)
    twitter_url = models.CharField(max_length=200,blank=True,null=True)
    linkdin_url = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(upload_to='PanelMember')
    details = models.TextField(max_length=200,blank=True,null=True)
    status = models.CharField(max_length=30, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""