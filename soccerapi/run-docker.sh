docker-compose --env-file ./.env up -d 
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py migrate team
docker-compose exec web python manage.py test