mkdir django
cd django
pip install virtualenv
virtualenv --python=python3.5 venv
. venv/bin/activate
pip install Django==2.1.3
django-admin startproject mysite
deactivate


rm mysite/mysite/wsgi.py
# vim mysite/mysite/wsgi.py # copy below
# vim mysite/mysite/settings.py # add '*'  to allowed_hosts
# cd
# sudo mv django/ /var/www/django/
#
# sudo vim /etc/apache2/conf-available/wsgi.conf #copy below
# sudo a2enconf wsgi
# sudo /etc/init.d/apache2 restart
