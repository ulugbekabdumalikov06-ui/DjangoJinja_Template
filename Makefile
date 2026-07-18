mig:
	python manage.py makemigrations
	python manage.py migrate

admin:
	puthon manage.py createsuperuser