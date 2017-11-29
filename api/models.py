from django.db import models

class Question(models.Model):
    category = models.CharField(max_length=50)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.category, self.question)
