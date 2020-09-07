from django.db import models

# Create your models here.
class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract=True

class Team(BaseModel):
    name = models.CharField(max_length=255)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'date_created': self.date_created,
            'date_modified': self.date_modified
        }


class Player(BaseModel):
    name = models.CharField(max_length=255)
    number = models.SmallIntegerField(null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'number': self.number,
            'team': self.team,
            'date_created': self.date_created,
            'date_modified': self.date_modified
        }

