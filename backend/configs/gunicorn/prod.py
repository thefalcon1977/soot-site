import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'  # Changed from 'gevent' to 'sync'
# worker_connections = 1000  # Not needed for sync workers
max_requests = 1000
timeout = 60
graceful_timeout = 65
keepalive = 65
preload_app = True
daemon = False
sendfile = True

# 
proc_name = "metricz"

# log
accesslog = '/app/logs/gunicorn/access.log'
log_level = 'info'
errorlog = '/app/logs/gunicorn/error.log'

# debug
reload = False
