from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=50, primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at',)

class Comment(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    stars = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at',)

# Create your models here.
