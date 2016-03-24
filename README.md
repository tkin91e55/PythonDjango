The picture is like:
Nginx is the front proxy server of gunicorn server, gunicorn server Django1421 project.
Nginx already set to auto start up by installation, but gunicorn server is monitored by supervisord, set to auto started by supervisord
Neither supervisord is auto-start, need to put root/etc/init/supervisor.conf under /etc/init.

Config:
(1) things under root/ put to system / according to hierarchy
(2) Django1421/mysite_gunicorn.py is config between Django and Gunicorn
(3) root/etc/nginx/site-enabled/gunicornMysite is Nginx config for Gunicorn
(4) root/etc/init/supervisor.conf is auto-starting supervisord 
(5) supervisordConfig/supervisord.conf is supervisord config
(6) supervisordConfig/conf.d/mysite.conf, config between Gunicorn and supervisor
(7) 

A lot hard-coded settings:
(1) mysite_gunicorn.py:
	bind = "0.0.0.0:8080"
	pythonpath = "/home/vagrant/Github/DjangoNginxGunicorn/PythonDjango/Django1421/mysite"
(2) gunicornMysite:
	root /home/vagrant/Github/DjangoNginxGunicorn/PythonDjango/Django1421/mysite;
	proxy_pass http://0.0.0.0:8080;
(3) supervisor.conf:
	exec /home/vagrant/Github/DjangoNginxGunicorn/PythonDjango/venvs/supervisorVenvs/bin/supervisord -n --configuration /home/vagrant/Github/DjangoNginxGunicorn/PythonDjango/supervisordConfig/supervisord.conf
(4) supervisord.conf:
	(a lot)
	(there is socket and supervisord IP)
(5) mysite.conf:
	(skip)	
	(there is IP config)

Remarks:
(1) put etc/init/supervisor.conf under system /etc/init to auto start the service
(2) need to edit the Django1421/mysite/settings.py STATIC_ROOT
(3) in supervisord.conf, need to create the var/log file if doesn't exist, supervisord won't create by self.
        also var/supervisor, var/log/supervisor

References:
(1) https://jeffknupp.com/blog/2012/10/24/starting-a-django-14-project-the-right-way/


Softwares:
(1)nginx version: nginx/1.1.19
