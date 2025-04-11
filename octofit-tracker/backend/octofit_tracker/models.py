from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    password = models.CharField(max_length=255)
    class Meta:
        db_table = 'users'
        app_label = 'octofit_tracker'

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    members = models.JSONField()
    class Meta:
        db_table = 'teams'
        app_label = 'octofit_tracker'

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()
    class Meta:
        db_table = 'activity'
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user = models.CharField(max_length=255)
    score = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
        app_label = 'octofit_tracker'

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    class Meta:
        db_table = 'workouts'
        app_label = 'octofit_tracker'
