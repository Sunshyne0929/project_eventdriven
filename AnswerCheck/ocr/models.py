from django.db import models

class AnswerSheet(models.Model):
    image = models.ImageField(upload_to='answersheets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
