import multiprocessing
import os

bind = os.getenv("WEB_BIND", "0.0.0.0:5000")
# access_log_format = '%({x-forwarded-for}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
access_log_format = '%({Fly-Client-Ip}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
accesslog = "-"
errorlog = "-"
capture_output = True

cpu_count = multiprocessing.cpu_count() * 2 + 1

workers = int(os.getenv("WEB_CONCURRENCY", cpu_count))
threads = int(os.getenv("PYTHON_MAX_THREADS", "1"))

reload = bool(os.getenv("WEB_RELOAD", False))
