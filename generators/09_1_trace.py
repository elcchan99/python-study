from libs import select
from libs.apachelog import apache_log
from libs.gentrace import trace
from libs.linesdir import lines_from_dir

lines = lines_from_dir("access_log*.log", "www")
logs = apache_log(lines)
logs = select.first(logs, n=25)
r404 = (r for r in logs if r["status"] == 404)
r404 = trace(r404)
list(r404)
