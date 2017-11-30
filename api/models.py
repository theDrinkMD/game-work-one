from django.db import models

class Question(models.Model):
    category = models.CharField(max_length=50)
    question = models.TextField()
    definition = models.TextField()
    example = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.category, self.question)

class Player(models.Model):
    name = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.name)

class PlayerResponse(models.Model):
    player_id = models.BigIntegerField()
    player_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.player_id, self.player_response)
