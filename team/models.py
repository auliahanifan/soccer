from django.db import models

# Create your models here.
class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract=True

class Team(BaseModel):
    name = models.CharField(max_length=255, null=False)

class Player(BaseModel):
    name = models.CharField(max_length=255, null=False)
    number = models.SmallIntegerField(null=False)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name="player", null=True)