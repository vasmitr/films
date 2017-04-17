#! /bin/bash
#sudo killall gunicorn
sudo systemctl restart nginx
source venv/bin/activate
cd project/
python manage.py runserver
#gunicorn -b 127.0.0.1:8000 Tickets.wsgi:application &
cd ../
