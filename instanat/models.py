from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    image = models.ImageField()
    user = models.ForeignKey(User)
    added_date = models.DateTimeField(auto_now_add=True)

    def get_username(self):
        username = User.objects.get(pk=self.user)
        return username


class Comment(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    text = models.CharField(max_length=256)
    added_date = models.DateTimeField(auto_now_add=True)

    def get_username(self):
        username = User.objects.get(pk=self.user)
        return username


class Like(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)


class Subscribe(models.Model):
    subscriber = models.ForeignKey(User, null=False, related_name='subscriber')
    subscribed_to = models.ForeignKey(User, null=False, related_name='subscribed_to')
