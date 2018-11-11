. venv/bin/activate

django-admin startproject mysite
sed -i "s/'django.contrib.staticfiles',/'django.contrib.staticfiles','rest_framework'/" /home/ubuntu/django/mysite/mysite/settings.py
sed -i "s/'DIRS': [],/'DIRS': ['var/www/django/mysite/mysite/templates'],/" /home/ubuntu/django/mysite/mysite/settings.py
echo 'STATIC_ROOT = "/var/www/django/static/"' >> /home/ubuntu/django/mysite/mysite/settings.py
python mysite/manage.py migrate
rm mysite/mysite/urls.py
rm mysite/mysite/views.py

deactivate
