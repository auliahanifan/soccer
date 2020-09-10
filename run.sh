python -m pip install -r requirements.txt
python manage.py migrate
python manage.py migrate team
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
python manage.py runserver
