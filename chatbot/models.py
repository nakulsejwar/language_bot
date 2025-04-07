# chatbot/models.py
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    known_language = models.CharField(max_length=100)
    target_language = models.CharField(max_length=100)
    level = models.CharField(max_length=50)

class Mistake(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    original_input = models.TextField()
    corrected_input = models.TextField()
    mistake_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
