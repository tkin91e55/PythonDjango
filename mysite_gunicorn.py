import multiprocessing

preload_app = True
timeout = 300
bind = "127.0.0.1:8080"
pythonpath = "/home/vagrant/Github/DjangoNginxGunicorn/PythonDjango/Django1421/mysite"

workers = (multiprocessing.cpu_count()-1) * 4 + 4
