import multiprocessing

#preload_app is gunicorn settings,http://docs.gunicorn.org/en/stable/settings.html#server-mechanics
preload_app = True
timeout = 300
#bind = "127.0.0.1:8080"
bind = "0.0.0.0:8080"
pythonpath = "/home/vagrant/Github/DjangoNginxGunicorn/PythonDjango/Django1421/mysite"

workers = (multiprocessing.cpu_count()-1) * 4 + 4
