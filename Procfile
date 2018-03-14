release: python ./call_records/manage.py migrate
web: gunicorn --chdir ./call_records call_records.wsgi
