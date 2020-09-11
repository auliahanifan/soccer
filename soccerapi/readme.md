# Soccer API Documentations

___ 

## Requirements

To run this app, you need this:

1. Python 3.7+
2. PostgreSQL (If you want to use this, default use SQLite)

___

## Configurations

This app configuration use virtual environment variables or `.env` file. The example you can check on `example.env`

Here the variables that used:
1. `SECRET_KEY=your-secret-key` its django secret key
2. `USE_CACHE=true` just set `true` if you want to use cache for better performance. It use local memory for cache.
3. `USE_POSTGRES=true` just set `true` if you want to use postgres as database. If you dont set it, default app use SQLite as database.
4. `PG_DB_NAME=your-database-name` just set it with your database name in postgres, have default value `postgres` if you dont set it.
5. `PG_USERNAME=your-user` just set it with your user in postgres, have default value `postgres` if you dont set it.
6. `PG_PASSWORD=password` just set it with your password of user in postgres, have default value empty string `""`  if you dont set it.
7. `PG_HOST=localhost` just set it with your host of postgres, have default value `localhost` if you dont set it.
8. `PG_PORT=5432` just set it with your port of postgres, have default value `5432` if you dont set it.
___

## How to run

Here how to run natively:
1. Activate VirtualEnv on Python first
2. Make sure your CONFIGURATION is Ok.
3. And you can run this app with `sh run.sh ` if you run in linux/macos environment or `.\run.ps1` if you run in windows with powershell , it install all dependencies. 
4. Or manually run with `python manage.py runserver` if all dependencies installed and database has been migrated.
5. use docker-compose by run `sh run-docker.sh`
### Notes

This app has been installed with Swagger. You can access it on `/` endpoints.
This app has been tested. You can access the result on `/test-result/index.html` endpoints.

___

## Models

Here is models of Soccer API, it has 2 main models: Team & Player that inheritanced from BaseModel

```python
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
    # When a team deleted, player's team become null.
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name="player", null=True)

```

___

## Endpoints and JSON Scheme

Here the endpoints:

`/v1/team/` GET all teams, POST a team
`/v1/team/<id>` GET a team, PUT a team, PATCH a team, DELETE a team

`/v1/player/` GET all players, POST a player
`/v1/player/<id>` GET a player, PUT a player, PATCH a player, DELETE a player

### Player JSON
Here the JSON scheme:

Example player request single
```json
{
    "name": "Name",
    "number": 1,
    "team": 1
}
```
or... you can bulk create player in POST
```json
[
    {
       "name": "Name",
       "number": 1,
       "team": 1
    },
    {
       "name": "Jorge",
       "number": 2,
       "team": 1
    },
    {
       "name": "Hansen",
       "number": 3,
       "team": 1
    }
]
```

Example response body:
```json
[
  {
    "id": 1,
    "date_created": "2020-09-11T06:39:44.342339Z",
    "date_modified": "2020-09-11T06:39:44.342339Z",
    "name": "Name",
    "number": 1,
    "team": 1
  },
  {
    "id": 2,
    "date_created": "2020-09-11T06:39:44.354305Z",
    "date_modified": "2020-09-11T06:39:44.354305Z",
    "name": "Jorge",
    "number": 2,
    "team": 1
  },
  {
    "id": 3,
    "date_created": "2020-09-11T06:39:44.369020Z",
    "date_modified": "2020-09-11T06:39:44.369020Z",
    "name": "Hansen",
    "number": 3,
    "team": 1
  }
]
```
### Team JSON
Example request body:
```json
{
    "name" : "Team Name"
}
```
Example team response body:
```json
[
  {
    "player": [
      {
        "name": "Name",
        "number": 1,
        "id": 1
      },
      {
        "name": "Jorge",
        "number": 2,
        "id": 2
      },
      {
        "name": "Hansen",
        "number": 3,
        "id": 3
      }
    ],
    "name": "Persibas Banyumas",
    "id": 1,
    "date_created": "2020-09-11T06:38:28.679675Z",
    "date_modified": "2020-09-11T06:38:28.679675Z"
  }
]
```

___ 
