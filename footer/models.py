from django.db import models

# Create your models here.

class FooterSettings(models.Model):
    label_number = models.CharField(max_length=100)
    label_email = models.CharField(max_length=100)
    label_address = models.CharField(max_length=100)    
    label_social = models.CharField(max_length=100)   
    text_number = models.CharField(max_length=100, null=True, blank=True)
    text_email = models.CharField(max_length=100, null=True, blank=True)
    text_address = models.CharField(max_length=100, null=True, blank=True)    
    text_social = models.CharField(max_length=100, null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class FooterCategory(models.Model):
    footer = models.ForeignKey(FooterSettings, on_delete=models.CASCADE, related_name="categories")
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    
class FooterItem(models.Model):
    category = models.ForeignKey(FooterCategory, on_delete=models.CASCADE, related_name="items")
    label = models.CharField(max_length=100)
    link = models.URLField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label